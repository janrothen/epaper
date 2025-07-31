from flask import Flask, request, jsonify
from ledlightstrip_controller import LEDController
from color import Color

app = Flask(__name__)
led = LEDController()

@app.route("/on", methods=["POST"])
def turn_on():
    led.switch_on()
    return jsonify({"status": "on"}), 200

@app.route("/off", methods=["POST"])
def turn_off():
    led.switch_off()
    return jsonify({"status": "off"}), 200

@app.route("/fade", methods=["POST"])
def fade_to_color():
    color_name = request.args.get("color", "white").upper()
    duration = float(request.args.get("duration", 5.0))

    try:
        color = getattr(Color, color_name)
    except AttributeError:
        return jsonify({"error": f"Invalid color '{color_name}'"}), 400

    led.set_color(color, duration)
    return jsonify({"status": "fading", "color": color_name.lower(), "duration": duration}), 200

@app.route("/status", methods=["GET"])
def status():
    return jsonify(led.get_status()), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)