from flask import Blueprint, render_template, redirect, url_for, session
logout = Blueprint('logout', __name__, template_folder='template', static_folder='template/static')
from login import *


@logout.route('/logout', methods=['GET', 'POST']) 
def logout2(): 
    if 'Login' in session: 
        session.pop('Login' ,None) 
    return redirect(url_for('login.log'))