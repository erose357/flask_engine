from app import db
from  sqlalchemy.sql.expression import func

class Merchants(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())
    items = db.relationship('Items', backref='merchant', lazy='dynamic')
    invoices = db.relationship('Invoices', backref='merchant', lazy='dynamic')

    @staticmethod
    def get_all():
        return Merchants.query.all()

    def get_one(merchant_id):
        return Merchants.query.filter_by(id=merchant_id).first()

    def get_random():
        return Merchants.query.order_by(func.random()).first()

    def get_items(merchant_id):
        merchant = Merchants.query.filter_by(id=merchant_id).first() 
        return merchant.items.all()

    def get_invoices(merchant_id):
        merchant = Merchants.get_one(merchant_id)
        return merchant.invoices.all()

    def __repr__(self):
        return '<Merchant: id=%r, name=%r>' % (self.id, self.name)

class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())
    invoices = db.relationship('Invoices', backref='customer', lazy='dynamic')

    @staticmethod
    def get_all():
        return Customers.query.all()

    def get_one(customer_id):
        return Customers.query.filter_by(id=customer_id).first()

    def get_random():
        return Customers.query.order_by(func.random()).first()

    def __repr__(self):
        return '<Customer: id=%r, first_name=%r, last_name=%r>' % (self.id, self.first_name, self.last_name)

class Items(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    unit_price = db.Column(db.Integer)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

class Invoices(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'))
    status = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

class Transactions(db.Model):
    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'))
    credit_card_number = db.Column(db.Text)
    credit_card_expiration_date = db.Column(db.Text)
    result = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

class InvoiceItems(db.Model):
    __tablename__ = 'invoice_items'
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())
