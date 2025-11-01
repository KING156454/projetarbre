from pile import *

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
            if h_fils > h_max :
                h_max = h_fils


    def taille(self) :
        taille_totale = 1
        for fils in self.liste_fils :
            taille_totale += fils.taille()
        return taille_totale 

    def binaire(self) :
        if len(self.liste_fils) > 2 :
            return False
        for fils in self.liste_fils :
            if not fils.binaire() :
                return False
        return True
    
    def parcours_largeur(self):
        resultat = ""
        file = [self]
        while file:
            noeud = file.pop(0)
            resultat += noeud.nom_racine + " "
            for fils in noeud.liste_fils:
                file.append(fils)
        return resultat

    def parcours_profondeur_prefixe(self) :
        pass

    def liste_aretes(self) :
        pass

    def affiche(self) :
        pass

    

arbre = Arbre("projetArbre")
rapport_pdf = Arbre("rapport.pdf")
source = Arbre("source")
code = Arbre("code")
arbre.ajoute_fils(rapport_pdf)
arbre.ajoute_fils(source)
arbre.ajoute_fils(code)
fichier1 = Arbre("fichier1")
fichier2 = Arbre("fichier2")
fichier3 = Arbre("fichier3")
source.ajoute_fils(fichier1)
source.ajoute_fils(fichier2)
source.ajoute_fils(fichier3)
test_py = Arbre("test.py")
arbre_py = Arbre("Arbre.py")
code.ajoute_fils(test_py)
code.ajoute_fils(arbre_py)


print(arbre.parcours_largeur())
