from aiohttp import web

from db import init_pg, close_pg
from routes import setup_routes, setup_static_routes

import jinja2
import aiohttp_jinja2
from jac import CompressorExtension


app = web.Application()
setup_routes(app)
setup_static_routes(app)
# conf = load_config(str(pathlib.Path('.') / 'config' / 'polls.yaml'))
# app['config'] = conf

DEBUG = True

aiohttp_jinja2.setup(
    app,
    loader=jinja2.FileSystemLoader("/home/andrey/projects/issue_tracker/frontend/templates/"),
    extensions=[CompressorExtension]
)

app[aiohttp_jinja2.APP_KEY].compressor_output_dir = '/home/andrey/projects/issue_tracker/var/static'
app[aiohttp_jinja2.APP_KEY].compressor_static_prefix = '/static'
app[aiohttp_jinja2.APP_KEY].compressor_source_dirs = '/home/andrey/projects/issue_tracker/frontend/static'

web.run_app(app, host='127.0.0.1', port=12345)
