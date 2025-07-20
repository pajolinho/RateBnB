---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
Merdan Alkas

---
Bilder werden Online leider nicht gelanden. Die Bilder kann man aber über GitHub sehen.

---

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [Section / module]

### `index()`

**Route:** `/`

**Methods:** `GET` `POST`

**Purpose:** Hauptseite der Anwendung. Hier kann der Nutzer die Anwendung steuern nachdem er sich angemeldet hat. Nutzer wird mit Nutzernamen angesprochen und kann das Spiel starten und auf die Überunsseite und auf die eigenen Favoriten soweit. 


**Index output:**
![Bild Index / Seite](/docs/images/bild1.png)

---


### `registrieren()`

**Route:** `/registrieren`

**Methods:** `GET` `POST`

**Purpose:** Falls der Nutzter noch kein Account hat kann er sich hier einen anlegen. Der Benutzername und das Passwort können beliebig ausgewählt werdene es gelten keine Bestimmungen, außer dass der Benutzername nicht vorher vergeben sein darf. Falls der Nutzter bereits ein Account hat kann er über den Link "zum Login" auf die Login seite wechseln!

**Registrieren output:**

![registrieren() sample](/docs/images/registrieren.png)

---

### `anmelden()`

**Route:** `/anmelden>`

**Methods:** `GET` `POST`

**Purpose:** Hier kann der Nutzter sich anmelden falls er bereits einen Account hat. Falls er kein Account hat kann er über den Link "Noch kein Account?" sich ein Account anlegen. Wenn der Nutzter sich angemeldet hat kommt er auf die /index Seite.

**anmelden output:**

![anmelden()](/docs/images/anmelden.png)

---


### `logout()`

**Route:** `/logout`

**Purpose:** Über diesen Pfad kann der Nutzter sich abmelden und kommt wieder auf die Anmeldenseite zurück. Dieser Pfad wurde als Button auf der Spiel und Index implementiert.

---

### `aboutus()`

**Route:** `/aboutus`

**Methods:** `GET`

**Purpose:** Hier kann der Nutzter etwas über die App Entwickler lesen. 

**Über Uns output:**

![aboutus()](/docs/images/aboutus.png)

---

### `favoritelist()`

**Route:** `/favoritelist`

**Purpose:** Hier werden die im Spielverlauf als Favoriten gespeicherten AriBnbs angezeigt mit Preis Info und direktem Link auf die AirBnb seite um das gepspeicherte AirBnb sehen zu können.

**Favoriten output:**
![favoritelist()](/docs/images/favoriten.png)

---


### `start()`

**Route:** `/game`

**Methods:** `GET` `POST`

**Purpose:** Hier kann der Nutzter das Spiel spielen. Es werden zwei AirBnb mit Titel, Bild, Anzahl der Betten & Anzahl der Zimmer angezeigt. Der Nutzter kann anhand dieser Informationen auswählen welches AirBnb nach seiner Meinung mehr als das andere Kostet. Außerdem kann der Nutzter sich das AirBnb auch auf die Favoritenliste packen.

**Start output:**

![start()](/docs/images/start_game.png)

---

### `add_favorite(bnb_id)`

**Route:** `/add_favorite`

**Methods:** `POST`

**Purpose:** Diese Route ist dafür da um die Listings in die Favoritenliste einzuspeichern falls noch nicht gespeichert ist.

---

### `get_favs()`

**Route:** `/api/Favs`

**Methods:** `GET` 

**Purpose:** Diese Route stellt eine Headless JSON Datei für die gepseicherten Favoriten zu verfügung. 

**Start output:**

![get_favs()](/docs/images/JSON.png)