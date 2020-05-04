import asyncio
import aiohttp
import json
from .base import BaseSpider


class BaseApiWrapper(BaseSpider):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_page_size(self):
        """
        Pagination page size
        :return: int: page_size
        """
        raise NotImplementedError("Subclasses should implement this!")

    def get_total(self, *args, **kwargs):
        """
        Return total count for pagination
        :param args:
        :param kwargs:
        :return: int: total
        """
        raise NotImplementedError("Subclasses should implement this!")

    def get_urls(self, *args, **kwargs):
        """
        List of url for requests
        :return: list: urls
        """
        raise NotImplementedError("Subclasses should implement this!")

    def update_data(self, data):
        """
        Transform data from API response to ww format
        :param data: api response
        :return: list: updated_data
        """
        raise NotImplementedError("Subclasses should implement this!")

    async def fetch(self, client, url, retry=True, max_attempt=3):
        resp = await self.requester.fetch(client, url, retry=retry, max_attempt=max_attempt)
        return json.loads(resp)

    async def request_data(self, url):
        async with aiohttp.ClientSession() as client:
            return await self.fetch(client, url)

    async def parse_data(self, page):
        data = await self.request_data(page)
        update_data = self.update_data(data)
        return self.save_items(update_data)

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.set_debug(self.crawler.settings.get('DEBUG'))
        tasks = [self.parse_data(url) for url in self.get_urls()]
        if tasks:
            loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=not settings.DEBUG))
        loop.close()
