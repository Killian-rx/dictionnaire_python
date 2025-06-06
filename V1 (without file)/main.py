import afficher_menu
import ajouter_mot
import supprimer_mot
import rechercher_mot
import afficher_dictionnaire
import modifier_mot

def main():
    dictionnaire = {
        "arbre": "Plante vivace possédant un tronc en bois.",
        "balise": "Marque servant à indiquer une direction ou un repère.",
        "chat": "Petit félin domestique apprécié pour sa compagnie.",
        "désert": "Région aride avec peu de précipitations et de végétation.",
        "forêt": "Étendue de terrain couverte d'arbres.",
        "glace": "Eau congelée, solide et transparente.",
        "harmonie": "Équilibre et accord parfait entre plusieurs éléments.",
        "jardin": "Espace aménagé pour cultiver des plantes et fleurs.",
        "kayak": "Embarcation légère propulsée à la pagaie.",
        "lion": "Grand félin d'Afrique connu pour sa crinière.",
        "montagne": "Relief élevé formé par des mouvements tectoniques.",
        "nuage": "Masse visible constituée de gouttelettes d'eau en suspension.",
        "océan": "Vaste étendue d'eau salée couvrant une grande partie de la Terre.",
        "pluie": "Précipitation d'eau sous forme liquide tombant des nuages.",
        "quartz": "Minéral dur et translucide souvent utilisé en bijouterie.",
        "rivière": "Cours d'eau coulant vers un lac, une mer ou un océan.",
        "soleil": "Étoile centrale du système solaire.",
        "tigre": "Félin sauvage rayé vivant en Asie.",
        "univers": "Ensemble de tout ce qui existe, y compris l'espace et le temps.",
        "vent": "Déplacement d'air causé par des différences de pression.",
        "wagon": "Véhicule ferroviaire servant au transport des passagers ou marchandises.",
        "xylophone": "Instrument de musique composé de lames de bois frappées.",
        "zèbre": "Mammifère africain reconnaissable à ses rayures noires et blanches."
    }
    while True:
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
                modifier_mot.modifier_mot(dictionnaire)
            case "0":
                print("Fin du programme.")
                break
            case _:
                print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
