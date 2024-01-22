import os
num = ["0","1","2","3","4","5","6","7","8","9"]
cs = ["!","$","@","#"]
key = ["Pietro","Peter","Pietrolino","Pierluigi","Pigi","Gabriella","Gabry","Gabri","Tokyo","Tokio","Tocio"]

psw_non_finita=[]
password=[]

for a in cs:
    for b in key:
        psw_non_finita += [a+b.lower()]
        psw_non_finita += [a+b]

os.system("del password.txt")

for c in psw_non_finita:
    for d in range(0,11):
        password_finita = c + str(d)
        password.append(password_finita)
        # print(password_finita)

        os.system(f"echo {password_finita}>>password.txt")

print("Finish")