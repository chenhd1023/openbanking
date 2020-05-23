import flask
from flask import jsonify, request, Response, render_template, redirect
import csv
import datetime
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/test/oauth', methods=['GET'])
def test_oauth():
    content = {
        "bank": "700",
        "redirect_link": "https://api.obtest.org.tw/700/oauth/authentication",
    }
    response = Response(content, status=200, mimetype='application/json')
    write_log(request, response)
    return response


@app.route('/oauth/authentication', methods=['POST'])
def oauth_authentication():
    response = render_template('login.html')
    write_log(request, 'login.html')
    return response


@app.route('/identity/queryAPI', methods=['GET'])
def identity_queryAPI():
    if request.args.get('code') == 'QDPsc0':
        response = render_template('QueryAPI.html')
        write_log(request, 'QueryAPI.html')
        return response
    else:
        response = redirect(
            "http://127.0.0.1:5000/identity/queryAPI?code=QDPsc0")
        write_log(request, "http://127.0.0.1:5000/identity/queryAPI?code=QDPsc0")
        return response


@app.route('/oauth/token', methods=['POST'])
def oauth_token():
    content = {
        "access_token": "(string)",
        "token_type": "bearer",
        "refresh_token": "(string)",
        "expires_in": "43199",
        "scope": "select",
        "jti": "(string)"
    }
    response = Response(content, status=200, mimetype='application/json')
    write_log(request, response)
    return response


@app.route('/user/testdata', methods=['GET'])
def user_testdata():
    content = {
        "MSG": "GET data OK"
    }
    response = Response(content, status=200, mimetype='application/json')
    write_log(request, response)
    return response


app.run()

def write_log(request, response):
    with open('log.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.datetime.now(), request, response])
