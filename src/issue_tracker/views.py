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
                "author": {
                    "name": "Yara Stafievskaya",
                    "datetime": "18:23",
                    "status": "rejected"
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
