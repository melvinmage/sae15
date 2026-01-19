import pandas as pd

def demander_groupe_tp():
    """
    Demande à l'utilisateur son numéro de groupe (1 à 4)
    et vérifie que l'entrée est valide.
    """
    choix = input("Quel est votre groupe de TP ?\n1) TP1\n2) TP2\n3) TP3\n4) TP4\n» ")
    while choix not in ["1", "2", "3", "4"]:
        choix = input("\nMauvaise entrée. Quel est votre groupe de TP ?\n1) TP1\n2) TP2\n3) TP3\n4) TP4\n» ")
    return choix

def obtenir_codes_ade(choix_groupe):
    """
    Associe le choix de l'utilisateur (1, 2, 3, 4) aux 
    groupes présents dans le fichier ADE (ex: 1ATDA, 1ATP1).
    """
    groupes = ()
    if choix_groupe == "1":
        groupes = ("1A", "1ATDA", "1ATP1")
    elif choix_groupe == "2":
        groupes = ("1A", "1ATDA", "1ATP2")
    elif choix_groupe == "3":
        groupes = ("1A", "1ATDB", "1ATP3")
    elif choix_groupe == "4":
        groupes = ("1A", "1ATDB", "1ATP4")

    return groupes

def charger_donnees(chemin_fichier):
    """
    Charge le fichier CSV dans un DataFrame Pandas.
    """
    try:
        df = pd.read_csv(chemin_fichier)
        return df
    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        return None

def trouver_premier_cours(df, date_recherche, groupes_etudiant):
    """
    Cherche le premier cours disponible à une date donnée pour une liste de groupes.
    Retourne la ligne du DataFrame correspondant au cours ou None.
    """
    # 1. Filtrer par date
    cours_du_jour = df[df["Date"] == date_recherche]
    
    # 2. Filtrer par groupe (le cours doit être pour un des groupes de l'étudiant)
    cours_utiles = cours_du_jour[cours_du_jour["Group"].isin(groupes_etudiant)]
    
    if not cours_utiles.empty:
        # 3. Trier par heure de début et prendre le premier
        return cours_utiles.sort_values(by="HStart").iloc[0]
    else:
        return None

def afficher_resultat(nom_periode, date, cours):
    """
    Affiche joliment les informations du cours trouvé.
    """
    print(f"--- {nom_periode} ---")
    
    if cours is not None:
        print(f"Date   : {cours['Date']}")
        print(f"Heure  : {cours['HStart'][:5]}") # Coupe les secondes si nécessaire
        print(f"Module : {cours['Summary']}")
        print(f"Salle  : {cours['Location']}")
        print(f"Prof   : {cours['Teacher']}\n")
    else:
        print(f"Pas de cours trouvés le {date} pour vos groupes.\n")

def main():
    """
    Fonction principale qui orchestre le programme.
    """
    # 1. Configuration des dates de rentrée
    rentrees = {
        "Rentrée des Vacances de Toussaint": "2025-11-03",
        "Rentrée du Pont de Novembre": "2025-11-12",
        "Rentrée des Vacances de Noël": "2026-01-05",
        "Rentrée des Vacances d'hiver": "2026-02-23",
        "Rentrée des Vacances de Printemps": "2026-04-20",
        "Rentrée du Pont de l'Ascension": "2026-05-18"
    }
    
    # 2. Chargement des données
    chemin_csv = "/home/UCA/memage/SAE15/Projet5/calendrier.csv" # Vérifie bien ce chemin
    calendrier = charger_donnees(chemin_csv)
    
    if calendrier is not None:
        # 3. Interaction utilisateur
        choix = demander_groupe_tp()
        groupes = obtenir_codes_ade(choix)
        
        print(f"Vous faites donc partie du {groupes[1][2:]} et du {groupes[2][2:]}.\n")

        # 4. Boucle de traitement
        for nom_vacances, date_rentree in rentrees.items():
            premier_cours = trouver_premier_cours(calendrier, date_rentree, groupes)
            afficher_resultat(nom_vacances, date_rentree, premier_cours)

# Exécution du script
main()