from flask import Blueprint, render_template , request, redirect, url_for
dashboard = Blueprint('dashboard', __name__, template_folder='template', static_folder='template/static')

@dashboard.route('/')
def dashboardd():
    return render_template("dashboard.html")