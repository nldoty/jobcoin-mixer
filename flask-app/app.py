from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS, cross_origin
from jobcoin import api, jobcoin
import uuid
app = Flask(__name__)
api = Blueprint('api', __name__)
CORS(app, support_credentials=True)


@app.route('/mix_coins', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_mixer_address():
    body = request.get_json()
    addresses = body['addresses']

    if len(addresses) != 0:
        generated_address = uuid.uuid4().hex
        response = {
            'deposit_address': generated_address
        }

        return jsonify(response), 200

    else:
        return 400


@app.route('/check_deposit/<uuid>', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def check_mixer_address(uuid):
    if request.method == 'GET':
        balance = int(api.check_balance(uuid))
        # Let the front end know
        return jsonify({
            'balance': balance
        })

    if request.method == 'POST':

        body = request.get_json()

        addresses = body['addresses']
        transactions = body['transactions'] if body['transactions'] else None
        timeout = body['timeout'] if body['timeout'] else None

        transactions_list = jobcoin.mix_coins(addresses, uuid, transactions)
        body = jobcoin.convert_transactions_list_to_json(transactions_list)
        jobcoin.make_transactions(transactions_list)

        return jsonify(body), 200


app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
