"""DINAMOU YINYANG WILFRIED Mat:18B326FS"""

#Importation des differentes classes

from Compte import Compte
from Client import Client
from Courant import Courant
from Personne import Personne
from Compte_epargne import Compte_epargne
from Compte_gre_a_gre import Compte_gre_a_gre
from Controleur import controleur
from Chef_agence import Chef_agence
from Guichetier import Guichetier
from Gestionnaire import Gestionnaire



"""Définition de la classe Banque"""
class Banque : 
    
    def __init__(self):
        self.nom = "UBA"; #Par exemple
        self.codeB = 000;
        self.controleur = Controleur();
        self.gestionnaire = Gestionnaire();
        self.guichetier = Guichetier();
        self.caisse = 10000000; # Montant de la caisse de la banque
        self.nbrCompte = 0; # Nombre de compte bancaire créé
        self.capital = 10000000000; # Capital de la banque
        
    def __str__(self):
        return "\t {0} code : {1}\nCapital : {2} FCFA\nNombre de Compte : {3}\n\n".format(self.nom,self.codeB,self.capital,self.nbrCompte);
