from views import index


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path="/home/andrey/projects/issue_tracker/var/static",
                          name='static')


def setup_routes(app):
    app.router.add_get('/', index, name="index")
