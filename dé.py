# encoding utf-8
import random 
print("================= Debut =================")
print("Lancement du dé 1-> lancer 0 -> quitter !")
status = True
while status :
    user=int(input(">> "))
    if user==1 :
        print(random.randint(1,20))
        print("Bravo !!!")
        break
    elif user ==0 :
        status =False

print("================== FIN ==================")
