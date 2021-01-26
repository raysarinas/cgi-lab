#!/usr/bin/env python3

import os, json, cgi

# serve the envt back as JSON
# print('Content-Type: application/json') # type of file being sent
# print()
# print(json.dumps(dict(os.environ), indent=2))

# Modified FROM: Lab Presentation 2021-01-25 by Hazel Campbell
print('Content-Type: text/html')
print()
print("""
<!doctype html>
<html>
<body>
<h1>HELLO LAB 3</h1>""")

# report the values of the query parameters in the HTML
# print(f"<p> QUERY_STRING = {os.environ['QUERY_STRING']} </p>")
# print("<p>QUERY_STRING Parameters:</p>")
# print("<ul>")
# for parameter in os.environ['QUERY_STRING'].split('&'):
#     (name, value) = parameter.split('=')
#     print(f"<li><em>{name}</em> = {value}</li>")
# print("""
# </ul>
# """)

# report browser
# print(f"<p> HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']} </p>")

# login form
print("""
    <h1> Welcome! </h1>

    <form method="POST"">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

print("""
</body>
</html>
""")

# FROM https://www.tutorialspoint.com/python/python_cgi_programming.htm
form = cgi.FieldStorage()

username = form.getvalue('username')
password = form.getvalue('password')

print("<ul>")
print(f"<li><em>username:</em> {username}</li>")
print(f"<li><em>password:</em> {password}</li>")
print("</ul>")