
class Personne :
    def __init__(self, nom ,prenom,cin) :
        self.nom=nom
        self.prenom= prenom
        self.cin= cin
    def toString(self):
        print(f" Nom : {self.nom} \n Prenom : {self.prenom} \n cin : {self.cin}")
class Vaccine(Personne) :
    def __init__(self,nom,prenom,cin,code,date) :
        super().__init__(self,nom,prenom,cin)
        self.__code=code
        self.__date=date
    def get_code(self):
        return self.__code
    def get_date(self) :
        return self.__date
    def set_code(self,code1):
        self.__code=code1
    def set_date(self,date1) :
        self.__date=date1
    def toString(self):
        print(f" Nom : {super().nom} Prenom : {super().prenom} cin : {super().cin} de code de vaccination : {self.__code} a la date {self.__date}")
class Vaccin(Personne) :
    def __init__(self,nom,prenom,cin,code,nom_1,dure):
        super().__init__(self,nom,prenom,cin)
        self.code=code
        self.nom_1= nom_1
        self.dure=dure
    def toString(self):
        print(f" Nom : {super().nom} Prenom : {super().prenom} cin : {super().cin} de code de vaccination : {self.__code} a la date {self.__date} de nom vaccin : {self.name_1} a la durée {self.dure}")      
P1 = Personne("Diarra","Moussa","je ne sais quoi")
P1.toString()
 