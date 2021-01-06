from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route('/hash', methods=['GET'])
def api_hash():
    #hash for string
        return jsonify({'hash': hash('thedarkdog.attlasian.net')})


app.run()

# if __name__ == "__main__":
#   app.run(host='0.0.0.0')
