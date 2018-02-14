import aiohttp
from aiohttp import web
import aiohttp_jinja2


@aiohttp_jinja2.template("issues.html.j2")
async def issues(request):
    return {
        "page_title": "Issues",
        "issues": [
            {
                "id": "PLAN-1",
                "name": "План 1",
                "status": "ok",
                "datetime": "17:54",
                "author": {
                    "name": "Andrey Kabylin",
                },
                "history": [
                    {
                        "action": "Updated",
                        "author": {
                            "name": "Andrey Kabylin",
                        },
                    }
                ]
            },
            {
                "id": "PLAN-2",
                "name": "План 2",
                "datetime": "07 Dec 17",
                "status": "rejected",
                "author": {
                    "name": "Yara Stafievskaya",
                }
            },
            {
                "id": "PLAN-3",
                "name": "План 3",
                "datetime": "23 Jan",
                "status": "rejected",
                "author": {
                    "name": "Yara Stafievskaya",
                }
            }
        ],
        "projects": [
            {
                "name": "AppCode",
                "count": 120
            }
        ],
    }


@aiohttp_jinja2.template("base.html.j2")
async def help(request):
    return {}


@aiohttp_jinja2.template("base.html.j2")
async def sight_out(request):
    return {}


# Example
async def websocket_handler(request):
    print('Websocket connection starting')
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print('Websocket connection ready')

    # noinspection PyTypeChecker
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())

    print('websocket connection closed')
    return ws
