---
title: Architecture
parent: Technical Docs
nav_order: 1
---

{: .label }
[Paul Grüßing]

{: .no_toc }
# Architecture

{: .attention }
> Diese Seite beschreibt den technischen Aufbau der RateBnb Anwendung. Es soll  neuen Entwicklern helfen sich zurecht zufinden

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Overview
**RateBnB** ist eine Flask basierte WebApp
+ Benutzerregistrierung & Login sind Session basiert
+ Es werden jeweils zwei unterschiedliche Unterkünfte dem Nutzer vorgeschlagen
+ Favoritenliste der Airbnbs je Benutzer

## Codemap
|**Datei**| **Beschreibung**|
|-------------|-----------------------------------------------------|
|app.py| Hauptlogik: enthält alle Routen, Datenbankmodelle und den Spielflow|
|data_to_db.py| Füllt Airbnbs Daten in die Datenbank|
|db.db| Datenbank für Nutzer, Unterkünfte und Favoriten|
|index.html| Startseite mit Spielanleitung und navigations Möglichkeiten|
|game.html|zeigt zwei zufällige Unterkunfte zum Preisraten|
|game_over.html| Bewertet und zeigt das Ergebnis der letzten Spielrunde|
|favorites.html| zeigt gespeicherte Favoriten des jewiligen Nutzers|
|anmelden.html & registrieren.html| Login oder neue Registrierung des aktuellen Nutzers|
|aboutus.html| Vorstellung des Entwicklerteams|


## Cross-cutting concerns

Die Anwendung verwendet Session-basierte Authentifizierung, wobei die **user_id** in der Session gespeichert wird, um eingeloggte Nutzer zu identifizieren. Für die Datenpersistenz wird SQLAlchemy eingesetzt, um Python-Klassen mit Datenbanktabellen wie User, Bnb und Favs zu verknüpfen. Die Spiellogik ist direkt in den Flask-Routen implementiert und basiert auf einem Preisvergleich zwischen zwei zufällig ausgewählten Unterkünften. Favoriten werden nutzergebunden gespeichert.
