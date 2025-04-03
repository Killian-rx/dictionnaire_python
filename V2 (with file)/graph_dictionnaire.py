
import matplotlib as plt

def graph_dictionnaire(dictionnaire):
    """
    Affiche un graphique représentant le nombre de mots dans le dictionnaire.
    """
    if dictionnaire:
        for mot, definition in sorted(dictionnaire.items()):
            longueurs = [len(definition.split())]

        plt.figure(figsize=(10, 6))
        plt.barh(definition, longueurs, color='skyblue')
        plt.xlabel('Longueur du mot')
        plt.ylabel('Mots')
        plt.title('Longueur des mots dans le dictionnaire')
        plt.show()
    else:
        print("Le dictionnaire est vide.")