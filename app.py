from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# DAtenbank Konfi
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#Table erstellen
class Bnb (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(600), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    beds = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=True)
    price_per_night = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String, nullable=False)

@app.route("/")
def index():
    return 'Hallo Welt!'

#ohne "with app.app_context" ist "db.create_all(")" nicht möglich // Name musste auch von "test.py" auf "app.py" geändert werden
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)