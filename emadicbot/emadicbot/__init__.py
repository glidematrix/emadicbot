# import os
from flask import Flask

def create_app():
    """
    """
    app = Flask(__name__)

    app.config.from_object('emadicbot.config.Config')

    from emadicbot.views.api import v1
    app.register_blueprint(v1.bp)

    return app