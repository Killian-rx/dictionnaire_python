import json

FICHIER_DICO = "dictionnaire.json"


def sauvegarder_dictionnaire(dictionnaire):
    with open(FICHIER_DICO, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4, ensure_ascii=False)