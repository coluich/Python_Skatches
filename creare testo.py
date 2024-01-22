import os
nome=input("come ti chiami: ")
eta=input("Dimmi la tua età: ")
testo="Ciao {} \n Tu hai {} anni".format(nome,eta)
x=open("asd3.txt","w")
print(testo)
x.write(testo)
x.close()
os.system("asd3.txt")
