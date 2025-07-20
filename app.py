import random
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "blabla"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#[Q6]
class Bnb (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(600), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=True)
    price_per_night = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String, nullable=False)

#[Q6]
class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)

# [Q6]
class Favs (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bnb_id = db.Column(db.Integer, db.ForeignKey('bnb.id'), nullable=False)


@app.route("/", methods=["GET", "POST"])
def index():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.get(user_id)
        return render_template("index.html", user=user)
    else:
        return redirect(url_for("anmelden"))

# [Q7] + [Q8]
@app.route("/registrieren", methods=["GET", "POST"])
def registrieren():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            return "Username ist bereits vergeben! "

        anmelder = User(username=username, password=password)
        db.session.add(anmelder)
        db.session.commit()

        return redirect(url_for("anmelden"))

    return render_template("registrieren.html")

# [Q7] + [Q8]
@app.route("/anmelden", methods=["GET", "POST"])
def anmelden():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user_id"] = user.id
            return redirect(url_for("index"))
        else:
            return "Username oder Passwort flasch"

    return render_template("anmelden.html")

# [Q7] + [Q8]
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("anmelden"))


@app.route("/aboutus", methods=["GET"])
def aboutus():
    return render_template("aboutus.html")


@app.route("/favoritelist")
def favoritelist():
    user_id = session.get("user_id")
    favorites = Favs.query.filter_by(user_id=user_id).all()
    favorite_bnb_ids = [fav.bnb_id for fav in favorites]
    favorite_bnb_listings = Bnb.query.filter(Bnb.id.in_(favorite_bnb_ids)).all()
    return render_template("favorites.html", listings=favorite_bnb_listings)

#[Q3] + [Q9]
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
        bnb1, bnb2 = random.sample(Bnb.query.all(), 2)
        if bnb1.price_per_night > bnb2.price_per_night:
            expected = "oneExpensive"
        else:
            expected = "twoExpensive"

        return render_template("game.html", score=score, listing1=bnb1, listing2=bnb2, expected=expected)
    
@app.route("/add_favorite/<int:bnb_id>", methods=["POST"])
def add_favorite(bnb_id):
    user_id = session.get("user_id")
    existing = Favs.query.filter_by(user_id=user_id, bnb_id=bnb_id).first()
    
    if not existing:
        fav = Favs(user_id=user_id, bnb_id=bnb_id)
        db.session.add(fav)
        db.session.commit()

    score = request.form.get("score", 0)
    return redirect(url_for("start", score=score))

# [Q10] [Q11] [Q12]
@app.route("/api/Favs", methods=["GET"])
def get_favs():
    favs = Favs.query.all()
    favs_list = [{
        "id": fav.id,
        "bnb_id": fav.bnb_id,
    }for fav in favs]
    return jsonify(favs_list)


if __name__ == "__main__":     
    with app.app_context():
        db.create_all()
    app.run(debug=True)
