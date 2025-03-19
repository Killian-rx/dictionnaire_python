import sauvegarder_dictionnaire

def supprimer_mot(dictionnaire):
    mot = input("Entrez le mot à supprimer : ").lower()
    if mot in dictionnaire:
        del dictionnaire[mot]
        sauvegarder_dictionnaire.sauvegarder_dictionnaire(dictionnaire)
        print(f"Mot '{mot}' supprimé avec succès !")
    else:
        print("Ce mot n'existe pas dans le dictionnaire.")