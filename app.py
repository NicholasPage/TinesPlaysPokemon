#!flask/bin/python
"""Now let's build a JSON from s3. Did someone say stateful?"""
import random
import json
import subprocess

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

allowed_keys = ["A","B","Space","Up","Down","Left","Right"]

WID = subprocess.run(["xdotool", "search", "--class", "retroarch"], capture_output=True)

WID = str(WID.stdout)

WID = WID.split("'")

WID = WID[1]

WID = WID.split('\\')

WID = WID[0]

@app.route('/TPP/api/v1.0/command', methods=['POST'])
def Input_Command():
    """"build the input for xdotool"""
    subprocess.run(["xdotool", "windowfocus", WID])
    subprocess.run(["xdotool", "key", request.json.get('input', "")])
    return jsonify(request.json.get('input', "")), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
