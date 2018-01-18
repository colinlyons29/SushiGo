from cgitb import enable 
enable()
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
import subprocess
form_data = FieldStorage()
username = ''
result = ''
if len(form_data) != 0:
    email1 = escape(form_data.getfirst('email1', '').strip())
    email2 = escape(form_data.getfirst('email2', '').strip())
    username = escape(form_data.getfirst('username', '').strip())
    password1 = escape(form_data.getfirst('password1', '').strip())
    password2 = escape(form_data.getfirst('password2', '').strip())
    if not username or not password1 or not password2 or not email1 or not email2:
        result = '<p id="result">***Error: Email address, Username, and Password fields are required***</p>'
    elif password1 != password2:
        result = '<p id="result">***Error: Password fields must be equal***</p>'
    elif email1 != email2:
        result = '<p id="result">***Error: Email fields must be equal***</p>'
    elif "@" not in email1 or "@" not in email2 or "." not in email1 or "." not in email2:
        result = """<p id="result">***Error: use a valid email address***</p>"""
    else:
        try:
            connection = db.connect('cs1dev.ucc.ie', 'cdl1', 'aipahxoh', '2019_cdl1')
            cursor = connection.cursor(db.cursors.DictCursor)
            # Todo: Set up tables
            cursor.execute("""SELECT * FROM users WHERE username = %s""", (username))
            if cursor.rowcount > 0:
                result = '<p id="result">***Error: user name already taken***</p>'
            cursor.execute("""SELECT * FROM users WHERE email = %s""", (email1))
            if cursor.rowcount > 0:
                result = '<p id="result">***Error: email address already in use***</p>'
            else:
                sha256_password = sha256(password1.encode()).hexdigest()
                cursor.execute("""INSERT INTO users (username, email, user_password) VALUES (%s, %s, %s)""", (username, email1, sha256_password))
                connection.commit()
                cursor.close()  
                connection.close()
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('SessionID_' + sid, writeback=True)
                session_store['Authenticated'] = True
                session_store['username'] = username
                session_store.close()
                result = """
                   <p class="success">Succesfully inserted! <br> Thank you for registering!</p>
                   """
                print(cookie)
        except (db.Error, IOError):
            result = '<p id="result"Error connection to database</p>'
print('Content-Type: text/html')
print()
print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Register</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" >
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black"> 
        %s
    </head>
        <body>
            <form action="register.py" method="post">
            <br>
                <label for="username"><span>User name: </span></label>
                <input type="text" name="username" id="username" value="%s"><br>
                <label for="email1"><span>Email: </span></label>
                <input type="text" name="email1" id="email1"><br>
                <label for="username"><span>Confirm email: </span></label>
                <input type="text" name="email2" id="email2"><br>
                <label for="password1"><span>Password: </span></label>
                <input type="password" name="password1" id="password1"><br>
                <label for="passwords2"><span>Re-enter password: </span></label>
                <input type="password" name="password2" id="password2"><br>
                <input type="submit" value="Register">
            </form>
            %s
        </body>
    </html>""" % (redirect ,username, result))
