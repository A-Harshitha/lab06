from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import re

app = Flask(__name__)
app.secret_key = 'harshitha'

def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

class User:
    @staticmethod
    def add_user(username, password):
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))
            conn.commit()
            return cursor.lastrowid

def password_check(password):
    errors = []
    if len(password) < 8:
        errors.append("Password should be at least 8 characters long.")
    if not re.search("[a-z]", password):
        errors.append("Password must contain a lowercase letter.")
    if not re.search("[A-Z]", password):
        errors.append("Password must contain an uppercase letter.")
    if not password[-1].isdigit():
        errors.append("Password must end with a number.")
    return errors

@app.route('/')
def index():
    session['failed_attempts'] = session.get('failed_attempts', 0)
    return render_template('index.html')

@app.route('/report', methods=['POST'])
def report():
    username = request.form['username']
    password = request.form['password']
    errors = password_check(password)
    if not errors:
        user_id = User.add_user(username, password)
        session['failed_attempts'] = 0
        return render_template('report.html', passed=True)
    else:
        session['failed_attempts'] = session.get('failed_attempts', 0) + 1
        if session['failed_attempts'] == 3:
            flash('Warning: 3 consecutive failed attempts!')
        elif session['failed_attempts'] >= 3:
            flash('Warning: More than 3 consecutive failed attempts!')
        
        for error in errors:
            flash(error)
        return redirect(url_for('index', username=username))

@app.route('/index')
def index_with_username():
    username = request.args.get('username', '')
    session['failed_attempts'] = session.get('failed_attempts', 0)
    return render_template('index.html', username=username)

@app.route('/view_users')
def view_users():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, username FROM users')
        users = cursor.fetchall()
    return render_template('view_users.html', users=users)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
