print("============ Debut ================")
print("Veuillez saisir les trois notes :")
n1=int(input("nombre 1 : "))
if n1<0 or n1 >20 :
    print("le premier n'est pas borné ")
    n1=int(input("veuillez reprendre svp : "))
n2=int(input("nombre 2 : "))
if n2<0 or  n2 >20 :
    print("le second nombre n'est pas borné ")
    n2=int(input("veuillez reprendre svp : "))
n3=int(input("nombre 3 : "))
if n3<0 or  n3 >20 :
    print("le trio nombre n'est pas borné ")
    n3=int(input("veuillez reprendre svp : "))
m=(n1+n2+n3)/(3)
if m>=16 :
    print(" Moyenne {}\n Mention : Très Bien !!!".format(m))
elif 14 <= m  < 16 :
    print(" Moyenne {} \n Mention : Bien !!!".format(m))
elif  12 <= m < 14 :
    print("Moyenne {} \n Mention : Assez Bien !!!".format(m))
elif  10 <=  m < 12 :
    print("Moyenne {} \n Mention : Passable !!!".format(m))
elif m<10:
    print("Moyenne {} \n Mention : Insuffisant !!!".format(m))
print("============ Fin ================")

