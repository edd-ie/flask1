from main import db


class Inventories(db.Model):
    inv_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    buying_price = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def add_records(self):
        db.session.add(self)

        db.session.commit()

        # Fetch all records

    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    # fetch one record

    @classmethod
    def fetch_one_record(cls,id):
        return cls.query.filter_by(id=id).first()
