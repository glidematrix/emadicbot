from crypt import methods
import os
from emadicbot.views.api.v1 import bp


@bp.route('/telegram/webhook', methods=['POST'])
def telegram_webhook():

    res = {}

    return res


@bp.route('/test')
def test():

    res = {}

    return res