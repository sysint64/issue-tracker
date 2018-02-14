from issue_tracker import views
from views import index


def setup_static_routes(app):
    app.router.add_static('/static-compress/',
                          path="/home/andrey/projects/issue_tracker/var/static",
                          name='static-compress')
    app.router.add_static('/static/',
                          path="/home/andrey/projects/issue_tracker/frontend/static",
                          name='static')


def setup_routes(app):
    app.router.add_get('/', index, name="index")
    app.router.add_get('/ws', views.websocket_handler, name="ws")
    app.router.add_get('/issues', views.issues, name="issues")
    app.router.add_get('/help', views.help, name="help")
    app.router.add_get('/sight-out', views.sight_out, name="sight-out")
