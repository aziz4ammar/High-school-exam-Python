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
def verifier(t,n):
    pd=0
    pf=n-1
    s=0
    camion=0
    while pd<pf :
        if(t[pd]+t[pf])>10:
            s=t[pd]+t[pf];camion=camion+1
            print("\nla somme t["+str(pd)+"]"+"+"+"t["+str(pf)+"]"+"="+str(t[pd])+"+"+str(t[pf])+"="+str(s)+">10 donc camion N"+str(camion)+" a un seul conteneur("+str(t[pd])+")tonnes")
            pd=pd+1
        else:
            s=t[pd]+t[pf];camion=camion+1
            print("\nla somme t["+str(pd)+"]"+"+"+"t["+str(pf)+"]"+"="+str(t[pd])+"+"+str(t[pf])+"="+str(s)+"<=10 donc camion N"+str(camion)+" a conteneurs double("+str(t[pd])+","+str(t[pf])+")tonnes")
            pd=pd+1;pf=pf-1
    print("\nle nombre de camions a louer est:",camion)
























#pp
import numpy as np
saisir()
t=np.array([float]*n)
remplir(t,n)
tri(t,n)
afficher(t,n)
verifier(t,n)
