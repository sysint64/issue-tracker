from views import index
from issue_tracker.views import get as get_views
from issue_tracker.views import actions as actions_views


def setup_static_routes(app):
    app.router.add_static('/static-compress/',
                          path="/home/andrey/projects/issue-tracker/var/static",
                          name='static-compress')
    app.router.add_static('/static/',
                          path="/home/andrey/projects/issue-tracker/frontend/static",
                          name='static')


def setup_routes(app):
    app.router.add_get('/', index, name="index")
    app.router.add_get('/ws', get_views.websocket_handler, name="ws")

    app.router.add_get('/issues', get_views.issues, name="issues")
    app.router.add_get('/issues/create', actions_views.issues_create, name="issues_create")
    app.router.add_post('/issues/create', actions_views.issues_create, name="issues_create_post")
    app.router.add_get(r'/issues/{id:\d+}', get_views.issue, name="issue")

    app.router.add_get('/help', get_views.help, name="help")
    app.router.add_get('/sight-out', get_views.sight_out, name="sight-out")
