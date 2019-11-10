#HAMADOU OUSMANOU 18A040FS

class Guichetier(Compte): #Sous-Classe Guichetier ayant comme classe mere Personne
     montantv = input("Saisir le Montant de versement\n")
    # Notre méthode constructeur

     def __init__(self,solde): 

         #Constructeur de notre classe
      
      def affSolde(self):
        print("Solde disponible est de {0} FCFA : Protected".format(solde))

     def versement(self,compte,montantv):
         self.montantv=montantv
        # Un montant de la somme que vous entrez au clavier va etre retirer
         print("Versement de {0} : Protected".format(compte.montantv))
         self.affSolde(compte)
    
     def retrait(self,Compte,affSolde):
        """ ici, un test va etre effectuer dans la classe Controlleur pour savoir si le solde disponible est suffisant """
        # Si "OUI" ... un retrait de 7000 par exemple est effectuer
        print("montant débité de {0} FCFA: Protected".format(soldeDispo))
        self.affSolde()
          
          
          # lien video youtube https://youtu.be/0uDGzEvi620
