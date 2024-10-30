from flask_assets import Environment, Bundle
from app.app import app

assets = Environment(app)
assets.directory = app.static_folder

scss_main = Bundle(
    'scss/main.scss',
    filters=['libsass', 'cssmin'],
    output='css/style.css',
    depends='scss/**/*.scss'
)

scss_contact = Bundle(
    'scss/page/contact.scss',
    filters=['libsass', 'cssmin'],
    output='css/contact.css',
    depends='scss/**/*.scss'
)

scss_admin = Bundle(
    'scss/page/admin.scss',
    filters=['libsass', 'cssmin'],
    output='css/admin.css',
    depends='scss/**/*.scss'
)

assets.register('scss_main', scss_main)
assets.register('scss_contact', scss_contact)
assets.register('scss_admin', scss_admin)