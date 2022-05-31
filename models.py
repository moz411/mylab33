from . import base
db = base.db
app = base.app

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    images = db.relationship('Images', backref='article', lazy=True)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    story = db.Column(db.String(1000), nullable=True)
    image = db.Column(db.String(200), nullable=False)
    href = db.Column(db.String(200), nullable=False)
    icons = db.relationship('Icons', backref='contacts', lazy=True)

class Projets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), nullable=True)
    href = db.Column(db.String(200), nullable=True)
    description = db.Column(db.String(200), nullable=True)
    href2 = db.Column(db.String(200), nullable=True)
    description2 = db.Column(db.String(200), nullable=True)
    video = db.Column(db.String(1000), nullable=True)
    start = db.Column(db.Integer, nullable=False)
    
class Icons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), nullable=False)
    href = db.Column(db.String(200), nullable=False)
    alt = db.Column(db.String(50), nullable=True)
    contacts_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)

class Divers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre  = db.Column(db.String(50), nullable=True)
    texte = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(50), nullable=True)
    href = db.Column(db.String(50), nullable=True)