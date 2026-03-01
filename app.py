from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def verify():
    # كلمة السر لربط البوت بفيسبوك
    if request.args.get("hub.verify_token") == "my_secret_password":
        return request.args.get("hub.challenge")
    return "Hello World"

@app.route("/", methods=['POST'])
def webhook():
    return "ok", 200

if __name__ == "__main__":
    app.run()
