#Moussa boubakary 18A856FS
#création de la SURCLASSE classe mère Compte

class Compte:     
    
#Classe représentant le compte d'une personne

    def __init__(self,n = 0,solde = 0.0):
        self._numero = n
        self._solde = solde
        
    def __str__(self):

        #Méthode appelée lors d'une conversion de l'objet en chaîne
        
        return "Code compte : {0} Solde : {1}".format(self._numero, self.solde)
    
    def _get_numero(self):
        print("numéro de compte est : {0}".format(self._numero))
        return self._numero
    
    def _get_solde(self):
        print("Solde est de {0} FCFA ".format(self._numero))
    
    def _set_solde(self,new_solde):
        print("nouveau solde est de {0} FCFA ".format(new_solde))
        self._solde = new_solde
    
    def infoSolde(self):
        print("Votre solde est de {0} FCFA ! ".format(self._solde))

    def versement(self,add):
        self._solde += add
        print("Versement de {0} FCFA éffectué !".format(add))
        self.infoSolde()
    
    def retrait(self,moins):
        self._solde -= moins
        print("Le montant débité est de {0} FCFA".format(moins))
        self.infoSolde()
    
    solde = property(_get_solde, _set_solde)    
    numero = property(_get_numero)
