msg = "Hello, wordl!"
print(msg)


nome = input("\ncome ti chiami?\n")
if(nome == "coluich"):
    print(nome + " è un nome di merda.....")
else:
    print("\nciao " + nome)








lunghezza_nome = len(nome)
lunghezza_nome_str = str(lunghezza_nome)
print(nome + " ha " + lunghezza_nome_str + " lettere")
anno_di_nascita = input("\nIn che anno sei nato?\n")
anno_di_nascita_int = int(anno_di_nascita)

anno_corrente = input("In che anno siamo?????\n")
anno_corrente_int = int(anno_corrente)

eta = anno_corrente_int - anno_di_nascita_int
eta_str = str(eta)
print("Hai " + eta_str + " anni")
risposta = ""
while (risposta != "Chi è?"):
    print("\ntoc toc....")
    risposta = input("")
print("\nnessuno")
animali = ["0. gatto", "1. pesce", "2. cavallo", "3. cane", "4. balena", "5. gheopardo"]
animali_si = ["gatto", "pesce", "cavallo", "cane", "balena", "gheopardo"]
print("\nQualè il tuo animale preferito?\nIndicalo con un numero: ")
for animale in animali:
    print(animale)
numero_animale = int(input())
if (numero_animale < 0 or numero_animale > 5):
    print("Non hai capito un cazzo")
else:
    animale_scelto = animali_si[numero_animale]
    print("Hai scelto " + animale_scelto)
