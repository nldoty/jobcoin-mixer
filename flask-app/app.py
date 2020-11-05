from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from jobcoin import api, logic
import uuid
app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/api/get_address', methods=['POST'])
@cross_origin(supports_credentials=True)
def get_mixer_address():
    # Allows the user
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


@app.route('/api/mix_coins/<uuid>', methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def check_mixer_address(uuid):
    if request.method == 'GET':
        balance = str(api.check_balance(uuid))
        print("BALANCE: " + str(balance))
        # Let the front end know
        return jsonify({
            'balance': balance
        })

    if request.method == 'POST':

        body = request.get_json()

        addresses = body['addresses']
        transactions = body['transactions'] if body['transactions'] else None
        timeout = body['timeout'] if body['timeout'] else None

        transactions_list = logic.mix_coins(addresses, uuid, timeout, transactions, False)
        body = logic.convert_transactions_list_to_json(transactions_list)

        logic.make_transactions(transactions_list)

        return jsonify(body), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
