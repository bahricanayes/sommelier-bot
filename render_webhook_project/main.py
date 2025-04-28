
from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'bahrican_token'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if verify_token == VERIFY_TOKEN:
            return challenge, 200
        return 'Verify token mismatch', 403
    return 'OK', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
