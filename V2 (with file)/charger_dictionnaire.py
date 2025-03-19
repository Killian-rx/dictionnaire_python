#charger_dictionnaire.py

import json

FICHIER_DICO = "dictionnaire.json"


def charger_dictionnaire():
    try:
        with open(FICHIER_DICO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}