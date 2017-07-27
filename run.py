from app import app
from db import db

db.init_app(app)

# neat trick to auto create a DB and tables before a request is pushed through
@app.before_first_request
def create_tables():
    db.create_all()
