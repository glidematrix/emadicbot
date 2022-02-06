from flask import Blueprint

bp = Blueprint(
    'api_v1',
    __name__,
    url_prefix='/api/v1'
)

from emadicbot.views.api.v1 import handlers