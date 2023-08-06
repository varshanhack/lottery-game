from time import sleep as sp
import sys,subprocess
while True:
 print("LOTTERY GAME")
 print("")
 sp(1)
 print("_____________")
 print("|","?","|","?","|","?","|")
 print("-------------")
 sp(1)
 print("")
 print("If the three numbers are same you will be the winner")
 sp(1)
 print("")
 a=input("Enter a name ==> ")
 import random
 n1=random.randrange(1,8)
 n2=random.randrange(1,8)
 n3=random.randrange(1,8)
 print("_____________")
 print("|",n1,"|",n2,"|",n3,"|")
 print("-------------")
 print("")
 if n1==n2==n3:
    print(a,"is a winner")
    print("")
 else:
    print(a,"is a loser")
    print("")
 input("Press enter to continue...")
 subprocess.run("cls",shell=True)
