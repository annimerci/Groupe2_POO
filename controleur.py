
#LABARAN ABOUBAKAR 18A090FS // lien video : https://youtu.be/wkmR2qYjFwc

@author: Capri
"""
import Personne.py
class Controleurs(Personne):

    
# Quand un client veut retirer de l'argent
        Retrait=0
        solde=0
    def Retirer(self,nom,prenom,identifiant,Retrait,solde):
         Personne.__init__(self,nom,prenom,identifiant)
        self._Retrait=Retrait
        self._solde=solde
        if ( solde >= Retrait):
            print("Vous allez effectuer le retrait d'un montant de {}" .format(Retrait))
        else:
            print("Solde insuffisant") 
       
       
       
#Les conditions d'emprunt       
    def C_emprunt(self,montant,taux_emprunt,dette,soldeMensuel): 
         self._montant=montant
         self._taux_emprunt=taux_emprunt
         self._dette=dette
         self._soldeMensuel=soldeMensuel
         if (dette == False and soldeMensuel >= (montant * taux_emprunt)):
            print("vous venez d'effecture un emprunt de {} ".format(montant))
         else:
            print("la banque a refuse le credit")
         
#Verification            
       
    def Verifier(self,Trans_jr,solde_caisse):
        self._Trans_jr=Trans_jr
		self._solde_caisse=solde_caisse
        if (Trans_jr == solde_caisse):
            print("les transactions cadrent")
        else:
            print("les transactions ne cadrent pas")
