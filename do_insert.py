from alertchan.database import init_db
from alertchan.database import db_session
from alertchan.models import ConfigData

# idには連番。title、textを指定。dateは日時が勝手に入る(model.pyのデフォルト設定により)
c1 = ConfigData("Do Not Distarb", "checked", "donotdistarb", "on")  # カラム1:'Flask' カラム2:'micro framework'を指定してインスタンス作成
db_session.add(c1)                            # insert実行
db_session.commit()                           # commit実行
c2 = ConfigData("Slack Notification", "checked", "runmode", "home")        # 以下同上
c3 = ConfigData("Twitter Notification", "", "aaa", "on")
db_session.add(c2)
db_session.add(c3)
db_session.commit()