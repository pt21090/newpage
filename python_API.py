from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)
# LINE 聊天機器人的基本資料
#聊天機器人的 Chennel access token
line_bot_api = LineBotApi('CCxxp2eejx8Ov1aZFA1l8ExjIu8p3JKQgAFZxXW4NsV+qDzYIWANU9HII9rNpjEXGBIz1+g1+3fwkfty9npA/SlUwmq70HWTh41NCb5x2Vb/9km2vOlRqUrTswn7oD2/xtiMsI/Tlooxfu3sSakNwAdB04t89/1O/w1cDnyilFU=')
#聊天機器人的 Channel secret
handler = WebhookHandler('012eb4ff708b52457f34dd3dec8b40b7')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

if __name__ == "__main__":
    app.run()