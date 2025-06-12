import random
from flask import Flask, render_template, request, redirect, url_for

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
            final = score
            return render_template("game_over.html", final_score=final)
    if request.method == "GET":
        score = int(request.args.get("score", 0))
        expected = random.choice(["richtig", "falsch"])
        return render_template("index.html", score=score, expected=expected)
if __name__ == "__main__":
    app.run(debug=True)
