print("============ Debut ================")
nbre1=int(input("Donner le nombre de depart : "))
def fact(nbre) :
    if nbre==0 or nbre==1 :
        return 1
    else :
        return  nbre*fact(nbre-1)
result=fact(nbre1)
print("Voici le factorielle de {}! : {} ".format(nbre1,result))
print("============ Fin ================")
