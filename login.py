from flask import Blueprint, render_template , request, redirect, url_for
import sqlite3
from dashboard import dashboardd
login = Blueprint('login', __name__, template_folder='template', static_folder='template/static')

@login.route('/login', methods=['GET', 'POST'])
def log():
     if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('Password')
        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute (('''SELECT password FROM Passwords WHERE login ='{}';''').format(login))
        pas = cursor_db.fetchone()
        data = cursor_db.execute (('''SELECT password FROM Passwords WHERE login ='{}';''').format(login)).fetchall()
        # data = cursor_db.execute (('''SELECT password FROM Passwords WHERE password ='{}';''').format(login)).fetchall()
        db_lp.commit()
        if not data:
            return "Пользователь не найден, зарегистрируйтесь"
        db_lp.commit()
        if data[0][0]!=password:
            return render_template('auth.html')
        db_lp.close()
        return render_template('dashboard.html')
     return render_template('auth.html')
