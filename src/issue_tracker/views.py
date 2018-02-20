import aiohttp
from aiohttp import web
import aiohttp_jinja2


async def fetch_issues(cursor):
    await cursor.execute("SELECT id, name, pub_date FROM issues")

    async for row in cursor:
        yield {
            "id": row[0],
            "name": row[1],
            "status": "ok",
            "datetime": row[2],
            "author": {
                "name": "Andrey Kabylin",
            },
            "tags": [
                "security",
                "performance"
            ]
        }


async def items(async_generator):
    return [item async for item in async_generator]


@aiohttp_jinja2.template("issues.html.j2")
async def issues(request):
    async with request.app['db'].acquire() as conn:
        async with conn.cursor() as cursor:
            return {
                "page_title": "Issues",
                "issues": await items(fetch_issues(cursor)),
                "filters": [
                    {
                        "name": "Tags",
                        "count": 4,
                        "fields_type": "links",
                        "addable": True,
                        "children": [
                            {
                                "name": "Security",
                            },
                            {
                                "name": "Performance",
                            },
                            {
                                "name": "Documents",
                            },
                            {
                                "name": "Server",
                            }
                        ]
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
                                "children": [
                                    {
                                        "name": "Security",
                                    },
                                    {
                                        "name": "Performance",
                                    },
                                    {
                                        "name": "Documents",
                                    },
                                    {
                                        "name": "Server",
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }


@aiohttp_jinja2.template("issue.html.j2")
async def issue(request):
    return {
        "page_title": "План 12",
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
