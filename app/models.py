from app import db

class Merchants(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

    @staticmethod
    def get_all():
        return Merchants.query.all()

    def __repr__(self):
        return "<Merchant: {}>".format(self.name)

class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

    @staticmethod
    def get_all():
        return Customers.query.all()

    def __repr__(self):
        return "<Customers: {}>".format(self.name)

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


