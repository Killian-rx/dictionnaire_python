import charger_dictionnaire
import afficher_menu
import ajouter_mot
import supprimer_mot
import rechercher_mot
import afficher_dictionnaire
import modifier_mot


def main():
    # Charger le dictionnaire depuis le fichier JSON
    dictionnaire = charger_dictionnaire.charger_dictionnaire()

    while True:
        # Afficher le menu en passant dictionnaire en argument
        afficher_menu.afficher_menu(dictionnaire)
        choix = input("Votre choix : ")

        match choix:
            case "1":
                ajouter_mot.ajouter_mot(dictionnaire)
            case "2":
                supprimer_mot.supprimer_mot(dictionnaire)
            case "3":
                rechercher_mot.rechercher_mot(dictionnaire)
            case "4":
                afficher_dictionnaire.afficher_dictionnaire(dictionnaire)
            case "5":
                modifier_mot.modifier_mot(dictionnaire)  # Ajout de l'option de modification
            case "0":
                print("Fin du programme.")
                break
            case _:
                print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
