class Pet :
    def __init__(self, name,animalType,age):
        self.__name=name
        self.__animalType=animalType
        self.__age=age
    def get_name(self):
        return self.__name
    def get_animalType(self) :
        return self.__animalType
    def get_age(self) :
        return self.__age
    def set_name(self,name1):
        self.__name =name1
    def Set_animalType(self,type1) :
        self.__animalType = type1
    def set_age(self,age1) :
        self.__age = age1
print("====== Debut ======")
name=input("Donner le nom de l'animal : ")
type=input("Donner le type de l'animal : ")
age=int(input("Donner l'age de l'animal : "))
P = Pet(name,type,age)
print(f"Le nom de l'animal est : {P.get_name()} il est de type : {P.get_animalType()} et il a {P.get_age()} ans !!!")



      