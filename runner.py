from app.app import app
from gevent.pywsgi import WSGIServer
import app.assets.assets as assets
import config as config

# Загружаем конфигурацию
app.config.from_object('config.DevelopementConfig')

from flask_cors import CORS
CORS(app)

import app.view.admin.view as admin_view
import app.view.site.view as site_view
import app.view.api.view as api_view

if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0", 5000), app)
    http_server.serve_forever()
    """ app.run(host='0.0.0.0', port=5000) """