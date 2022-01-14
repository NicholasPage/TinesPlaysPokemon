#!flask/bin/python
"""API wrapper for XDOtool"""
import random
import json
import subprocess
import time

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

allowed_keys = ["A","B","C","Up","Down","Left","Right"]

WID = subprocess.run(["xdotool", "search", "--class", "retroarch"], capture_output=True)

WID = str(WID.stdout)

WID = WID.split("'")

WID = WID[1]

WID = WID.split('\\')

WID = WID[0]


@app.route('/TPP/api/v1/command', methods=['POST'])
def Input_Command():
    """"build the input for xdotool"""
    if (request.json.get('input', "") in allowed_keys):
        subprocess.run(["xdotool", "windowfocus", WID])
        time.sleep(0.1)
        subprocess.run(["xdotool", "key", request.json.get('input', "")])
        return jsonify(request.json.get('input', "")), 200
    else:
        return jsonify('Unapproved Key Attempt'), 400
if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')
