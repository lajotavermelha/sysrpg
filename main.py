from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/sysrpg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)
if __name__ == '__main__':
    from routes import *
    app.run(debug=True)