#!flask/bin/python
"""API wrapper for XDOtool"""
import json
import subprocess
import time

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

allowed_keys = ["A","B","C","Up","Down","Left","Right"]

WID = xdotool.xdo_find("retroarch")

@app.route('/TPP/api/v1/command', methods=['POST'])
def Input_Command():
    """"build the input for xdotool"""
    if (request.json.get('input', "") in allowed_keys):
        xdotool.xdo_get(WID)
        time.sleep(0.2)
        xdotool.xdo_key(request.json.get('input', ""))
        time.sleep(0.2)
        return jsonify(request.json.get('input', "")), 200
    else:
        return jsonify('Unapproved Key Attempt'), 400
if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')
