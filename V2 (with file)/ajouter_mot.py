import sauvegarder_dictionnaire

def ajouter_mot(dictionnaire):
    mot = input("Entrez le mot à ajouter : ").lower()
    if mot in dictionnaire:
        print("Ce mot existe déjà !")
    else:
        definition = input("Entrez la définition : ")
        dictionnaire[mot] = definition
        sauvegarder_dictionnaire.sauvegarder_dictionnaire(dictionnaire)
        print(f"Mot '{mot}' ajouté avec succès !")