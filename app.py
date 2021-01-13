import time

from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route('/hash', methods=['GET', 'POST'])
def api_hash():
    content = request.json
    #print(content)

    #use json fild concatenation
    #keyString = content["projectKey"]+content["issueTypeName"]+content["creatorDisplayName"]+content["key"]
    #print(keyString)
    #return jsonify({'hash': hash(keyString)})
    time.sleep(20)
    return jsonify({'hash': hash(str(content))})

  
app.run()
