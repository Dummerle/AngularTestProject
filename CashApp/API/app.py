from flask import Flask, render_template, jsonify, make_response, Response, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/api/getData")
def getData():
    resp: Response = make_response(jsonify({
        "xy": 4,
        "z": "xyz",
        "list": ["xy", "z", "huju", "xy"]
    }))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Request-Methods"] = "POST, GET"
    return resp


@app.route("/api/send", methods=["POST", "GET"])
def send():
    print("Hi")
    print(request.method)
    resp:Response = make_response()
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "POST,GET"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers"
    
    return resp


if __name__ == '__main__':
    app.run(debug=True)
