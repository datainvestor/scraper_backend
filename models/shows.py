from db import db

class ShowsModel(db.Model):
    __tablename__ = 'Shows'

    id = db.Column(db.Integer, primary_key=True)
    imdb_key = db.Column(db.String(80))
    display_data = db.Column(db.JSON)

    def __init__(self, imdb_key, display_data):
        self.imdb_key = imdb_key
        self.display_data = display_data

    def json(self):
        return {
            'id': self.id,
            'imdb_key': self.imdb_key,
            'display_data': self.display_data,
        }

    @classmethod
    def find_by_imdb_key(cls, imdb_key):
        return cls.query.filter_by(imdb_key=imdb_key).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()