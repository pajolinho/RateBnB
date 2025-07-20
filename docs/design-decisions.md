---
title: Design Decisions
nav_order: 3
---

{: .label }
[Paul Grüßing]

{: .no_toc }
# Design decisions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Sprache der Applikation

### Meta
Status
:  **Decided**

### Problem statement
Wir standen vor der Überlegung ob wir unsere Applikation auf deutsch oder englisch schreiben sollten.

### Decision
Wir haben uns für deutsch entschieden, da wir uns auf den europäischen Airbnb Raum fokussiert haben mit unserer App. Außerdem haben wir sie im deutschen Sprachraum entwickelt und möchten daher auch alten Menschen ansprechen die möglicherweise als Minderheit nicht derenglischen Sprache mächtig sind. Diese entscheidung wurde als Team getroffen.


### Regarded options
Englisch oder Deutsch als Sprache 


## 02:  SQLite oder SQLAlchemy 

### Meta

Status
: **Decided**

### Problem statement
Für die anwendung benötigen wir eine relationale Datenbank. Daher die frage ob wir  mit SQL arbeiten oder das SQLAlchemy nutzen.


### Decision
Die Entscheidung ist für SQLALchemy gefallen. Denn damit können wir Datenbankmodelle direkt in Python definieren. Zudem können wir Tabellen als Python Klassen modellieren. Entschieden bei Merdan Alkas
### Regarded options
+ SQLAlchemy lesbarer
+ erlernen neuen Knoq-Hows (Datenbanken als Modul bereits bestanden :)


## 03: Highscores als Liste

### Meta

: **Decided**

### Problem statement
Soll der Nutzer seinen Highscore sehen können?
Wir haben abgewogen zwischen der möglichen Demotivation immer einem Highscore hinterher zu jagen, aber auch der möglichen Motivation die es manchen Nutzern bringt, wenn sie einen Highscore knacken.

### Decision
Wir haben uns dazu entschieden den Highscore wegzulassen. Es wurde sich jedoch für ein Kompromiss entschieden. Seinen Highscore kann man nicht einsehen, allerdings den aktuellen Score. So werden die Leute angesprochen die sich von Highscores motiviert fühlen. Sie können ihren Score von Spiel zu Spiel ungefähr verfolgen. Zudem wird keiner demotiviert wenn sein Highscore niedrig ist. Die Entscheidung wurde von Paul Grüßing getroffen
## Regarded options

| Kriterium | Highscores | einfachen Score |
| --- | --- | --- |
| **Motivation** | ✔️ positiv wenn sich Spieler angesport fühlen | ❌ sinkende Motivation wenn der Highscore nicht geknackt wird |
| **Gamification** | ✔️ Spielgefühl wird intensiver | ❌ Spieler konzentrieren sich mehr auf eigentliche Ziel: Airbnb zu finden 
| **Aufwand** | ❌ Aufwand UI und Usertracking | ✔️ kein Mehraufwand , einfache Umsetzbarkeit |



## 04: JSON 

### Meta

: **Decided**

### Problem statement
Nutzung von JSON im project

### Decision
JSON wird nur verwendet um für die Favoriten Airbnbs 
### Regarded options
+ So kann der Nutzer seine Favoriten liste migrieren falls die App eingestellt wird

## 05: Datenbank 

### Meta

: **Decided**

### Problem statement
Wie sollen die Airbnb in die Datenbank eingepflegt werden

### Decision
Wir haben uns entschieden die Datenbank händisch zu füllen. Dies ermöglicht uns einerseits die volle Kontrolle welche Airbnb dem Nutzer zur Auswahl stehen. So können wir gewährleisten originelle, nicht in Touristen Hotspots bfindliche Unterkünfte vorgeschlagen werden können. Anders als wenn wir mit einem Algorithmus die Airbnbs einpfelgen.Enschieden von Merdan Alkas
### Regarded options
Der ausschlag gebende Punkt war die Skalierbarkeit des Projekts. Da es sich um ein kleines Projekt handelt, war für uns die Händische Pfelge ausreichend. 

## 06: Spielprinzip

### Meta

: **Decided**

### Problem statement
Wie soll das Spiel aufgebaut sein, damit der Spieler nicht überfordert ist, aber trotzdem genug Informationen bekommt um richtig erraten zu können welche Unterkunft teuerer ist.

### Decision
Wir haben das Spiel nach dem KISS (Keep It Simple and Stupid) designed. Damit das Verständnis leicht ist und der neue Spieler nicht erschlagen wird von den optionen
### Regarded options
So haben wir uns dafür entschieden dem Spieler 2 Airbnbs anzuzeigen, bei welchem er das günstigere erraten muss. Er bekommt ein Foto, den Namen des Airbnb und die Anzahl der Zimmer. 
In Test durchläufen der Entwickler war diese Anzahl der Information am sinnvoll um dem Spieler nicht zu viel zu verraten, also den Schwierigkeitsgrad hoch zu halten aber auch nicht zu wenig Informationen zu geben, was die Frustration erhöhen könnte. Wenn das Spiel zu schwer ist.

---
