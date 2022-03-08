import json
from flask import Flask, request, render_template, abort, jsonify
from Carpark import Carpark
from Vehicle import Vehicle

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    cp = Carpark(15)
    return render_template("index.html", cars=cp.spaces, capacity=cp.capacity, spaces=cp.capacity-len(cp.spaces))


@app.route("/add", methods=["POST"])
def add():
    cp = Carpark(15)
    reg = request.form["reg"]
    kind = request.form["type"]
    veh = Vehicle(reg, kind)
    if not cp.add_car(veh):
        abort(400)
    else:
        cp.save_to_file()
        return json.dumps(veh.__dict__)

@app.route("/remove", methods=["POST"])
def remove():
    cp = Carpark(15)
    reg = request.form["reg"]
    if not cp.remove_car(reg):
        abort(404)
        return "error"
    cp.save_to_file()
    return json.dumps(cp.spaces, default=obj_dict)

def obj_dict(obj):
    return obj.__dict__

if __name__ == "__main__":
    app.run(debug=True)