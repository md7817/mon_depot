class Table :
    def __init__(self,ref,matiere,poid,hauteur,longueur,largeur,prix_vente,prix_fab,nombre) :
        self.ref=ref
        self.matiere=matiere
        self.poid =poid
        self.hauteur=hauteur
        self.longueur=longueur
        self.largeur=largeur
        self.prix_vente=prix_vente
        self.__prix_fab=prix_fab
        self.__nombre=nombre

    def get_prix_fab(self):
        return self.__prix_fab
    def get_nombre(self):
        return self.__nombre
    def affiche(self):
        print(f"La table contient : \n La référence : {self.ref} \n Matiere de la table : {self.matiere} \n La longeur x hauteur x hauteur : {(self.longueur)*(self.largeur)*(self.hauteur)} \n Le poid est : {self.poid} \ Et le prix de vente est : {self.prix_vente}")
    def gain(self) :
        print(f"Voici le gain : {(self.prix_vente)*(self.__nombre)}")
print("====== Main =====")
T1= Table("ref1","mat1",12,24,43,26,500,200,150)
T1.affiche()
T1.gain()
print("===== Fin =====")

        