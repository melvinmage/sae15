import pandas as pd

a = input("Quel est votre groupe de TP ?\n1) TP1\n2) TP2\n3) TP3\n4) TP4\n» ")

while a not in ["1", "2", "3", "4"]:
    a = input("\nMauvaise entrée. Quel est votre groupe de TP ?\n1) TP1\n2) TP2\n3) TP3\n4) TP4\n» ")

groupe = ()

if a == "1":
    groupe = ("1A", "1ATDA", "1ATP1")
elif a == "2":
    groupe = ("1A", "1ATDA", "1ATP2")
elif a == "3":
    groupe = ("1A", "1ATDB", "1ATP3")
elif a == "4":
    groupe = ("1A", "1ATDB", "1ATP4")

print(f"Vous faites donc partie du {groupe[1][2:]} et du {groupe[2][2:]}.\n")

rentrees = {
    "Rentrée des Vacances de Toussaint": "2025-11-03",
    "Rentrée du Pont de Novembre": "2025-11-12",
    "Rentrée des Vacances de Noël": "2026-01-05",
    "Rentrée des Vacances d'hiver": "2026-02-23",
    "Rentrée des Vacances de Printemps": "2026-04-20",
    "Rentrée du Pont de l'Ascension": "2026-05-18"
}

calendrier = pd.read_csv("/home/UCA/memage/SAE15/Projet5/calendrier.csv")

for nom, date in rentrees.items():
    cours_du_jour = calendrier[calendrier["Date"] == date]
    cours_utiles = cours_du_jour[cours_du_jour["Group"].isin(groupe)]

    print(f"--- {nom} ---")

    if not cours_utiles.empty:
        premier_cours = cours_utiles.sort_values(by="HStart").iloc[0]
        print(f"Date : {premier_cours['Date']}")
        print(f"Heure : {premier_cours['HStart'][:5]}")
        print(f"Module : {premier_cours['Summary']}")
        print(f"Salle : {premier_cours['Location']}")
        print(f"Prof : {premier_cours['Teacher']}\n")
    else:
        print(f"Pas de cours trouvés le {date} pour vos groupes.\n") 