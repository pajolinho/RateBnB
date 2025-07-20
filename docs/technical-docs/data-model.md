---
title: Data Model
parent: Technical Docs
nav_order: 2
---

{: .label }
[Merdan Alkas]

{: .no_toc }
# Data model

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Datenbank

### Bnb Table

Hier werden die listings gespeichert für das Spiel.

| **Feld**        | **Typ**  | **Beschreibung**                          |
|-----------------|----------|-------------------------------------------|
| `ID`            | Integer  | Primärschlüssel, automatisch generiert     |
| `Image_url`     | String   | Pflichtfeld, Link zum Bild                 |
| `Title`         | String   | Pflichtfeld, Airbnb-Titel                  |
| `Location`      | String   | Pflichtfeld, Ort                           |
| `Beds`          | Integer  | Pflichtfeld, Anzahl der Betten im Airbnb   |
| `Rooms`         | Integer  | Pflichtfeld, Anzahl der Zimmer             |
| `Price_per_night` | Integer | Pflichtfeld, Preis pro Nacht               |
| `Link`          | String   | Pflichtfeld, Link zur Airbnb-Seite         |

### User Table

Hier werden die Nutzer angelegt 

| **Feld**   | **Typ**  | **Beschreibung**                        |
|------------|----------|------------------------------------------|
| `ID`       | Integer  | Primärschlüssel, automatisch generiert    |
| `Username` | String   | Pflichtfeld, eindeutiger Nutzername       |
| `Password` | String   | Pflichtfeld, Passwort zum Anmelden        |


### Favs Table

Hier werden die Favoriten gespeichert angelegt 

| **Feld**  | **Typ**  | **Beschreibung**                          |
|-----------|----------|--------------------------------------------|
| `ID`      | Integer  | Primärschlüssel, automatisch generiert      |
| `User_id` | Integer  | Pflichtfeld, Fremdschlüssel, Bezug auf User |
| `BNB_id`  | Integer  | Pflichtfeld, Fremdschlüssel, Bezug auf BNB  |

