#!/usr/bin/env python3

import os, json, cgi
import templates, secret

# FROM https://python.readthedocs.io/en/latest/library/cgi.html
import cgitb
cgitb.enable()

# FROM https://www.tutorialspoint.com/python/python_cgi_programming.htm
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

if username == secret.username:
    if password == secret.password:
        print("Set-Cookie:loggies=yes")

print('Content-Type: text/html')
print()
print("""<!doctype html>
    <html>
    <body>
    """)

cookies = os.environ['HTTP_COOKIE'].split(";")
for cookie in cookies:
    key, value = cookie.split("=")

    if key == "loggies" and value == "yes":
        print(templates.secret_page(username, password))
    # else:
    #     print(templates.after_login_incorrect())

print("""
    </body>
    </html>
    """)