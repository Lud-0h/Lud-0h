# Hamel Ludovic, Vague Charlotte
def main():
    phrase = list(str(input("Écrivez une phrase :")))

    # Initialisation des variables
    ListeVoyelles = str("aeiouyAEIOUY")
    espace = " "

    car = len(phrase)

    a, voyelles, mots = 0, 0, 1

    # On fait tourner la boucle jusqu'à ce que le numéro du caractère de la phrase soit le nombre de caractère total.
    while a != car:
        # Chaque fois que le programme lit une voyelle, le compteur augmente
        if phrase[a] in ListeVoyelles:
            voyelles += 1
        # Pour calculer le nombre de mots, le programme compte le nombre d'espace (1 par défaut).
        if phrase[a] in espace:
            mots += 1
        a = a+1

    """Même si ce n'est peut-être pas nécéssaire, le programme vérifie si il faut mettre les mots au pluriel en fonction
    des valeurs des variables (si il y a un seul objet, le s disparaît/ on dit ce mot au lieu de cette phrase)"""

    print("La phrase "*(mots != 1) + "Le mot "*(mots == 1) + "fait", car, "caractère" + "s"*(car != 1))
    print("Il y a ", mots, " mot" + "s"*(mots != 1) + " dans cette phrase"*(mots != 1))
    print("Il y a ", voyelles, " voyelle" + "s"*(voyelles != 1) + " dans cette phrase"*(mots != 1) + " dans ce mot "*(mots == 1))


main()
