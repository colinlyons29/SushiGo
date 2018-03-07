from cgitb import enable 
enable()
from os import environ
from shelve import open
from http.cookies import SimpleCookie
print('Content-Type: text/html')
print()
result = ''
try:
    # If no cookie exists, user is already logged out
    cookie = SimpleCookie()
    http_cookie_header = environ.get('HTTP_COOKIE')
    if not http_cookie_header:
        result = '<p>You are already logged out</p>'
    else:
        # Load cookie, and set authenticated value to false
        cookie.load(http_cookie_header)
        if "sid" in cookie:
            sid = cookie['sid'].value
            session_store = open('sess_' + sid, writeback=True)
            session_store['authenticated'] = False
            session_store.close()
            result = """
                <p><span>You are now logged out<span></p>
                """
except IOError:
    result = '<p>Error logging out</p>'

# Redirect user to login page after logging out
print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Notes</title>
            <meta charset="UTF-8">  
            <meta name="viewport" content="width=device-width, initial-scale=1.0" >
            <meta name="apple-mobile-web-app-capable" content="yes">
            <meta name="apple-mobile-web-app-status-bar-style" content="black"> 
            <meta http-equiv="refresh" content="2;url=register.py" />
            <link rel="stylesheet" href="main.css">
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

            %s
        </body>
    </html>""" % (result))
