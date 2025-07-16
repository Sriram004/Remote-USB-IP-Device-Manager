from flask import Flask, request, jsonify
from usbip_utils import list_devices, attach_device, detach_device

app = Flask(__name__)

@app.route("/devices", methods=["GET"])
def get_devices():
    return jsonify(list_devices())

@app.route("/attach", methods=["POST"])
def attach():
    data = request.get_json()
    return jsonify(attach_device(data["ip"], data["busid"]))

@app.route("/detach", methods=["POST"])
def detach():
    data = request.get_json()
    return jsonify(detach_device(data["port"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
