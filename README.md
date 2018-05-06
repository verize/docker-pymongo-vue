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
```

3. Install client js dependencies, compile assets:
```
yarn install && yarn upgrade
yarn run dev
```

4. Run server:
```
python server.py
```


Server will run by default under http://localhost:5000 

###Licensing:

The code in this project is licensed under [MIT LICENSE](LICENSE). Read file for more information.

###TODOs:
- Adds Webpack HMR (Hot Module Replacement)
- Adds SSR (Server Side Rendering) 
- Enable MongoDB checking, connection
- Adds Prettier and Python Linters