---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
Merdan, Paul

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
![Bild Index / Seite](images/bild1.png)

---

## [Example, delete this section] Show to-do lists

### `get_lists()`

**Route:** `/lists/`

**Methods:** `GET`

**Purpose:** Show all to-do lists.

**Sample output:**

![get_lists() sample](../assets/images/fswd-intro_00.png)

---

### `get_list_todos(list_id)`

**Route:** `/lists/<int:list_id>`

**Methods:** `GET`

**Purpose:** Retrieve all to-do items of to-do list with ID `list_id` from database and present to user.

**Sample output:**

![get_list_todos() sample](../assets/images/fswd-intro_02.png)

---

## [Example, delete this section] Insert sample data

### `run_insert_sample()`

**Route:** `/insert/sample`

**Methods:** `GET`

**Purpose:** Flush the database and insert sample data set

**Sample output:**

Browser shows: `Database flushed and populated with some sample data.`