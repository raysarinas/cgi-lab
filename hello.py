#!/usr/bin/env python3

import os, json, templates

# serve the envt back as JSON
def print_json():
    print('Content-Type: application/json') # type of file being sent
    print()
    print(json.dumps(dict(os.environ), indent=2))

# report browser
def report_browser():
    print(f"<p> HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']} </p>")

# Modified FROM: Lab Presentation 2021-01-25 by Hazel Campbell
def main():
    print('Content-Type: text/html')
    print()
    print("""
    <!doctype html>
    <html>
    <body>
    <h1>HELLO LAB 3</h1>""")

    # report the values of the query parameters in the HTML
    # print(f"<p> QUERY_STRING = {os.environ['QUERY_STRING']} </p>")
    print("<p>QUERY_STRING Parameters:</p>")
    print("<ul>")
    for parameter in os.environ['QUERY_STRING'].split('&'):
        (name, value) = parameter.split('=')
        print(f"<li><em>{name}</em> = {value}</li>")
    print("""
    </ul>
    """)

    # report browser
    report_browser()

    print("""
    </body>
    </html>
    """)

main()