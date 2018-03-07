from cgitb import enable
enable()
from cgi import FieldStorage, escape
from hashlib import sha256
from time import time
from shelve import open
from http.cookies import SimpleCookie
import pymysql as db
form_data = FieldStorage()
username=""
result=""
formempty="""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>eNote</title>
        <meta charset="UTF-8">  
        <meta name="viewport" content="width=device-width, initial-scale=1.0" >
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black"> 
    </head>
    <body>
    </section>
        <div id="1" class="container">
        <div id="3">
    
        <form method="post" action="">
            <input type="hidden" name="action" value="login">
            <input type="hidden" name="hide" value="">
        </div>
        <table class='center'>
                <tr>
                    <td></td><td><input type="text" name="email" class="input" placeholder="Email"></td>
                </tr>
                <tr>
                    <td></td><td><input type="password" name="password" class="input" placeholder="Password"></td>
                </tr>
                <tr>
                    <td></td><td><input type="submit" value="submit"></td>
                </tr> 
                <p id=registered><a href="register.py">Click here to register!</a></p>
        </table>
        </form>
        </div>
        %s
        </body>
        </html>
"""
# If data is entered to form
if len(form_data) != 0:
    # Input sanitization
    email = escape(form_data.getfirst('email', '').strip())
    password = escape(form_data.getfirst('password', '').strip())
    # If something isn't filled in
    if not email or not password:
        result = '<p id="result">Error: email and password are required</p>'
    else:
        # Hash password given
        sha256_password = sha256(password.encode()).hexdigest()
        try:
            # Connect to DB
            connection = db.connect('cs1.ucc.ie', 'jp11', 'rahquahv', '2019_jp11')
            cursor = connection.cursor(db.cursors.DictCursor)
            # Find user with valid password, and the same email
            cursor.execute("""SELECT * FROM Users 
                              WHERE PlayerName = %s
                              AND PassHash = %s""", (email, sha256_password))
            if cursor.rowcount == 0:
                result = '<p id="result">Error: Login incorrect</p>'
            else:
                # Load cookie, and log the user in by setting the authenticated value to true
                cookie = SimpleCookie()
                sid = sha256(repr(time()).encode()).hexdigest()
                cookie['sid'] = sid
                session_store = open('sess_' + sid, writeback=True)
                session_store['authenticated'] = True
                session_store['email'] = email
                session_store.close()
                cursor.close()  
                connection.close()
                print(cookie)
        except (db.Error, IOError):
            result = '<p id="result">Sorry! We are experiencing problems at the moment. Please call back later.</p>'
print("Content-Type: text/html")
print()
print(formempty %(result))
