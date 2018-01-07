from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import request, jsonify, abort
from flask import render_template

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

    @app.route('/api/v1/customers/<int:id>/invoices', methods=['GET'])
    def get_customer_invoices(id):
        customer = Customers.get_one(id)
        invoices = Customers.get_invoices(id)
        customer_invoices = []

        for invoice in invoices:
            obj = {
                    'id': invoice.id,
                    'customer_id': invoice.customer_id,
                    'merchant_id': invoice.merchant_id,
                    'status': invoice.status
                }
            customer_invoices.append(obj)

        results = {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name,
                'invoices': customer_invoices
            }

        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/merchants/<int:id>/invoices', methods=['GET'])
    def get_merchant_invoices(id):
        merchant = Merchants.get_one(id)
        invoices = Merchants.get_invoices(id)
        merchant_invoices = []

        for invoice in invoices:
            obj = {
                    'id': invoice.id,
                    'customer_id': invoice.customer_id,
                    'merchant_id': invoice.merchant_id,
                    'status': invoice.status
                }
            merchant_invoices.append(obj)

        results = {
                'id': merchant.id,
                'name': merchant.name,
                'invoices': merchant_invoices
            }

        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/merchants/<int:id>/items', methods=['GET'])
    def get_merchant_items(id):
        merchant = Merchants.get_one(id)
        items = Merchants.get_items(id)
        merchant_items = []

        for item in items:
            obj = {
                    'id': item.id,
                    'name': item.name,
                    'description': item.description,
                    'unit_price': item.unit_price
                }
            merchant_items.append(obj)

        results = {
                'id': merchant.id,
                'name': merchant.name,
                'items': merchant_items
            }

        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/api/v1/customers/<int:id>', methods=['GET'])
    def one_custmer(id):
        customer = Customers.get_one(id)
        results = {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name
        }
        response = jsonify(results)
        response.status_code = 200
        return response

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

    @app.route('/api/v1/customers/random', methods=['GET'])
    def get_random_customer():
        customer = Customers.get_random()
        results = {
                'id': customer.id,
                'first_name': customer.first_name,
                'last_name': customer.last_name
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

    @app.route('/', methods=['GET'])
    def root():
        return render_template('index.html')

    return app
