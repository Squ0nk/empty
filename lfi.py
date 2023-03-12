from flask import Blueprint, render_template, redirect, url_for
lfi = Blueprint('lfi', __name__, template_folder='template', static_folder='template/static')

@lfi.route("/", methods=['GET', 'POST'])
def lfii():
    return render_template('lfi.html')