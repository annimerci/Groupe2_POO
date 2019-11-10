#TCHANGA TCHOUNGUI DARLIN 18B749FS
class compte_courants(compte):
    def __init__(self,n=0,solde=0.0):
        compte.__init__(self,n,solde)
        
#Grace aux comptes courants on peut transferts d'argent à un autre compte 
        def transferts (self,compt,montant):
            self._solde=montant
            compt.versement(montant)
