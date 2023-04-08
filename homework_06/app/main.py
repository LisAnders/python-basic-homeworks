from os import getenv
from flask import Flask, render_template
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

from models import db
from views.articles import article_app


config_name = getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
app.register_blueprint(article_app)

db.init_app(app)
migrater = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


@app.get("/", endpoint="main_page")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()