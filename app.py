from flask import Flask, jsonify, request

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
    return jsonify(request.json)
    #content = request.json
    #print content
#hash for issue object
      #return jsonify({'hash': hash('thedarkdog.attlasian.net')})


app.run()
