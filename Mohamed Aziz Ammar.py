def saisir():
    global n
    test=False
    while test==False:
        n=int(input("n="))
        test=4<=n<=20
def remplir (t,n):
    for i in range (n):
        test=False
        while test==False:
            t[i]=float(input("t["+str(i)+"]="))
            test=(1<=t[i]<=10)and(t[i]%10!=t[i]//10)
def tri(t,n):
    test=False
    while test==False:
        echange=False
        for i in range (n-1):
            if(t[i]<t[i+1]):
                aux=t[i]
                t[i]=t[i+1]
                t[i+1]=aux
                echange=True
        n-=1
        test=(echange==False)or(n==1)
def afficher(t,n):
    for i in range(n):
        print(t[i],end="|")
def ver(t,n):
    h=0
    m=n-1
    s=0
    e=0
    while h<m :
        if(t[h]+t[m])>10:
            s=t[h]+t[m];e=e+1
            print("\nla somme t["+str(h)+"]"+"+"+"t["+str(m)+"]"+"="+str(t[h])+"+"+str(t[m])+"="+str(s)+">10 donc camion N"+str(e)+" a un seul conteneur("+str(t[h])+")tonnes")
            h=h+1
        else:
            s=t[h]+t[m];e=e+1
            print("\nla somme t["+str(h)+"]"+"+"+"t["+str(m)+"]"+"="+str(t[h])+"+"+str(t[m])+"="+str(s)+"<=10 donc camion N"+str(e)+" a conteneurs double("+str(t[h])+","+str(t[m])+")tonnes")
            h=h+1;m=m-1
    print("\nle nombre de camions a louer est:",e)
























#pp
import numpy as np
saisir()
t=np.array([float]*n)
remplir(t,n)
tri(t,n)
afficher(t,n)
verif(t,n)
