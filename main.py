#cree par Elie Kozaily
#cree en 2023
#cree dans le but de faire un jeu de devinette (tp2)
import random #pour importer la fonction random

def devinete(): #fonction qui sert a lancer le jeu
    recommencer = True

#boucle qui sert a recommecer le jeu tant que l'utilisateur veut jouer
    while recommencer:

        nbr1 = int(input("veuillez entre un premier nombre :"))
        nbr2 = int(input("veuillez entre un deuxieme nombre :"))

        hasard = random.randint(nbr1, nbr2)
        essaie = 0

        valeur = int(input("veuillez entrer un nombre entre %d et %d pour deviner le nombre généré au hasard par l'ordinateur: " % (nbr1, nbr2)))

        #création de la fonction boucle qui as pour but de determiner si ton essaie est plus grand ou plus petit que le nombre generer par l'ordinateur

        while valeur != hasard :

           if valeur > hasard :
               print ("Ta valeur est trop grande")
               essaie = essaie + 1

               valeur = int(input("veuillez entrer un nombre entre %d et %d pour deviner le nombre généré au hasard par l'ordinateur: " % (nbr1, nbr2)))

           elif valeur < hasard :
               print ("Ta valeur est trop petite")
               essaie = essaie + 1
               valeur = int(input("veuillez entrer un nombre entre %d et %d pour deviner le nombre généré au hasard par l'ordinateur: " % (nbr1, nbr2)))

        else :
               print("Bravo! tu as trouvé la bonne reponse")
               print ("nombre d'essaie total:")
               print(essaie + 1)
               rejouer = str(input("Voulez-vous rejouez, oui ou non : "))
               if rejouer == "non":
                   recommencer = False

devinete()

