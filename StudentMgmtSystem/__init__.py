from os import environ
from StudentMgmtSystem.extensions import db, csrf, Flask
from StudentMgmtSystem.backend.database.model import Student, add_values
from StudentMgmtSystem.frontend.views.index import index_page


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("FLASK_SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = environ.get("FLASK_SECRET_KEY")

    db.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(index_page, url_prefix="/")

    with app.app_context():
        # db.drop_all()
        # db.create_all()
        # add_values()
        pass

    return app
