import _hashlib

from flask import Flask, render_template, jsonify, make_response, Response, request

app = Flask(__name__)
adminkey = "d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db"


def add_headers(resp):
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    resp.headers["Access-Control-Request-Methods"] = "POST, GET"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.headers["Access-Control-Allow-Headers"] = "content-type"
    return resp


def get_hash(text: str):
    return _hashlib.openssl_sha512(text.encode()).hexdigest()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/second')
def second():
    return render_template("index.html")


@app.route("/api/getData")
def getData():
    data = {"lol": [42, 1337]}
    if request.cookies.get("adminkey"):

        resp: Response = make_response(jsonify(data), 200)
        resp = add_headers(resp)
    else:
        resp: Response = make_response(jsonify(None), 401)
        resp = add_headers(resp)
    return resp


@app.route("/api/send", methods=["POST", "OPTIONS"])
def send():

    password = ""
    if request.method == "POST":
        data = request.get_data(as_text=True)
        data = eval(data)
        password = str(data['password'])
        print(request.cookies.get("adminkey"))
        if get_hash(password) == adminkey:
            resp: Response = make_response(jsonify(None), 200)
            resp.set_cookie("adminkey", adminkey)
            print("cookie set und eingelogt")

        elif request.cookies.get("adminkey") == adminkey:
            print("Adminkey gesetzt")
            print(request.cookies.get("adminkey"))
            resp = make_response(jsonify(None), 200)

        else:
            resp = make_response(jsonify(None), 401)
            print("Nicht erlaubt")

        resp = add_headers(resp)
        return resp

    if request.method == "OPTIONS":
        resp = make_response(jsonify(None), 200)
        resp = add_headers(resp)
        return resp


@app.route("/api/check")
def check():
    if request.cookies.get("adminkey") == adminkey:
        print(adminkey)
        resp = make_response(jsonify(None), 200)
    else:
        resp = make_response(jsonify(None), 401)

    resp = add_headers(resp)
    print(resp)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
