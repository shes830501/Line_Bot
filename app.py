#SDK : software development kit

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('MRfyX4zUMIwL/9QE+W5xedXgrrn9FN2BprqBPyCAVU/+SgTo7yTEbKYeIKz4yDsABN17hygLfm3Ql1xwDcCpBN2DFqQy9k9hOG8BvpepPzWAzDHbthfd1+dlF7J4qGMFC6m+J9HhCClPEdDTc9SlRgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('788d014633c17fe38af68bd17f13fbd7')

#有人來這個路徑 這個callback就會被觸發
@app.route("/callback", methods=['POST']) #line公司把訊息轉載進網址，進而觸發function被執行
def callback(): #用瀏覽器發送網址(訊號)過來 
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body #handle function會觸發handler function
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	msg = event.message.text
	r = '抱歉 能再說一次嗎'

	if msg in ['hi', 'Hi']:
		r = 'Hi'
	elif '吃飯' in msg:
		r = '還沒 您呢?'
	elif '誰' in msg:
		r = '我是您的小幫手'
	elif 'who' or 'Who' in msg:
		r = 'I am your assistant'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=''))#使用者傳來的訊息 回傳


if __name__ == "__main__":
    app.run()
#確保這個檔案是直接被執行，而不是被載入