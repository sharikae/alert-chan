from flask import Flask
from flask import request
from serial import arduino_1

app = Flask(__name__)


class Message(object):
    """Slackのメッセージクラス"""
    token = ""
    team_id = ""
    channel_id = ""  # 投稿されたチャンネルID
    channel_name = ""  # チャンネル名
    timestamp = 0
    user_id = ""
    user_name = ""  # 投稿ユーザー名
    text = ""  # 投稿内容
    trigger_word = ""  # OutgoingWebhooksに設定したトリガー

    def __init__(self, params):
        self.team_id = params["team_id"]
        self.channel_id = params["channel_id"]
        self.channel_name = params["channel_name"]
        self.timestamp = params["timestamp"]
        self.user_id = params["user_id"]
        self.user_name = params["user_name"]
        self.text = params["text"]
        self.trigger_word = params["trigger_word"]

    def __str__(self):
        res = self.__class__.__name__
        res += "@{0.token}[channel={0.channel_name}, user={0.user_name}, text={0.text}]".format(self)
        return res


@app.route("/api/v1/get_request", methods=['POST'])
def webhook():
    msg = Message(request.form)
    arduino_1()
    print(msg)
    print("body: %s" % request.data)

    return request.data

if __name__ == "__main__":
    app.run("127.0.0.1", 1234)
