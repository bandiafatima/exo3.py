# nombre aléatoire 
from random import *
n = randint(0,9) 
var = input("entrer un nombre")
var = int(var)
if var == n :
 print("bravo, le nombre entré correspond a celui généré")
else :
 print("desolé, le nombre entré ne correspond pas a celui généré")


