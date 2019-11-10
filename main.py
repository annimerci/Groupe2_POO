# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:44:54 2019

@author: Capri
"""

#importation des diffÃ©rentes classes


from Banque import Banque
from Compte import Compte
from Client import Client
from Courant import Courant
from Personne import Personne
from Compte_epargne import Compte_epargne
from Controleur import controleur
from Chef_agence import Chef_agence
from Guichetier import Guichetier
from Gestionnaire import Gestionnaire
from Compte_gre_a_gre import Compte_gre_a_gre
#Teste du fonctionnement de la classe Banque()
bank = Banque()

#GrÃ¢ce Ã  la mÃ©thode __str__ on peut faire : 
print(bank) 

#Teste de la classe Compte

#La crÃ©ation d'un compte ce fait normalement lors de la dÃ©claration d'un Client ( ceci est juste un exemple )
c = Compte(100,1500)
print(c)
#Le gestionnaire Ã  ici pour role de creer, supprimer un compte dans une instance de Banque

g = Gestionnaire("17B463FS","DIEZOUMBE" "dd")
g.ajoutCompte(bank)
print(bank)
g.ajoutCompte(bank)
g.ajoutCompte(bank)
print(bank)
g.supprimeCompte(bank)
print(bank)
#Le controleur ici Ã  pour rÃ´le de vÃ©rifier si le solde du compte est suffisant (pour un retrait)

cont =  Controleur()

#Petit exemple
if( cont.verifier( c.solde , 4000) ):
  print( "Votre solde est supÃ©rieur Ã  4000 FCFA ! \n" )
else:
  print( "Votre solde est infÃ©rieur Ã  4000 FCFA ! \n" )
  #CrÃ©ation d'un Client

buyer = Client("17A193FS","Ludovic","ludovic02")
buyer.verser(40000)
buyer.verser(50000)
print(buyer) #information sur le client
buyer.retrait(4000)

print(buyer.bank) #Information sur la banque du client   
#GrÃ¢ce Ã  la classe Courant, il est possible d'Ã©ffectuÃ© des transfert d'argent entre 2 comptes
#EXEMPLE : 
c1 = Courant(1,40000)
c2 = Courant(2,1250)

c1.transfert(c2 , 20000) # On prÃ©lÃ¨ve 20000 dans c1 pour envoyer Ã  c2
print(c1)
print(c2)
#GrÃ¢ce Ã  la classe Compte_Gre_a_gre, il est possible d'Ã©ffectuÃ© des transfert d'argent entre 2 clients
#EXEMPLE :
buyer1=buyer(20000)
buyer2=buyer(30000)
buyer1.transfert(buyer2, 10000)
print(buyer1)
print(buyer2)
#La classe Personne est la super-classe pour Client, Gestionnaire, Controleur et Guichetier
p = Personne("18A090FS","LABARAN","CAPRI") 

#On peut le spÃ©cialiser en Client
p = Client()
#Qui  peut Ãªtre aussi recrutÃ© par la banque pour devenir un Controleur par exemple
p = Controleur()

#La classe Personne se contente de regrouper ensemble les attributs propres aux Guichetier, Controleur et Gestionnaire


#...
