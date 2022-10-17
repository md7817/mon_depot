import subprocess
import os
from tkinter import TRUE
print("Merci mon createur Moussa Diarra") 
terminal=TRUE
while terminal :
    command = input(os.getcwd()+":> ")
    split_command=command.split(" ")
    if split_command[0]=="cd" and len(split_command)==2 :
        try :
            os.chdir(split_command[1])
        except FileNotFoundError:
            print(" ")
    resultat = subprocess.run(command , shell=True, capture_output=True, universal_newlines=True)
    print(resultat.stdout)
    print(resultat.stderr)
