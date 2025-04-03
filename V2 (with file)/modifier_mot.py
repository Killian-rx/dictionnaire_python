def modifier_mot(dictionnaire):
    mot = input("Entrez le mot à modifier : ")
    if mot in dictionnaire:
        nouveau_mot = input("Entrez le nouveau mot ou appuyez sur entrer si vous ne voulait pas le modifier : ")
        nouvelle_definition = input("Entrez la nouvelle définition : ")

        if nouveau_mot:
            dictionnaire[nouveau_mot] = nouvelle_definition
            del dictionnaire[mot]
            print(f"Le mot '{mot}' a été renommé en '{nouveau_mot}' et mis à jour.")
        else:
            dictionnaire[mot] = nouvelle_definition
            print(f"Le mot '{mot}' a été mis à jour.")
    else:
        print("Mot introuvable dans le dictionnaire.")