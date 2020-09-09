import _hashlib

from flask import Flask, render_template, jsonify, make_response, Response, request, redirect

app = Flask(__name__)
adminkey = "d404559f602eab6fd602ac7680dacbfaadd13630335e951f097af3900e9de176b6db28512f2e000b9d04fba5133e8b1c6e8df59db3a8ab9d60be4b97cc9e81db"


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
    resp: Response = make_response(jsonify({
        "xy": 4,
        "z": "xyz",
        "list": ["xy", "z", "huju", "xy"]
    }))
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    resp.headers["Access-Control-Request-Methods"] = "POST, GET"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    return resp


@app.route("/api/send", methods=["POST", "OPTIONS"])
def send():
    resp: Response = make_response(jsonify(1), 200)
    password = ""
    if request.method == "POST":
        data = request.get_data(as_text=True)
        data = eval(data)
        password = str(data['password'])

    if get_hash(password)==adminkey:
        resp.set_cookie("adminkey", adminkey)
        print("cookie set")
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:4200"
    # resp.headers["Access-Control-Allow-Methods"] = "POST,GET"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.set_cookie("hallo", "Peter")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
