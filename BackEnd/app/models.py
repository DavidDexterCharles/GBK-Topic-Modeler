import flask_restless
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_pyfile('config.cfg')


db = SQLAlchemy(app)

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    publicationdate = db.Column(db.String(80))
    content = db.Column(db.String(12000))
    articlecategories = db.relationship('Articlecategorie', backref= 'article', lazy='dynamic')
    geotags = db.relationship('Geotag', backref= 'article', lazy='dynamic')


class Articlecategorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.String(250))

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    desc = db.Column(db.String(250))
    articlecategories = db.relationship('Articlecategorie', backref= 'categorie', lazy='dynamic')


class Geotag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publishdate = db.Column(db.String(250))
    content = db.Column(db.String(250))

    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
restless_manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

if __name__ == '__main__':
    manager.run()
