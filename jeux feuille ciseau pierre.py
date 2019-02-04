x=input("quel est votre nom ? ")
print(x)
y=input("quel est votre choix Mr." + x +"?")
print(y)

def corrpds(y):
    if (y=='f'):
        result=1 
    if(y=='c'):
        result=2
    if(y=='p'):
        result=3
    return result
z=corrpds(y)
print(z)

import random
def corrps(n):
    if (n==1):
        resultat="f" 
    if(n==2):
        resultat="c"
    if(n==3):
        resultat="p"
    return resultat
a=random.randint(1,3)
res=corrps(random.randint(1,3))
print("l'ordinateur a choisit : " + res)
print(a)

def comps(a,z):
    if a==1 and z==1 :
        reslt="egalité"
    if a==2 and z==2 :
        reslt="egalité"
    if a==3 and z==3 :
        reslt="egalité"
    if a==1 and z==2 :
        reslt="vous avez gagné"
    if a==1 and z==3:
        reslt="l'ordinateur a gagné"
    if a==2 and z==1:
        reslt="l'ordinateur a gagné"
    if a==2 and z==3:
        reslt="vous avez gagné"
    if a==3 and z==1:
        reslt="vous avez gagné"
    if a==3 and z==2:
        reslt="l'ordinateur a gagnÃé"
    return reslt
print(comps(a,z))
