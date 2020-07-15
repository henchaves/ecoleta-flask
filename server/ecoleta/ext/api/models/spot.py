from ecoleta.ext.db import db

class SpotModel(db.Model):
    __tablename__ = "spots"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(80), unique=True)
    uf = db.Column("uf", db.String(2))
    city = db.Column("city", db.String(80))
    categories = db.Column("categories", db.String(80))

    def __init__(self, name, uf, city, categories):
        self.name = name
        self.uf = uf
        self.city = city
        self.categories = categories
    
    def json(self):
        return {
            "name": self.name,
            "uf": self.uf,
            "city": self.city,
            "categories": self.categories
        }

    def save_spot(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_spot(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()


