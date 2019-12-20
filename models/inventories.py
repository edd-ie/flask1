from main import db
from models.sales import Sales


class Inventories(db.Model):
    inv_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    sales = db.relationship('Sales', backref='inventory', lazy=True)

    def add_records(self):
        db.session.add(self)
        db.session.commit()

    # Fetch all records
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    # fetch one record
    @classmethod
    def fetch_one_record(cls, inv_id):
        return cls.query.filter_by(inv_id=inv_id).first()

 # class Authenticator:
 #    while Inventories.stock <= 0:
 #        print("Stock Refill")
