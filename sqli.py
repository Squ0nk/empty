from flask import Blueprint, render_template 
sqli = Blueprint('sqli', __name__, template_folder='template', static_folder='template/static')
@sqli.route("/")
def sqlii():
    return render_template('sqli.html')
