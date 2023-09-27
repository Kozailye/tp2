#cree par Elie Kozaily
#cree en 2023
#cree dans le but de faire un jeu de devinette (tp2)

import random #pour importer la fonction random
import sys #pour la fonciton sys.exit (sortir du programme)

nbr1 = int(input("veuillez entre un premier nombre :"))
nbr2 = int(input("veuillez entre un deuxieme nombre :"))

hasard = random.randint(nbr1, nbr2)
essaie =0



valeur = int(input("veuillez entrer un nombre entre %d et %d pour deviner le nombre généré au hasard par l'ordinateur: " % (nbr1, nbr2)))

#création de la fonction boucle qui as pour but de determiner si ton essaie est plus grand ou plus petit que le nombre generer par l'ordinateur
#si la fonction n'est pas egale a la bonne reponse la boucle continue jusqu'a se que la bonne reponse soit trouver
#le nombre d'essaie est aussi compter et a chaque essaie sa fait plus 1 et a la fin sa te donne ton nombre d'essaie final


while valeur != hasard :

   if valeur > hasard :
       print ("Ta valeur est trop grande")
       essaie = essaie + 1

       valeur = int(input("veuillez entrer un nombre au hasard entre 1 et 1000 : "))

   elif valeur < hasard :
       print ("Ta valeur est trop petite")
       essaie = essaie + 1
       valeur = int(input("veuillez entrer un nombre au hasard entre 1 et 1000 : "))

else :
       print("Bravo! tu as trouvé la bonne reponse")
       print ("nombre d'essaie total:")
       print(essaie + 1)
       sys.exit()

