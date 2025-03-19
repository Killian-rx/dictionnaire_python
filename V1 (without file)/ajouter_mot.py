def ajouter_mot(dictionnaire):
    mot = input("Entrez le mot à ajouter : ").lower()
    if mot in dictionnaire:
        print("Ce mot existe déjà !")
    else:
        definition = input("Entrez la définition : ")
        dictionnaire[mot] = definition
        print(f"Mot '{mot}' ajouté avec succès !")