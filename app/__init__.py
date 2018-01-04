from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request, jsonify, abort

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
    from app.models import Merchants, Customers
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)
    db.init_app(app)

    @app.route('/api/v1/merchants/<int:id>', methods=['GET'])
    def one_merchant(id):
        merchant = Merchants.get_one(id)
        results = {
                'id': merchant.id,
                'name': merchant.name
        }
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/merchants/random', methods=['GET'])
    def get_random_merchant():
        merchant = Merchants.get_random()
        results = {
                'id': merchant.id,
                'name': merchant.name
        }
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/merchants', methods=['GET'])
    def all_merchants():
        merchants = Merchants.get_all()
        results = []

        for merchant in merchants:
            obj = {
                'id': merchant.id,
                'name': merchant.name
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/customers', methods=['GET'])
    def all_customers():
        customers = Customers.get_all()
        results = []

        for customer in customers:
            obj = {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    return app
