# SAE 15 – Projet n°5

## Aider un étudiant à planifier ses vacances

### Contexte

Dans le cadre de la **SAE 15** du **BUT Réseaux & Télécommunications**, ce projet vise à aider un étudiant à organiser ses vacances en identifiant **le premier cours planifié après chaque période de vacances universitaires**.

Avant de partir, l’étudiant peut ainsi vérifier qu’aucun cours n’est prévu avant son retour et connaître précisément les informations du cours de reprise.

---

### Objectif du projet

Afficher, pour un **groupe d’étudiants de BUT1** appartenant à un département donné :

* le **nom du module**
* la **date**
* l’**heure**
* la **salle**
* le **nom de l’enseignant**

du **premier cours après chaque période de vacances** :

* Toussaint
* Pont de novembre
* Noël
* Hiver
* Printemps
* Pont de l’Ascension

---

### Cahier des charges fonctionnel

* Les données sont **extraites d’ADE** (export CSV).
* Le **choix du groupe de TP est paramétrable** via une entrée utilisateur.
* Le script prend en compte **toute l’année universitaire**, du **1er septembre au 31 août**.
* Le code est **structuré** et repose sur l’utilisation de fonctions (principe attendu dans la SAE).

---

### Correction du script `icalTOcsv.py` (gestion de la timezone)

Lors de l’exploitation des données issues d’ADE, un problème a été identifié dans le script fourni initialement (`icalTOcsv.py`).
Celui-ci **ne prenait pas en compte la timezone**, ce qui entraînait des **décalages d’horaires** entre les cours affichés dans ADE et les heures présentes dans le fichier CSV généré.

Afin de garantir la fiabilité des informations (notamment l’heure du premier cours après les vacances), une **correction a été apportée** pour intégrer correctement la gestion de la timezone lors de la conversion du fichier `.ics` vers `.csv`.

Cette correction permet :

* d’obtenir des **horaires exacts**,
* d’éviter les décalages d’une ou deux heures selon la période de l’année,
* et d’assurer la cohérence des données utilisées par le script principal du projet.

---

### Fonctionnement général

1. L’utilisateur choisit son **groupe de TP** (TP1 à TP4).
2. Le script associe automatiquement les **groupes ADE correspondants**.
3. Pour chaque rentrée de vacances définie :

   * le script recherche les cours du jour concerné,
   * filtre les cours correspondant aux groupes de l’étudiant,
   * affiche le **premier cours de la journée**, trié par heure de début.
4. Si aucun cours n’est trouvé, un message explicite est affiché.

---

### Prérequis

* Python 3
* Bibliothèque **pandas**

Installation de pandas si nécessaire :

```bash
pip install pandas
```

---

### Structure des données

Le script utilise un fichier CSV issu d’ADE, nommé par exemple :

```
calendrier.csv
```

Ce fichier doit contenir au minimum les colonnes suivantes :

* `Date`
* `HStart`
* `Group`
* `Summary`
* `Location`
* `Teacher`

---

### Utilisation

1. Placer le fichier `calendrier.csv` dans le répertoire indiqué dans le script.
2. Lancer le programme :

```bash
python main.py
```

3. Sélectionner le **groupe de TP** lorsque demandé.
4. Consulter les informations affichées pour chaque rentrée de vacances.

---

### Exemple de sortie

```
--- Rentrée des Vacances d'hiver ---
Date   : 2026-02-23
Heure  : 09:00
Module : Téléphonie2
Salle  : A5-A5bis
Prof   : TOUSSAINT JOEL
```

---

### Limites et améliorations possibles

* Gestion automatique des dates de vacances via un calendrier académique.
* Recherche du **premier cours réel après la rentrée**, même s’il n’y a pas cours le jour exact.
* Interface graphique ou interface web.
* Séparation complète du code en fonctions dédiées (lecture, filtrage, affichage).

---

### Auteur

Projet réalisé dans le cadre de la **SAE 15 – BUT Réseaux & Télécommunications**
Projet n°5 – Aider un étudiant à planifier ses vacances
