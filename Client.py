

class Client(Personne):

    def __init__(name,prenom,identifiant,solde):
        self.soldeMensuel = solde

#verifie son solde mensuel   
    def getSolde(self):
        return self.soldeMensuel

#situation endetté ou non   
    def getdette(self):
        return self.dette

#demande de verification de sa situation d'emprunt
    def getEmprunt(self):
        return self.Emprunt
 
 #demande un emprunt       
    def setEmprunt(self):
        return self.Emprunt
        
   


