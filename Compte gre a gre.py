"""ADAMOU SAMBERO GNAGNA Mat:18A893FS"""


class Compte_Gre_a_gre: #Ceci est une classe

        #Constructeur

        def __init__(self,mt = 0.0,solde = 0.0):
        self._mt = mt
        self._solde = solde
        
        # Methode d'affichage du solde d'abord avant de commencer
    def __str__(self):
         return "Solde disponible : {0}".format(self.solde)

        # Methode d'affichage du solde qui sera utiliser apres avoir fait un versement ou un retrait 

    def infoSolde(self):
        print("Votre solde est de {0} FCFA ! ".format(self._solde))

        # Methode versement

    def versement(self,mt):
        self._solde += mt
        print("Versement de {0} FCFA éffectué !".format(mt))
        self.infoSolde()
    
         # Methode retrait

    def retrait(self,mt):
        if(mt>solde):
            print("Solde insuffisant")
        else:
            self._solde -= mt
            print("Le montant débité est de {0} FCFA".format(mt))

            # appel de la 2e methode pour l'affichage du nouveau solde
        self.infoSolde()
