[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Statistic-Crawler

## Prerequisites

- [pip](https://pip.pypa.io/en/stable/installing/)
- [Docker](https://docs.docker.com/docker-for-mac/install/)

## Setup pre-commit pipeline
Install pre-commit:

> `pip install pre-commit`

To setup pre-commit hooks use:

> `pre-commit install`

## Local Development

Start the dev server for local development:
```bash
make run
```

Format all code:
```bash
make black
```
