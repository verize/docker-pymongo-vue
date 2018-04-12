## PyMongoVue Stack

**An open source stack:** Python3 + Flask/Eve framework + MongoDB + Vue.js-ES6 client

- RESTful API
- NoSQL Storage
- Javascript-ES6 client

**Author:** Gonzalo Plaza <gonzalo@verize.com>

**Installation:**

1. Clone repository
```
git clone https://github.com/gonzaloplaza/py-mongo-vue.git py-mongo-vue
cd py-mongo-vue
```
2. Add Python Virtual Environment and install dependencies
```
virtualenv venv
. venv/bin/activate
python setup.py install 
```

3. Install client js dependencies:
```
yarn install && yarn upgrade
```

4. Run server:
```
python run.py
```


Server will run by default under http://localhost:5000 