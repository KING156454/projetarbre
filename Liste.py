class Cellule:
    def __init__(self, valeur, successeur):
        'Initialise la cellule '
        self.valeur = valeur
        self.successeur = successeur  

class Liste_chainee:
    def __init__(self):
        self.debut = None
        self.longueur = 0
        
    def ajoute_debut(self, valeur):
        cell = Cellule(valeur, self.debut) 
        self.debut = cell    
    
    def __repr__(self):
        affichage = ""
        cellule_courante = self.debut
        while cellule_courante != None:
            affichage += str(cellule_courante.valeur) + ' '
            cellule_courante = cellule_courante.successeur
        return affichage


    def sup_debut(self):
        if self.debut == None:
            return None
        else :
            self.debut = self.debut.successeur
    
    def ajoute_fin(self,valeur):
        if self.debut is None :
            self.ajoute_debut(valeur)
        else :
            Cellule_courrante = self.debut
            while Cellule_courrante.successeur is not None :
                Cellule_courrante = Cellule_courrante.successeur
            nouvelle_cellule = Cellule(valeur, None)
            Cellule_courrante.successeur = nouvelle_cellule
        self.longueur += 1

    def sup_cellule(self,nom):
        if self.debut == None :
            return
        else:
            self.debut = self.debut.successeur
        self.longueur -= 1

    def sup_cellule_fin(self):
        if self.debut is None:
            return None
        if self.debut.successeur is None:
            self.debut = None
            return None
        cellule = self.debut
        while cellule.successeur.successeur is not None:
            cellule = cellule.successeur
        cellule.successeur = None

    def complexite(self) :
        if self.debut is None :
            return 0
        compteur = 0
        cc = self.debut
        while cc is not None :
            compteur += 1
            cc = cc.successeur
        return compteur

    def taille(self):
        if self.debut is None :
            return 0
        compteur = 0
        cc = self.debut
        while cc is not None :
            compteur += 1
            cc = cc.successeur
        return compteur
    
    def recherche_cellule_index(self,index) :
        if index < 0 or index > self.longueur:
            print("erreur index")
            return
        cellule_courante = self.debut
        cc = self.debut
        for i in range(index):
            cc = cc.successeur
        return cc.valeur
    
    def recherche_cellule_valeur(self,valeur):
        if self.debut == None :
            return None
        cc = self.debut
        compteur = 0
        while cc.valeur != valeur and cc.successeur is not None :
            cc = cc.successeur
            compteur += 1
        if cc.valeur == valeur :
            return compteur
        else :
            return None
    
    def sup_liste_index(self,index):
        if index < 0 or index >= self.longueur:
            print("erreur index")
            return
        if index == 0 :
            self.debut = self.debut.successeur
            return
        cc = self.debut
        for i in range(index-1):
            cc = cc.successeur
        cc.successeur = cc.successeur.successeur
        self.longueur -= 1
    
    def insertion_index(self,index,valeur):
        if index < 0 or index > self.longueur:
            print("erreur index")
            return
        if index == 0 :
            self.ajoute_debut(valeur)
            return
        cc = self.debut
        for i in range(index-1):
            cc = cc.successeur
        nouvelle_cellule = Cellule(valeur,cc.successeur)
        cc.successeur = nouvelle_cellule
        self.longueur += 1
    
    def sup_valeur(self,valeur):
        if self.debut is None :
            return
        if self.debut.valeur == valeur :
            self.debut = self.debut.successeur
            return
        cc = self.debut
        while cc.successeur is not None and cc.successeur.valeur != valeur :
            cc = cc.successeur
        if cc.successeur is not None and cc.successeur.valeur == valeur :
            cc.successeur = cc.successeur.successeur
            self.longueur -= 1
    
    def sup_valeur_toutes(self,valeur):
        if self.debut is None :
            return
        while self.debut is not None and self.debut.valeur == valeur :
            self.debut = self.debut.successeur
            self.longueur -= 1
        cc = self.debut
        while cc is not None and cc.successeur is not None :
            if cc.successeur.valeur == valeur :
                cc.successeur = cc.successeur.successeur
                self.longueur -= 1
            else :
                cc = cc.successeur