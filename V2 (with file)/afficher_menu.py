from charger_dictionnaire import charger_dictionnaire


def afficher_menu(dictionnaire):
    print(f"""
    Il y a actuellement {len(dictionnaire)} mots dans le dictionnaire :
    Gestion d'un dictionnaire
    1. Ajout d'un mot
    2. Suppression d'un mot
    3. Recherche d'un mot
    4. Affichage de tout le dictionnaire
    5. Modifier un mot
    0. Fin du programme
    """)


if __name__ == "__main__":
    # Charger le dictionnaire depuis le fichier JSON
    dictionnaire = charger_dictionnaire()

    # Afficher le menu avec le contenu du dictionnaire
    afficher_menu(dictionnaire)
