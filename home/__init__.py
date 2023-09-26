from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
swagger = Swagger(app)

@app.route('/')
def home():
    return f'<h1>WELCOME TO PIZAA RESTAURANT</h1>'


from home import routes, models
