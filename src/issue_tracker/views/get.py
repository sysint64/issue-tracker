import aiohttp
from aiohttp import web
import aiohttp_jinja2

from issue_tracker.repository import items


@aiohttp_jinja2.template("issues.html.j2")
async def issues(request):
    async with request.app.connect_repository() as repository:
        tags = [{"name": tag["name"].capitalize()} async for tag in repository.tags()]
        tags_length = await repository.tags_count()

        return {
            "page_title": "Issues",
            "issues": await items(repository.issues()),
            "filters": [
                {
                    "name": "Tags",
                    "count": tags_length,
                    "fields_type": "links",
                    "addable": True,
                    "children": tags
                },
                {
                    "name": "Departments",
                    "count": 4,
                    "fields_type": "links",
                    "addable": True,
                    "children": [
                        {
                            "name": "IT",
                        },
                        {
                            "name": "Security",
                        },
                        {
                            "name": "System administration",
                        },
                        {
                            "name": "Testing",
                        }
                    ]
                },
                {
                    "name": "Filters",
                    "children": [
                        {
                            "name": "Tags",
                            "fields_type": "checkboxes",
                            "addable": False,
                            "children": tags
                        }
                    ]
                }
            ]
        }


@aiohttp_jinja2.template("issue.html.j2")
async def issue(request):
    return {
        "page_title": "План 12"
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
