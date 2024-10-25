from flask import Flask, render_template
import config as config
from flask_assets import Environment, Bundle
from webassets.script import CommandLineEnvironment

app = Flask(__name__,
            template_folder='./app/template/',
            static_folder='./app/static/'
            )
# Загружаем конфигурацию
app.config.from_object('config.DevelopementConfig')

assets = Environment(app)
scss = Bundle(
    './style.scss',
    filters=['libsass', 'cssmin'],  # libsass - компиляция, cssmin - минификация
    output='./app/static/css/main.css'  # Выходной скомпилированный файл
)
assets.register('scss_all', scss)


@app.route('/')
def home():
    return render_template('home/index.html')

@app.route('/admin')
def admin():
    return render_template('admin/index.html')



""" @app.cli.command('watch')
def watch():
    cmdenv = CommandLineEnvironment(assets, app.logger)
    cmdenv.watch()
 """


if __name__ == '__main__':
    app.run()