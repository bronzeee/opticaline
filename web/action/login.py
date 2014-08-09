import pymysql

__author__ = 'xu'
from flask import request, url_for, redirect, session
from web import app


@app.route('/login', methods=['POST'])
def do_login():
    username, password = request.form['username'], request.form['password']
    conn = pymysql.connect(host='121.40.88.181', user='root', passwd='bronze', database='opticaline',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute(
        'SELECT ID, NAME, USER_NAME FROM USER WHERE PASSWORD = %s AND (USER_NAME = %s OR ID = %s OR E_MAIL = %s)',
        [password, username, username, username])
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user is not None:
        session['user'] = user
        return redirect(url_for('index'))
    else:
        return "not"


@app.route('/login', methods=['GET'])
def view_login():
    print(request)
    return "login"


@app.route('/logout')
def do_logout():
    session.pop('user', None)
    return redirect(url_for('index'))

