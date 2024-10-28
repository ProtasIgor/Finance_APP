from flask import render_template, make_response, url_for, request, g
from app.app import app
import app.assets.assets as assets
import config as config

# Загружаем конфигурацию
app.config.from_object('config.DevelopementConfig')

from flask_cors import CORS
CORS(app)

import app.view.site.view as site_view
import app.view.api.view as api_view

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)