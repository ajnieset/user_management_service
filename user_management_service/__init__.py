from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return {"message": "Welcome to User Manager!"}

    from .users import user

    app.register_blueprint(user.bp)

    return app
