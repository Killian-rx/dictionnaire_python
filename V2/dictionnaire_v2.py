import json

FICHIER_DICO = "dictionnaire.json"

def charger_dictionnaire():
    try:
        with open(FICHIER_DICO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def sauvegarder_dictionnaire(dictionnaire):
    with open(FICHIER_DICO, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4, ensure_ascii=False)

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
        sauvegarder_dictionnaire(dictionnaire)
        print(f"Mot '{mot}' ajouté avec succès !")

def supprimer_mot(dictionnaire):
    mot = input("Entrez le mot à supprimer : ").lower()
    if mot in dictionnaire:
        del dictionnaire[mot]
        sauvegarder_dictionnaire(dictionnaire)
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
    dictionnaire = charger_dictionnaire()
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
