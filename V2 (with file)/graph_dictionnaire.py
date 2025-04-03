import matplotlib.pyplot as plt  # Corrected import

def graph_dictionnaire(dictionnaire):
    if dictionnaire:
        mots = list(dictionnaire.keys())
        longueurs = [len(definition.split()) for definition in dictionnaire.values()]

        plt.figure(figsize=(10, 6))
        plt.bar(mots, longueurs, width=0.2, color='skyblue')
        plt.ylabel('Longueur de la définition')
        plt.xlabel('Mots')
        plt.title('Longueur des définitions dans le dictionnaire')
        plt.xticks(range(len(mots)), mots, rotation=45, ha='right')
        plt.show()
    else:
        print("Le dictionnaire est vide.")