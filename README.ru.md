# scrapy-boilerplate

Это шаблон для новых проектов на Scrapy.

*Проект является WIP, поэтому может серьезно измененятся и дополнятся со временем. Master ветка должна считаться всегда готовой к использованию.*

## Features

- Python 3.8+
- [Poetry](https://github.com/python-poetry/poetry) в качестве менеджера зависимостей
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) ORM с [alembic](https://github.com/sqlalchemy/alembic) для миграций 
- [pika](https://github.com/pika/pika/) для работы с RabbitMQ
- настройка с помощью `ENV`(переменных среды) и/или `.env` файла
- один файл для каждого класса
- [Black](https://github.com/psf/black) чтобы обеспечить единообразие кодового стиля (см. [here](#black))
- Docker-ready (см. [here](#docker))
- PM2-ready (см. [here](#pm2))
- supports single-IP/rotating proxy config out of the box (см. [here](#proxy-middleware))

## Installation

Для создания нового проекта с использованием данного шаблона необходимо:

1. Клонировать репозиторий
2. Установить зависимости: `poetry install`, `npm ci`
3. Активировать виртуальное окружение `poetry shell` либо через настройки IDE
4. Активировать git/hooks `pre-commit install`

## Usage

Шаблон поставляется с некоторыми заранее написанными классами, вспомогательными скриптами и функциями, которые описаны в этом разделе.

### Docker

The project includes Dockerfiles and docker-compose configuration for running your spiders in containers.

Also, a configuration for default RabbitMQ server is included.

Dockerfiles are located inside the `docker` subdirectory, and the `docker-compose.yml` - at the root of the project. You might want to change the `CMD` of the scrapy container to something more relevant to your project. To do so, edit `docker/scrapy/Dockerfile`.

Docker-compose takes configuration values from ENV. Environment can also be provided by creating a `.env` file at the root of the project (see `.docker_env.example` as a sample). Creating of dotenv for docker is handled in the `install.sh` script by default.

### Black

Black is the uncompromising Python code formatter. It is used in thsi project to ensure code style consistensy in the least intrusive fashion.

Black is included in Pipfile dev-dependencies. A pre-commit hook for running autoformatting is also included, via [pre-commit](https://pre-commit.com) tool. It is installed automatically, if you run `install.sh`. Otherwise, to use it you need to run `pre-commit install` in the root project folder after installing pre-commit itself.

### PM2

This boilerplate contains a sample PM2 config file along with a bash startup script that sets up all the necessary environment to run scrapy with this process manager.

All you need to do, is copy/edit `src/pm2/commands/command_example.sh` and change the `exec` part to the command actually needed to be run, and then create `process.json` ecosystem file (based on `src/pm2/process.example.json`) to start the script.

Then, cd to `src/pm2` and run `pm2 start process.json`.

### Proxy middleware

A scrapy downloader middleware to use a proxy server is included in `src/middlewares/HttpProxyMiddleware.py` and is enabled by default. You can use it by providing proxy endpoint with the env variable (or in the `.env` file) `PROXY` in the format `host:port`. Proxy authentication can also be provided in the `PROXY_AUTH` variable, using the format `user:password`. If provided, it is encoded as a Basic HTTP Auth and put into `Proxy-Authorization` header.

A single-endpoint proxy is used by default, assuming usage of rotating proxies service. If you want to provide your own list of proxies, an external package has to be used, as this use-case is not yet covered by this boilerplate.

## File and folder structure

This boilerplate offers a more intuitive alternative to Scrapy's default project structure. Here, file/directory structure is more flattened and re-arranged a bit.

- All scrapy-related code is placed directly in `src` subdirectory (without any subdirs with project name, contrary to default).
- All scrapy classes (by default located in `items.py, middlewares.py, pipelines.py`) are converted to sub-modules, where each class is placed in its own separate file. Nothing else goes into those files. Helper functions/modules can be placed in the `helpers` module.
- Configs in `scrapy.cfg` and `settings.py` are edited to correspond with these changes.
- Additional subdirectories are added to contain code, related to working with database (`src/database`), RabbitMQ (`src/rabbitmq`).
