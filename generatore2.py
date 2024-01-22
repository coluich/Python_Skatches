import random
import os
os.system("cls")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

val = int(input("\nInserisci un valore:\n->"))*10
for i in range(0,val):
    a, b = random.randint(0,27), random.randint(0,27)
    num[a], num[b] = num[b], num[a]
    os.system("cls")
    print(str(int(((i+1)*100)/val))+"%")
print(num)