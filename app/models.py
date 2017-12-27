from app import db

class Merchants(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
            db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

    @staticmethod
    def get_all():
        return Merchants.query.all()

    def __rep__(self):
        return "<Merchant: {}>".format(self.name)


