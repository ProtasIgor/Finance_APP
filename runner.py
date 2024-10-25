from flask import render_template, make_response, url_for
from app.app import app
import app.assets.assets as assets
import config as config
from flask_cors import CORS

# Загружаем конфигурацию
app.config.from_object('config.DevelopementConfig')

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')

@app.route('/test')
def index2():
    return "<link rel='stylesheet' href='app/static/css/style.css'>Главная страница"


if __name__ == '__main__':
    app.run()