from aiohttp import web

import context_processors
from db import init_pg, close_pg
from issue_tracker.repository import Repository
from routes import setup_routes, setup_static_routes

import jinja2
import aiohttp_jinja2
from jac import CompressorExtension
import aiohttp_debugtoolbar
import asyncio

loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
aiohttp_debugtoolbar.setup(app)

app["config"] = {
    "postgres": {
        "database": "issue_tracker",
        "user": "issue_tracker",
        "password": "123321",
        "host": "localhost",
        "port": 5432,
        "minsize": 1,
        "maxsize": 5
    }
}

app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)


def create_repository_context():
    return Repository(app)


app.connect_repository = create_repository_context

setup_routes(app)
setup_static_routes(app)

aiohttp_jinja2.setup(
    app,
    context_processors=[
        context_processors.project_info_processor,
        aiohttp_jinja2.request_processor
    ],
    loader=jinja2.FileSystemLoader("/home/andrey/projects/issue-tracker/frontend/templates/"),
    extensions=[CompressorExtension]
)

app[aiohttp_jinja2.APP_KEY].compressor_output_dir = '/home/andrey/projects/issue-tracker/var/static'
app[aiohttp_jinja2.APP_KEY].compressor_source_dirs = '/home/andrey/projects/issue-tracker/frontend/static'
app[aiohttp_jinja2.APP_KEY].compressor_static_prefix = '/static-compress'

web.run_app(app, host='127.0.0.1', port=12345)
