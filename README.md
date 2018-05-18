## PyMongoVue Stack

**An open source stack:** Python3 + Flask/Eve framework + MongoDB + Webpack4 + Vue.js-ES6 client

- RESTful API + Swagger Api Docs
- Authentication
- NoSQL Storage
- Javascript-ES6 client + Webpack

**Author:** Gonzalo Plaza <gonzalo@verize.com>

### Installation:

1. Clone repository
```
git clone https://github.com/verize/py-mongo-vue.git py-mongo-vue
cd py-mongo-vue
```
2. Add Python Virtual Environment and install dependencies
```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -r dev-requirements.txt

```

Note: To upgrade Pip requirements, just execute (and follow instructions):
```
pip-upgrade
```

3. Install client js dependencies, compile assets:
```
yarn install && yarn upgrade
yarn run dev
```

4. App configuration
You need to copy .env.dist to .env file (root folder) and set your own parameters
To generate secret key visit this page: https://randomkeygen.com/

Configuration vars:
```
FLASK_ENV=development
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DBNAME=''
MONGO_USERNAME=''
MONGO_PASSWORD=''
SECRET_KEY=''
```

5. Run server:
```
python server.py
```


Server will run by default under http://localhost:5000 

### Licensing:

The code in this project is licensed under [MIT LICENSE](LICENSE). Read file for more information.

### TODOs:

- Adds Webpack HMR (Hot Module Replacement)
- Adds SSR (Server Side Rendering) 
- Improve Authentication process / roles
- Installation command
- Adds Prettier and Python Linters
- Basic Tests