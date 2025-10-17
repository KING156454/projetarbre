from liste_chaine import Liste_chainee

class Pile:
    def __init__(self):
        self.donnees = Liste_chainee()       
        
    def push(self, element):
        self.donnees.ajoute_debut(element)

    def vide(self):
        if self.donnees.debut is None:
            return True
        return False

    def top(self):
        if not self.vide():
            return self.donnees.debut.valeur
        else:
            return None
    
    def pop(self):
        if self.donnees.debut is None:
            return
        val = self.donnees.debut.valeur
        self.donnees.sup_debut()
        return val
    
    def pop2(self):
        if not self.vide():
            self.donnees.sup_debut()
        else:
            print("liste vide")

    def pop3(self):
        return

class File:
    def __init__(self):
        self.donnees = Liste_chainee()
        
    def entrer(self, valeur):
        self.donnees.ajoute_fin(valeur)
        
    def sortir(self):
        if self.donnees.debut is None:
            return None
        valeur = self.donnees.debut.valeur
        self.donnees.sup_debut()
        return valeur
        
    def vide(self):
        if self.donnees.debut is None:
            return True
        return False