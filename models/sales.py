from main import db


class Sales(db.Model):
    sale_id = db.Column(db.Integer, primary_key=True)
    inv_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    sell_date = db.Column(db.DATE, nullable=False)

    def add_records(self):
        db.session.add(self)

        db.session.commit()

        # Fetch all records

    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    # fetch one record

    @classmethod
    def fetch_one_record(cls):
        return cls.query.filter_by(id=1).first()
