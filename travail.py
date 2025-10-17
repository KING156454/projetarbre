from Pile_File import *

class Arbre() :
    def __init__(self, nom_racine) :
        self.nom_racine = nom_racine
        self.liste_fils = []
    
    def ajoute_fils(self, fils) :
        self.liste_fils.append(fils)
    
    def hauteur(self) :
        h_max = 0
        for fils in self.liste_fils :
            h_fils = fils.hauteur()
            h_max += 1


    def taille(self) :
        if self.vide() :
            return None
        return len(liste_fils)

    def binaire(self) :
        pass
    
    def parcours_largeur(self) :
        pass

    def parcours_profondeur_prefixe(self) :
        pass

    def liste_aretes(self) :
        pass

    def affiche(self) :
        pass
