import random
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# #prototype
# bnbs = [
#     {"id": 1, "title": "Berlin Studio", "city": "Berlin", "price": 120},
#     {"id": 2, "title": "Warschau Flat", "city": "Warschau", "price": 90}
# ]

app = Flask(__name__)
# DAtenbank Konfi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Bnb (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(600), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=True)
    price_per_night = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String, nullable=False)


# Noch in Bearbeitung!!!
# class User (db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # firstname = db.Column(db.String(250), nullable=False)
    # name = db.Column(db.String(250), nullable=False)
    # 

# class Favs (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db(Integer, nullable=Flase)
#     bnb_id = db.(Integer, nullable=False)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/login")

@app.route("/aboutus", methods=["GET"])
def aboutus():
    return render_template("aboutus.html")

# [Q3]
@app.route("/game", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        score = int(request.form.get("score", 0))
        expected = request.form.get("expected")
        user = request.form.get("answer")

        #Q5 
        id1 = int(request.form.get("id1"))
        id2 = int(request.form.get("id2"))
        bnb1 = Bnb.query.get(id1)
        bnb2 = Bnb.query.get(id2)
        
        if user == expected:
            score += 1
            return render_template("game_over.html", final_score=score, listing1=bnb1, listing2=bnb2, correct=True)
        else:
            return render_template("game_over.html", final_score=score, listing1=bnb1, listing2=bnb2, correct=False)
    if request.method == "GET":
        score = int(request.args.get("score", 0))
        # bnb_list = Bnb.query.all()
        # bnb1, bnb2 = random.sample(bnb_list, 2)
        bnb1, bnb2 = random.sample(Bnb.query.all(), 2)
        if bnb1.price_per_night > bnb2.price_per_night:
            expected = "oneExpensive"
        else:
            expected = "twoExpensive"

        return render_template("game.html", score=score, listing1=bnb1, listing2=bnb2, expected=expected)

if __name__ == "__main__":     
    #Datenbank speichern falls im app context ausgeführt wird
    with app.app_context():
        db.create_all()
    app.run(debug=True)