# http://python-eve.org/config.html

import os
from eve import Eve
from flask import Response, json
from src.auth import BCryptAuth
from flask import render_template

app = Eve(__name__, auth=BCryptAuth, settings='config_dev.py', static_folder='build')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/status', methods=['GET'])
def status():
    data = json.dumps({
        'success': True,
        'version': '1.0'
    })

    return Response(data, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
