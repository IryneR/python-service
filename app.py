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
    return jsonify({'hash': hash('thedarkdog.attlasian.net')})
    #print content
#hash for issue object
      #return jsonify({'hash': hash('thedarkdog.attlasian.net')})
    res = json.loads(content)

#обработка случая, когда послан не json

app.run()
