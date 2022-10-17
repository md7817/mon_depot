import random 

print("================= Debut =================\n pi-> pierre , pa -> Papier , ci -> cisseaux !")
dict =["Pierre", "Cisseaux",  "Papier"]
pc = random.choice(dict)
user= input("Fait ton choix >> ")
if pc=="Pierre" :
    if user == "pa ":
        print("Bravo papier couvre la pierre !!!")
    elif user =="ci" :
        print("Desole la pierre detruit le cisseaux vous etes perdu !!!")
    elif user == "pi" :
        print("Egalite !!!")
    else :
        print("Veuillez svp faites un choix entre pi , pa ,ci")

elif pc=="Cisseaux" :
    if user == "pa ":
        print("Desole le papier est coupe par le ciseaux !!!")
    elif user =="pi" :
        print("Bravo la pierre detruit le cisseaux !!!")
    elif user == "ci" :
        print("Egalite !!!")
    else :
        print("Veuillez svp faites un choix entre pi , pa ,ci")

else :
    if user == "pa ":
        print("Desole le papier est coupe par le ciseaux !!!")
    elif user =="pi" :
        print("Bravo la pierre detruit le cisseaux !!!")
    elif user == "pa" :
        print("Egalite !!!")
    else :
        print("Veuillez svp faites un choix entre pi , pa ,ci")

print("================== FIN ==================")
