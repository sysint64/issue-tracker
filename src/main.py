from aiohttp import web

import context_processors
from db import init_pg, close_pg
from routes import setup_routes, setup_static_routes

import jinja2
import aiohttp_jinja2
from jac import CompressorExtension
import aiohttp_debugtoolbar


app = web.Application()
aiohttp_debugtoolbar.setup(app)
setup_routes(app)
setup_static_routes(app)

aiohttp_jinja2.setup(
    app,
    context_processors=[
        context_processors.project_info_processor,
        aiohttp_jinja2.request_processor
    ],
    loader=jinja2.FileSystemLoader("/home/andrey/projects/issue_tracker/frontend/templates/"),
    extensions=[CompressorExtension]
)

app[aiohttp_jinja2.APP_KEY].compressor_output_dir = '/home/andrey/projects/issue_tracker/var/static'
app[aiohttp_jinja2.APP_KEY].compressor_static_prefix = '/static-compress'
app[aiohttp_jinja2.APP_KEY].compressor_source_dirs = '/home/andrey/projects/issue_tracker/frontend/static'

web.run_app(app, host='127.0.0.1', port=12345)
