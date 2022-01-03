# Hamel Ludovic, Vague Charlotte
def main():

    # Attribution des variables
    score = 0
    niveau = 1
    vies = 3

    # On définit une fonction pour créer les séquences de caractère utilisées dans le programme,
    def sequence(niveau):
        troncon = ""
        # La fonction génère un nombre de lettres égal au niveau.
        for lettre in range(niveau):
            troncon += (chr(int(random() * 26+65)))
        return troncon

    # La boucle tourne tant que l'utilisateur a des vies en résèrve
    while vies > 0:
        messageA = "Niveau"+" "+ str(niveau) + ' : vous avez' + " " +str(vies) + " vies restantes"
        chaine = sequence(niveau)
        alert(messageA)
        alert(chaine)
        reponse = input("Qu'avez vous lu ?\n")
        if reponse == chaine:

            # Si l'utilisateur réussit il passe au prochain niveau et gagne un nombre de point égal aux lettres devinées
            score += niveau
            niveau += 1
            alert("Bravo, c'est la bonne réponse :) .")

        # Si l'utilisateur se trompe, il perd une vie
        else:
            vies -= 1
            alert("Oups ce n'est pas bon :( !")

    messagePerte = "Vous avez perdu , vous avez " + str(score) + " points."
    alert(messagePerte)


main()
