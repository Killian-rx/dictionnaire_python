def afficher_dictionnaire(dictionnaire):
    if dictionnaire:
        print("\nDictionnaire complet :")
        for mot, definition in sorted(dictionnaire.items()):
            print(f"{mot} : {len(definition.split())}")
    else:
        print("Le dictionnaire est vide.")