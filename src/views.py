import aiohttp_jinja2
from aiohttp import web

import db


@aiohttp_jinja2.template("login.html.j2")
async def index(request):
    return {
        "project_title": "Issue tracker",
        "page_title": "Login",
        "test": 12
    }


@aiohttp_jinja2.template("detail.html.j2")
async def poll(request):
    return {
        "test": 12
    }
    # async with request['db'].acquire() as conn:
    #     question_id = request.match_info['question_id']
    #
    #     try:
    #         question, choices = await db.get_question(conn, question_id)
    #     except db.RecordNotFound as e:
    #         raise web.HTTPNotFound(text=str(e))
    #
    #     return {
    #         'question': question,
    #         'choices': choices
    #     }
