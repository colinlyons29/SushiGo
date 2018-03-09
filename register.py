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
# If data is entered into the form
if len(form_data) != 0:
    # Sanatize inputs
    email1 = escape(form_data.getfirst('email1', '').strip())
    email2 = escape(form_data.getfirst('email2', '').strip())
    username = escape(form_data.getfirst('username', '').strip())
    password1 = escape(form_data.getfirst('password1', '').strip())
    password2 = escape(form_data.getfirst('password2', '').strip())
    # Check all inputs in the form are filled in
    if not username or not password1 or not password2 or not email1 or not email2:
        result = '<p id="result">***Error: Email address, Username, and Password fields are required***</p>'
    # If passwords aren't equal
    elif password1 != password2:
        result = '<p id="result">***Error: Password fields must be equal***</p>'
    # If email's aren't equal
    elif email1 != email2:
        result = '<p id="result">***Error: Email fields must be equal***</p>'
    # If the email entered is not a real address
    elif "@" not in email1 or "@" not in email2 or "." not in email1 or "." not in email2:
        result = """<p id="result">***Error: use a valid email address***</p>"""
    else:
        try:
            # Connect to DB
            connection = db.connect('cs1.ucc.ie', 'jp11', 'rahquahv', '2019_jp11')
            cursor = connection.cursor(db.cursors.DictCursor)
            # Todo: Set up tables
            # Check if user already exists
            cursor.execute("""SELECT * FROM Users WHERE PlayerName = %s""", (username))
            if cursor.rowcount > 0:
                result = '<p id="result">***Error: user name already taken***</p>'
            else:
                # Hash password
                sha256_password = sha256(password1.encode()).hexdigest()
                # Enter the username, email address and the hashed sha256 password into the database
                cursor.execute("""INSERT INTO Users (PlayerName, PassHash) VALUES (%s, %s)""", (username, sha256_password))
                # Commit changes
                connection.commit()
                cursor.close()  
                # Close connection
                connection.close()
                # Create cookie to identify authenticated users
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
# Main page content
print('Content-Type: text/html')
print()
print("""
<!DOCTYPE html>
<html lang="en">
    <head>

        <title>Register</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0" >
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black"> 
        <link rel="stylesheet" href="main.css">
        %s

    </head>
    <body>
        <ul>
            <li><a class="active" href="welcome.html">Home</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="rules.html"How To Play</a></li>
        </ul>
                
        <div class="logo">
                <img src="Images/sushi_go_logo.png">
        </div>
        
        <div class="form">
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
        </div>
        %s
    </body>
</html>""" % (redirect ,username, result))

