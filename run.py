# http://python-eve.org/config.html

import os
from eve import Eve
from flask import Response, json
from src.auth import BCryptAuth

app = Eve(auth=BCryptAuth, settings='config_dev.py')


@app.route('/', methods=['GET'])
def index():
    data = json.dumps({
        'success': True,
        'version': '1.0'
    })

    return Response(data, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)