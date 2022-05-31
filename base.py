from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_track_usage import TrackUsage
from flask_track_usage.storage.sql import SQLStorage
# from flask_compress import Compress

app = Flask(__name__)
app.config.from_object('mylab33.config')
db = SQLAlchemy(app)
# Compress(app)
# Set the configuration items manually for the example
app.config['TRACK_USAGE_USE_FREEGEOIP'] = False

# tracking
engine = create_engine('sqlite:///tracking.db')
t = TrackUsage(app, SQLStorage(engine=engine))