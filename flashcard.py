# Hamel Ludovic Vague Charlotte

import questions
import random


def fonction():
    questions_en_memoire = []
    print("Bonjour, veuillez choisir parmi les questions suivantes :")
    indicateur = input("1- Faire un Test ! \n 2- Ajouter des questions \n 3- Chercher des questions par mot clé \n 4- "
                       "Visualiser toutes les questions \n 5- Exporter les questions \n 6- Importer les questions \n "
                       "7- Supprimer des questions \n q- quitter\n")

    def test_connaissance(questions_memoire):
        # On crée une variable qui sera identique aux questions en mémoire pour pouvoir la manipuler sans conséquences.
        questions_stockees = questions_memoire
        if not questions_stockees:
            print("Il n'y a plus de questions en memoire, revenons au menu.")
            fonction()
        # Pour ne pas reposer la même question plusieurs fois, on la retire à la liste temporaire des questions.
        else:
            tuplee = random.choice(questions_stockees)
            question, reponse = tuplee
            print(question)
            rep = input()
            if rep == "stop":
                fonction()
            print("La réponse est :", reponse)
            oui_non = input("Avez vous eu la bonne réponse ? (oui/non)")
            if oui_non == "oui":
                questions_stockees.remove(tuplee)
                test_connaissance(questions_stockees)
            if oui_non == "stop":
                fonction()
            else:
                test_connaissance(questions_stockees)

    def ajout_question(questions_stockees):
        question = input("Question : ")
        while question == "":
            question = input("Votre question est invalide, répétez")
        if question == "stop":
            fonction()
        reponse = input("Réponse : ")
        while reponse == "":
            reponse = input("Votre réponse est invalide, répétez")
        if reponse == "stop":
            fonction()
        # Si l'utilisateur n'écrit pas stop, la question est ajoutée et la fonction se relance.
        else:
            questions_stockees.append((question, reponse))
            ajout_question(questions_stockees)

    def chercher_question(questions_stockees):
        mot_cher = str(input("Quel mot voulez vous chercher ?\n"))
        questions_cherchees = ""
        for nbr_qu in range(len(questions_stockees)):
            # Quand on passe sur une question qui contient le mot, on la stocke dans une variable qui sera imprimée.
            if mot_cher in (questions_stockees[nbr_qu])[0]:
                questions_cherchees += str(questions_stockees[nbr_qu][0])
        if questions_cherchees == "":
            print("Il n'y a pas de questions contenant ce mot.")
        else:
            print("Les questions concernées:\n", questions_cherchees)
        fonction()

    def visualiser_questions(questions_stockees):
        ouinon = input("Voulez vous voir les réponses ? (oui/non)\n")
        # On fait tourner une boucle pour le nombre de questions en mémoire.
        for nbr_qu in range(len(questions_stockees)):
            question, reponse = questions_stockees[nbr_qu]
            # Le numéro de la question correspond à l'étape de la boucle +1 car pour python la 1ere étape est 0.
            print("Question", nbr_qu + 1, ":", question)
            if ouinon == "oui":
                print("Réponse:", reponse)
        fonction()

    def supprimer_questions(questions_stockees):
        if not questions_stockees:
            print("Il n'y a pas de questions en mémoire.")
            fonction()
        for nbr_qu in range(len(questions_stockees)):
            question, reponse = questions_stockees[nbr_qu]
            print("Question", nbr_qu + 1, ":", question)
        suppression = int(input("Quelle question voulez vous supprimer ? (faites 0 pour quitter)"))
        if suppression == 0:
            fonction()
        questions_stockees.remove(questions_stockees[suppression - 1])
        print("Les questions sont maintenant:")
        supprimer_questions(questions_stockees)

    if indicateur == "1":
        test_connaissance(questions_en_memoire)

    if indicateur == "2":
        ajout_question(questions_en_memoire)

    if indicateur == "3":
        chercher_question(questions_en_memoire)

    if indicateur == "4":
        visualiser_questions(questions_en_memoire)

    if indicateur == "5":
        nom = str(input("Comment voulez vous nommer le fichier d'exportation ?\n"))
        resultat = questions.exporter(questions_en_memoire, nom)
        if not resultat:
            print("L'exportation ne put se faire.")
            fonction()
        else:
            print("L'exportation a réussi.")
            fonction()

    if indicateur == "6":
        nom = str(input("De quel fichier voulez-vous importer les questions ?\n"))
        nouvelles_questions = questions.importer(nom)
        # On immortalise les questions à importer pour le calcul des nouvelles questions.
        nouvelles_intactes = nouvelles_questions
        questions_en_double = []
        if not nouvelles_questions:
            print("L'importation ne peut avoir lieu.")
            fonction()
        else:
            # On passe à travers toutes les questions et on enlève celles qui sont en double
            for nbr_qu in range(len(nouvelles_questions)):
                tuplee = nouvelles_questions[nbr_qu-1]
                if tuplee in questions_en_memoire:
                    questions_en_double += tuplee
                    nouvelles_questions.remove(tuplee)
            # On ajoute seulement les nouvelles questions (pas de double).
            questions_en_memoire += nouvelles_questions
            print("L'importation s'est effectuée avec succès, il y a", len(nouvelles_intactes)-len(questions_en_double),
                  "nouvelles questions")
            fonction()

    if indicateur == "7":
        supprimer_questions(questions_en_memoire)

    if indicateur == "q":
        exit()

    else:
        print("Cette entrée est invalide, recommencez.")
        fonction()


fonction()


