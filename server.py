# http://python-eve.org/config.html

import os
from eve import Eve
from src.auth import BCryptAuth
from flask import render_template
from src.swagger import init_swagger
from eve_healthcheck import EveHealthCheck

app = Eve(
    __name__,
    auth=BCryptAuth,
    settings='./config/config_dev.py',
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
    app.run(debug=True)
