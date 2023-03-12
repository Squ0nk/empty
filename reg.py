from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
registr  = Blueprint('registr', __name__, template_folder='template', static_folder='template/static')

@registr.route('/', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('Password')
        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        sql_check_duplicate = cursor_db.execute(('''SELECT password FROM Passwords WHERE login ='{}';''').format(login)).fetchall()
        if  len(sql_check_duplicate) == 1:
            return render_template("reg.html")
        sql_insert = "INSERT INTO passwords VALUES(NULL, '{}','{}');".format(login, password)
        cursor_db.execute(sql_insert)
        db_lp.commit()
        cursor_db.close()
        db_lp.close()
        return redirect(url_for('login.log'))   
    return render_template('reg.html')
