from flask import Blueprint, render_template 
xss = Blueprint('xss', __name__, template_folder='template', static_folder='template/static')
@xss.route("/", methods=['GET', 'POST'])
def xsss():
    return render_template('xss.html')