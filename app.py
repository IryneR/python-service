from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


#@app.route('/hash', methods=['GET'])
#def api_hash():
    #hash for string
 #       return jsonify({'hash': hash('thedarkdog.attlasian.net')})

@app.route('/hash', methods=['GET', 'POST'])
def api_hash():
    #content = request.get_json(silent=True)
    #print content
    #return jsonify(request.json)
    #content = request.json
    content = request.json
    print(content)

    #res = json.loads(content)
    #print(res)
    #print(request.json()[0]['projectKey'])
    return jsonify({'hash': hash('thedarkdog.attlasian.net')})


app.run()
