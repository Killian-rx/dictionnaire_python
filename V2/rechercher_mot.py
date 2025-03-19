def rechercher_mot(dictionnaire):
    mot = input("Entrez le mot à rechercher : ").lower()
    if mot in dictionnaire:
        print(f"Définition de '{mot}' : {dictionnaire[mot]}")
    else:
        print("Ce mot n'existe pas dans le dictionnaire.")