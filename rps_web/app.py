from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)
# DB 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)

db = SQLAlchemy(app)


class ScoreBoard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String(50), nullable=False)
    computer_choice = db.Column(db.String(50), nullable=False)
    result = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"사용자: {self.user_choice}, 컴퓨터: {self.computer_choice} 당신은 {self.result}."


with app.app_context():
    db.create_all()


def judgment(computer, user):
    if (
        (computer == "가위" and user == "보")
        or (computer == "바위" and user == "가위")
        or (computer == "보" and user == "바위")
    ):
        return "졌습니다"
    elif computer == user:
        return "비겼습니다"
    else:
        return "이겼습니다"


@app.route("/")
def home():
    score_list = ScoreBoard.query.all()
    prev_result = ScoreBoard.query.order_by(ScoreBoard.id.desc()).limit(1)
    win = len(ScoreBoard.query.filter_by(result="이겼습니다").all())
    lose = len(ScoreBoard.query.filter_by(result="졌습니다").all())
    draw = len(ScoreBoard.query.filter_by(result="비겼습니다").all())
    print(type(prev_result))

    record = {
        "win": win,
        "lose": lose,
        "draw": draw,
        "prev_result": prev_result,
    }
    
    return render_template("index.html", data=score_list, context=record)


@app.route("/score/")
def new_score():
    # form에서 보낸 데이터 받아오기
    RPS = {"가위": "✌️", "바위": "✊", "보": "🖐️"}

    user_receive = request.args.get("RPS")
    computer_receive = random.choice(list(RPS.keys()))
    result_receive = judgment(computer_receive, user_receive)

    # 데이터를 DB에 저장하기
    song = ScoreBoard(
        user_choice=RPS[user_receive],
        computer_choice=RPS[computer_receive],
        result=result_receive,
    )
    db.session.add(song)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
