print("============ Debut ================")
print("Veuillez saisir les deux nbres :")
n1=int(input("nombre 1 : "))
n2=int(input("nombre 2 : "))
s=n1+n2
p=n1*n2
su=n1-n2
d=n1/n2
opera=input("Veuillez saisir une des oprerateurs svts +,-,*,/ :")
if opera=='+' :
    print("La somme de vos deux nbres est : {}".format(s))
elif opera=='-' :
    print("La soustraction de vos deux nbres est : {}".format(su))
elif opera=='*' :
    print("La multiplication de vos deux nbres est : {}".format(p))
elif opera=='/' :
    print("La division de vos deux nbres est : {}".format(d))
print("============ Fin ================")

