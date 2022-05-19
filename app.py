from ax_12.movement import *
from flask import Flask, jsonify, redirect, render_template, request


app = Flask(__name__)

# Initialize servos
servos = connectServos()


@app.get("/test")
def test():
    return jsonify({"msg": "TEST WORKING"})


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/move", methods=["POST", "GET"])
def move():
    command = request.form.get('command', "stand")
    print("RECEIVED COMMAND:", command)

    commands = {"sit": sit, "stand": stand,
                "spin-ccw": lambda servos: rotate(servos, "CCW"), "spin-cw": rotate, "flip": flip, "walk": walk}

    commands[command](servos)

    return redirect("/")


if __name__ == "__main__":
    # host parameter to make it available in LAN
    app.run(host="0.0.0.0")
