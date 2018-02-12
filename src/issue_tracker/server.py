from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


def init(argv):
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)
    return app
