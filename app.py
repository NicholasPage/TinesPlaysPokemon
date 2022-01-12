#!flask/bin/python
"""Now let's build a JSON from s3. Did someone say stateful?"""
import random
import json
import subprocess

from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

allowed_keys = ["A","B","Space","Up","Down","Left","Right"]

WID = subprocess.call(["xdotool", "search", "--class", "retroarch"])
subprocess.call(["xdotool", "windowfocus", WID])

@app.route('/TPP/api/v1.0/command', methods=['POST'])
def Input_Command():
    """"build the input for xdotool"""
  subprocess.call(["xdotool", "key", request.json.get('input', "")])
  return jsonify(request.json.get('input', "")), 201

if __name__ == '__main__':
    app.run(debug=True)
