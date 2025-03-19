import charger_dictionnaire
import afficher_menu
import ajouter_mot
import supprimer_mot
import rechercher_mot
import afficher_dictionnaire

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