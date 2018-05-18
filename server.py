# http://python-eve.org/config.html

from eve import Eve
from src.auth import BCryptAuth
from flask import render_template
from config.config import get_app_config
from src.swagger import init_swagger
from eve_healthcheck import EveHealthCheck
from flask_debugtoolbar import DebugToolbarExtension


app_settings = get_app_config()

app = Eve(
    __name__,
    auth=BCryptAuth,
    settings=app_settings,
    static_folder='./build',
    template_folder="./build"
)

with app.app_context():
    init_swagger()

status = EveHealthCheck(app, '/status')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    toolbar = DebugToolbarExtension(app)
    toolbar.init_app(app)
    app.run()
