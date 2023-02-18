from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://postgres:sevillaespagne@localhost:5432/store'

db = SQLAlchemy(app)
api = Api(app)

migrate = Migrate(app, db)


class BookModel(db.Model):
    __tablename__ = "books"
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    test_something = db.Column(db.String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class BookResource(Resource):
    def post(self):
        data = request.get_json()
        book: BookModel = BookModel(**data)
        db.session.add(book)
        db.session.commit()
        return book.as_dict()


api.add_resource(BookResource, "/books/")

if __name__ == '__main__':
    app.run()