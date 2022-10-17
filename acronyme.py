#encoding utf-8
print("================= Debut =================")
chaine = (input("Donner une chaine de caractere : "))
mots = chaine.split(" ")
print(mots)
acronyme = " "
for mot in mots :
    acronyme = acronyme + str(mot[0].upper())

print(f" Voici l'acronyme de {chaine} : {acronyme}")
print("================== FIN ==================")
