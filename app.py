from flask import Flask, render_template, Blueprint, redirect, url_for, session, make_response
from login import login
from reg import registr
from xss import xss
from lfi import lfi
from sqli import sqli
from sqli import sqli
from logout import logout
from dashboard import dashboard
app=Flask(__name__,template_folder='template', static_folder='template/static/')
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(registr, url_prefix='/reg')
app.register_blueprint(xss, url_prefix='/xss')
app.register_blueprint(lfi, url_prefix='/lfi')
app.register_blueprint(sqli, url_prefix='/sqli')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(logout)
app.config.from_object(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

#comment
@app.route('/')
def main():
    return render_template('main.html')