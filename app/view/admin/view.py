from flask import render_template, make_response, url_for, request, g
from app.app import app

@app.route('/admin')
def admin():
    return render_template('admin/index.html')