import random
print("================= Debut =================")
pc = random.randint(1, 10)
user = int(input(("Deviner le chiffre : ")))
if pc == user :
    print(f"Bravo vous avez trouvé {pc} = {user} ")
else :
    print(f"Desolé vous avez raté {pc} =! {user} ")
print("================== FIN ==================")
