import random
from flask import Flask, render_template, request, redirect, url_for

#prototype
bnbs = [
    {"id": 1, "title": "Berlin Studio", "city": "Berlin", "price": 120},
    {"id": 2, "title": "Warschau Flat", "city": "Warschau", "price": 90}
]

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        score = int(request.form.get("score", 0))
        expected = request.form.get("expected")
        user = request.form.get("answer")

        if user == expected:
            score += 1
            return redirect(url_for("index", score=score))
        else:
            return render_template("game_over.html", final_score=score)
    if request.method == "GET":
        score = int(request.args.get("score", 0))
        bnb1, bnb2 = random.sample(bnbs, 2)
        if bnb1["price"] > bnb2["price"]:
            expected = "oneExpensive"
        else:
            expected = "twoExpensive"

        return render_template("index.html", score=score, listing1=bnb1, listing2=bnb2, expected=expected)
if __name__ == "__main__":
    app.run(debug=True)
