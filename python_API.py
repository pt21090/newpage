import os
from flask import Flask, abort, request
# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
line_bot_api = LineBotApi(os.environ.get("CCxxp2eejx8Ov1aZFA1l8ExjIu8p3JKQgAFZxXW4NsV+qDzYIWANU9HII9rNpjEXGBIz1+g1+3fwkfty9npA/SlUwmq70HWTh41NCb5x2Vb/9km2vOlRqUrTswn7oD2/xtiMsI/Tlooxfu3sSakNwAdB04t89/1O/w1cDnyilFU="))
handler = WebhookHandler(os.environ.get("012eb4ff708b52457f34dd3dec8b40b7"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
