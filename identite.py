# Ludovic Hamel et Charlotte Vague
import ift1016_identite
import random


def generer_nom_complet():
    nom = random.choice(ift1016_identite.liste_prenoms).title() + " " + random.choice(ift1016_identite.liste_noms).title()
    return nom


def generer_taille():
    taille = 140+(random.randint(0, 600)/10)
    return taille


def generer_nas():
    print()
    nas = ""
    verifier = 0
    chiffrecle = 1
    """Le principe général de cette fonction est de générer aléatoirement les 8 premiers chiffres du NAS, et de s'arranger
    pour que le dernier permette de vérifier la condition de validité."""
    for loop in range(8):
        chiffre = random.randint(0, 9)
        nas += str(chiffre)
        """À chaque fois que le programme génère un nouveau chiffre pour le NAS, il le multiplie par le coefficient 
        correspondant de la clé de vérification puis stocke la somme dans "verifier" """
        if chiffrecle == 1:
            verifier += chiffre
            """À la fin des "if", on attribue 1 ou 2 à "chiffrecle" en fonction de quel chiffre apparait sur la clé 
            comme coefficient, il change à chaque étape."""
            chiffrecle = 2
        elif chiffrecle == 2:
            if chiffre >= 5:
                # Si le chiffre est plus grand que 5 et qu'il devrait être multiplié, on le transforme comme indiqué.
                verifier += (chiffre*2 % 10)+1
            else:
                verifier += chiffre*2
            chiffrecle = 1
    # Si il le NAS est valide avant le dernier chiffre, on le garde comme tel en le finissant par un 0.
    if verifier % 10 == 0:
        nas += "0"
        return str(nas)
    else:
        """Afin que le NAS vérifie la condition, le dernier chiffre est déterminé par celui qui permettra d'avoir un 
        multiple de 10 avec la clé."""
        chiffre = 10-verifier % 10
        nas += str(chiffre)
        verifier += chiffre
        return str(nas)


def validation_nas(nas):
    compteur = 0
    verification = 0
    """Le principe de ce programme est identique, mais cette fois on décompose le NAS avec la variable "compteur" qui
    agit comme indice, qui scan au fur et à mesure le NAS et on stock la somme avec clé dans "verification". """
    for boucle in range(9):
        chiffre = int(nas[compteur])
        coef = 1 + compteur % 2
        compteur += 1
        if chiffre >= 5 and coef == 2:
            verification += (chiffre*2 % 10)+1
        else:
            verification += chiffre * coef
    if verification % 10 == 0:
        return True
    else:
        return False


def generer_email(nom):
    """On créé d'abord deux chaînes de caractères, une pour les caractères qu'on veut remplacer et une pour ceux
    avec lesquels on va les remplacer."""
    caracteres = "éÉèêëï '-"
    # On utilise le "1" pour remplacer les apostrophes et les tirets, qui seront supprimés à la fin du programme.
    remplacement = "eeeeei.11"
    type = 0
    """À chaque étape de la boucle, on avance dans les deux séries grâce à "type", et on remplace le caractère
    de la première par celui de la deuxième"""
    for loop in range(len(caracteres)):
        nom = nom.replace(caracteres[type], remplacement[type])
        type += 1
    nom = nom.replace("1", "")
    nom = nom.lower()
    email = nom + "@umontreal.ca"
    return email


def generer_date_naissance():
    annee = random.randint(1950, 2009)

    # Pour faciliter le calcul des jours, on sépare les mois longs et les mois courts
    moislong = "janvier", "mars", "mai", "juillet", "aout", "octobre", "décembre"
    moiscourt = "fevrier", "avril", "juin", "septembre", "novembre"
    bisextile = (annee % 4 == 0)

    """Avec 217 jours appartenant aux mois longs, la probabilité que notre date en comporte un est égale à 217/(365(+1))
    """
    if random.random() < 217/(365+bisextile-1):
        mois = random.choice(moislong)
    else:
        mois = random.choice(moiscourt)

    if mois in moislong:
        jour = random.randint(1, 31)
    if mois in moiscourt:

        """On modifie la borne supérieure en créant une équation qui soustrait 2 dans le cas du mois de février mais
        seulement 1 si c'est également une année bisextile."""
        jour = random.randint(1, 30-int(2*(mois == "fevrier")-bisextile))
    date = str(jour) + " " + mois + " " + str(annee)
    return date


def generer_mission():
    liste_missions = ["Concocter un antidote détruisant le covid-19 le plus vite possible", "Hacker l'ordinateur de Mustapha Boushaba pour augmenter les notes de tous les eleves à l'examen intra", "Pendant une journée, échangez de vie avec une personne tirée aléatoirement et respectez a la lettre sa routine et son programme de la journée"]
    mission = random.choice(liste_missions)
    return mission


def generer_identite():
    nom = generer_nom_complet()
    nas = generer_nas()
    print("Prénom et nom:", nom)
    print("Addresse courriel:", generer_email(nom))
    print("NAS:", nas)
    if validation_nas(nas):
        print("Le NAS est valide")
    print("Taille:", generer_taille(), "cm")
    print("Date de naissance", generer_date_naissance())
    print("Mission:", generer_mission())














