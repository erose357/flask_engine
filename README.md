# Flask Engine
Flask Engine is the Turing School's [Rales Engine](http://backend.turing.io/module3/projects/rails_engine) project written in Python.  It is an API returning JSON from the [SalesEngine](https://github.com/turingschool-examples/sales_engine/tree/master/data) data set.  

hosted at: https://flask-engine-api.herokuapp.com/  

## Getting Started

### Versions
Python 3.6.4  
Flask 0.12.2  
Postgresql 9.6.3

### Prerequisites
[Python3](http://docs.python-guide.org/en/latest/starting/installation/)  
[Pipenv](https://github.com/pypa/pipenv)  
[Postgresql](https://www.postgresql.org/)  

### Setup
#### Database setup:    
create database in `psql`:  
```
$ psql
username=# CREATE DATABASE flask_engine;
CREATE DATABASE
\q
```
#### App Setup/Installation:  
clone the repo and `cd` into the directory:  
```
$ git clone git@github.com:erose357/flask_engine.git
$ cd flask_engine
```
install dependencies:  
`$ pipenv install`   

set the following environment variables(MacOS):  
```
$ export FLASK_APP=run.py
$ export APP_SETTINGS=development
$ export DATABASE_URL=<YOUR_DB_PATH>
```
activate the virtual environment:  
```
$ pipenv shell
Spawning environment shell (/bin/bash). Use 'exit' to leave.
bash-3.2$ source .local/share/virtualenvs/flask_engine-wL03M76k/bin/activate
(flask_engine-wL03M76k) bash-3.2$
```
migrate the database:
```
(flask_engine-wL03M76k) bash-3.2$ python manage.py db upgrade
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 5488175015cc, empty message
```  
seed the database:  
```
(flask_engine-wL03M76k) bash-3.2$ python manage.py seed
merchants table seeded
customers table seeded
items table seeded
invoices table seeded
transactions table seeded
invoice_items table seeded
```  
run the app:  
```
(flask_engine-wL03M76k) bash-3.2$ flask run
 * Serving Flask app "run"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ``` 
 the root path gives an explanation of the currently available endpoints
