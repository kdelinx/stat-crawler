import asyncio
import logging
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Requester:

    def __init__(self, request_limit=None):
        """
        Making limited per second requests with retries
        :param request_limit: requests rate per second. If None - no limit.
        """
        self.tokens = request_limit
        self.request_limit = request_limit
        self.updated_at = time.monotonic()

    async def fetch(self, client, url, timeout=140, retry=True, max_attempt=3, attempt=1):
        response = await self.get(client, url, timeout=timeout)
        if response.status != 200:
            if retry and attempt <= max_attempt:
                logger.error('Response code: {}. Retry'.format(response.status))
                await asyncio.sleep(0.5)
                return await self.fetch(client, url, timeout, retry, max_attempt, attempt+1)
            else:
                logger.error('Response code: {}. End'.format(response.status))
                return ''
        return await response.text()

    async def get(self, client, *args, **kwargs):
        await self.wait_for_token()
        return await client.get(*args, **kwargs)

    async def wait_for_token(self):
        if self.request_limit:
            while self.tokens <= 0:
                self.add_new_tokens()
                await asyncio.sleep(1)
            self.tokens -= 1

    def add_new_tokens(self):
        now = time.monotonic()
        time_since_update = now - self.updated_at
        new_tokens = time_since_update * self.request_limit
        if self.tokens + new_tokens >= 1:
            self.tokens = min(self.tokens + new_tokens, self.request_limit)
            self.updated_at = now
