import json

def afficher_menu():
    print("""
    Gestion d'un dictionnaire
    1. Ajout d'un mot
    2. Suppression d'un mot
    3. Recherche d'un mot
    4. Affichage de tout le dictionnaire
    0. Fin du programme
    """)

def ajouter_mot(dictionnaire):
    mot = input("Entrez le mot à ajouter : ").lower()
    if mot in dictionnaire:
        print("Ce mot existe déjà !")
    else:
        definition = input("Entrez la définition : ")
        dictionnaire[mot] = definition
        print(f"Mot '{mot}' ajouté avec succès !")

def supprimer_mot(dictionnaire):
    mot = input("Entrez le mot à supprimer : ").lower()
    if mot in dictionnaire:
        del dictionnaire[mot]
        print(f"Mot '{mot}' supprimé avec succès !")
    else:
        print("Ce mot n'existe pas dans le dictionnaire.")

def rechercher_mot(dictionnaire):
    mot = input("Entrez le mot à rechercher : ").lower()
    if mot in dictionnaire:
        print(f"Définition de '{mot}' : {dictionnaire[mot]}")
    else:
        print("Ce mot n'existe pas dans le dictionnaire.")

def afficher_dictionnaire(dictionnaire):
    if dictionnaire:
        print("\nDictionnaire complet :")
        for mot, definition in sorted(dictionnaire.items()):
            print(f"{mot} : {definition}")
    else:
        print("Le dictionnaire est vide.")

def main():
    dictionnaire = {
        "arbre": "Plante vivace possédant un tronc en bois.",
        "balise": "Marque servant à indiquer une direction ou un repère.",
        "chat": "Petit félin domestique apprécié pour sa compagnie.",
        "désert": "Région aride avec peu de précipitations et de végétation.",
        "éléphant": "Grand mammifère terrestre avec une trompe.",
        "forêt": "Étendue de terrain couverte d'arbres.",
        "glace": "Eau congelée, solide et transparente.",
        "harmonie": "Équilibre et accord parfait entre plusieurs éléments.",
        "île": "Terre entourée d'eau de tous côtés.",
        "jardin": "Espace aménagé pour cultiver des plantes et fleurs.",
        "kayak": "Embarcation légère propulsée à la pagaie.",
        "lion": "Grand félin d'Afrique connu pour sa crinière.",
        "montagne": "Relief élevé formé par des mouvements tectoniques.",
        "nuage": "Masse visible constituée de gouttelettes d'eau en suspension.",
        "océan": "Vaste étendue d'eau salée couvrant une grande partie de la Terre.",
        "pluie": "Précipitation d'eau sous forme liquide tombant des nuages.",
        "quartz": "Minéral dur et translucide souvent utilisé en bijouterie.",
        "rivière": "Cours d'eau coulant vers un lac, une mer ou un océan.",
        "soleil": "Étoile centrale du système solaire.",
        "tigre": "Félin sauvage rayé vivant en Asie.",
        "univers": "Ensemble de tout ce qui existe, y compris l'espace et le temps.",
        "vent": "Déplacement d'air causé par des différences de pression.",
        "wagon": "Véhicule ferroviaire servant au transport des passagers ou marchandises.",
        "xylophone": "Instrument de musique composé de lames de bois frappées.",
        "zèbre": "Mammifère africain reconnaissable à ses rayures noires et blanches."
    }
    while True:
        afficher_menu()
        choix = input("Votre choix : ")
        match choix:
            case "1":
                ajouter_mot(dictionnaire)
            case "2":
                supprimer_mot(dictionnaire)
            case "3":
                rechercher_mot(dictionnaire)
            case "4":
                afficher_dictionnaire(dictionnaire)
            case "0":
                print("Fin du programme.")
                break
            case _:
                print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
