from flask import render_template, request, send_from_directory
from sqlalchemy.sql.expression import asc, desc

from . import base
db = base.db
app = base.app
t = base.t
from .models import Article, Images, Contacts, Projets, Icons, Divers


@t.include
@app.route('/')
def index():
    articles = list(db.session.query(Article).join(Images))
    contacts = list(db.session.query(Contacts).join(Icons))
    projets = list(db.session.query(Projets).order_by(desc(Projets.id)))
    divers = list(db.session.query(Divers))
    return render_template('index.html', articles=articles, contacts=contacts, projets=projets, divers=divers)


@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/google464558d1461f9002.html')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/CV_tdupouy_OC.pdf')
def staticfiles():
    return send_from_directory(app.static_folder + "/files", request.path[1:])