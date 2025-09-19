Dieses Projekt wurde im Rahmen des Kurses **Full-Stack Web Development** an der HWR Berlin erstellt!

# Rate BNB
Rate bnb ist eine App, die dafür erstellt wurde den Buchungsprozess für eure Ferien Wohnung spielerisch zu gestalten.

# How to get the Code running
Klonen unseres Repositorys
```bash
git clone https://github.com/pajolinho/RateBnB.git
```

virtuelles Environment erstellen
```bash
python -m venv venv
```

nun muss es aktiviert werden
```bash
source venv\bin\activate
```

installation des requirement.txt
```bash
pip install -r requirements.txt
```

create the database table
```bash
python app.py
```

da die Datenbank noch mit einträgen gefüllt werden muss 
ctl + c in das Terminal eingeben

datenbank mit Airbnbs füllen
```bash
python data_to_db.py
```
beginne App
```bash
flask run
```

kopieren nun die erscheinende Adresse in deinen Browser

Viel Spaß dein zukünftiges Airbnb zu finden 

# GitHub Pages:
Das ist der Link: https://pajolinho.github.io/RateBnB/
