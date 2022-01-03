#Ludovic Hamel, Charlotte Vague

import matplotlib.pyplot as plt
import numpy as np
f = open('donneesTP2.csv', 'r')

liste = []
liste_valeur = []
pic = 0
valeur_debut = 0
valeur_fin = 0
# On créé une première liste de string contenant les données.
for i in f:
    liste.append(i)
# On la transforme en int et float
for i in liste:
    tuplee = i.split(',')
    liste_valeur.append(tuple([int(tuplee[0]), float(tuplee[1])]))
# Si des valeurs consécutives sont supérieures à 0.8, le pic augmente mais il retourne à 0 si une valeur est inférieure.
for i in range(len(liste_valeur)):
    if liste_valeur[i][1] > 0.8:
        pic += 1
    else:
        pic = 0
    # Quand le pic dépasse 10, on définit la valeur du début du pic, et celle de fin qui correspondra à l'indice maximal de la boucle+1.
    if pic >= 10:
        valeur_debut, valeur_fin = liste_valeur[i-9][0], i+1
        break

milisecondes = (valeur_debut%1000)
seconds=int((valeur_debut/1000)%60)
minutes=int((valeur_debut/(1000*60))%60)
print("Le pic d'activation a lieu à %d:%d.%d" % (minutes, seconds, milisecondes))



# On créé deux courbes, une pour représenter les valeurs de l'EEG et une pour indiquer le seuil 0.8 à dépasser par soucis de lisibilité.
seuil_x = np.linspace(valeur_debut-15, valeur_fin+15, 1000)
seuil_y = [0.8]*1000
# On prépare les listes qui seront utilisées pour créer le graphique en tirant les valeurs à représenter de la liste des valeurs en fonction de leur position par rapport au pic.
l = valeur_fin - valeur_debut + 31
#On initialise les variables avec des 0 pour pouvoir facilement remplacer leurs éléments
valeur_x = np.zeros(l)
valeur_y = np.zeros(l)
for i in range(l):
    valeur_x[i] = liste_valeur[valeur_debut -16 + i][0]
    valeur_y[i] = liste_valeur[valeur_debut -16 + i][1]

f1 = plt.figure()
plt.plot()
plt.plot(valeur_x, valeur_y, linestyle = '-', color = 'magenta', label = 'Activité cérébrale')
plt.plot(seuil_x, seuil_y, color= 'r', linestyle = '--', label = 'Seuil de pic d\'activation')
plt.legend()
# Titre des axes
plt.title("Pic d'activation cérébrale dans le scan EEG du patient")
plt.xlabel('Temps (ms)')
plt.ylabel('Activité cérébrale (%)')
plt.grid()
plt.savefig("graphique")


class PointDeDonnee(object):
    # Le constructeur prend comme paramètre un string et lui même.
    def __init__(self, str):
      # On utilise placeholder comme variable pour séparer les champs de l'objet.
        placeholder = str.split(',')
        self.temps = int(placeholder[0])
        self.activite = float(placeholder[1])

    def est_valide(self):
        # Si l'activite présente une valeur invalide, on sort la réponse appropriée
        if  0 < self.activite <= 1:
            return True
        return False

liste_erreur = []
# On créé une liste qui sera la cible pour réperer les erreurs
for i in liste:
    liste_erreur.append(PointDeDonnee(i))
# On compte les erreurs quand la fonction de l'objet retourne false
counter = 0
for i in liste_erreur:
    if not i.est_valide():
        counter += 1
print("La quantité d'erreurs est :", counter)