from flask import render_template, make_response, url_for, request, g
from app.app import app

@app.route('/')
def index():
    cookies = { 'darkMode': request.cookies.getlist('darkMode') }
    resp = make_response(render_template('index.html'))
    if not cookies['darkMode']:
        resp.status_code = 200
        resp.set_cookie('darkMode', '1', 60*60)
    return resp

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/peculiarities')
def peculiarities():
    return render_template('peculiarity.html')

@app.route('/news')
def news():
    return render_template('news.html')