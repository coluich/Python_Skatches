import os
import random
os.system("cls")

wire = {"r":None, "g":None, "b":None}

def bomb(biscotto):

    '''
    Funzione che simula il funzionamento di una bomba:
        - imposta valori casuali ai 3 cavi 
            - 2 cavi portano alla detonazioe della bomba ["Bomb"]
            - il restanto 1 cavo disinnesca la bomba ["Ok]
            - uno di quest 3 cavi viene scelto ["Chosed"]
        - elimina il cavo che portava alla d. della bomba e NON scelto ["Bomb", None]
        - in base alla variabile "biscotto" effettua o meno lo scambio di scelta dei cavi
          e poi verifica se il cavo scelto ha portato all'esplosione della BOMBA ['bomb', 'Chosed']
          concludendo la funzione returnando il risultato "save" oppure "dead"
    
    '''

    global wire
    wire = {"r":None, "g":None, "b":None}

    # scelte casuali dei cavi
    # con criteri vedi qui sotto
    BOMBwire1 = random.randint(0,2)
    BOMBwire2 = random.choice([x for x in range(3) if x != BOMBwire1])
    OKwire = random.choice([x for x in range(3) if x != BOMBwire1 and x != BOMBwire2])
    CHOSEDwire = random.randint(0,2)

    # assegnazioni valori casuali alle variabili
    wire[list(wire.keys())[BOMBwire1]] = ['Bomb', None]
    wire[list(wire.keys())[BOMBwire2]] = ['Bomb', None]
    wire[list(wire.keys())[OKwire]] = ['Ok', None]
    wire[list(wire.keys())[CHOSEDwire]][1] = 'Chosed'
    
    # rimuove il cavo detonante e non scelto ["Bomb", None]
    for chiave, valore in list(wire.items()):
        if valore==['Bomb', None] or valore==[None, 'Bomb']:
            # print(f'Wire {chiave} exploded!')
            del wire[chiave]
            break

    if biscotto == "Change":
        # esegue la scelta
        wire[list(wire.keys())[0]][1], wire[list(wire.keys())[1]][1] = wire[list(wire.keys())[1]][1], wire[list(wire.keys())[0]][1]
        
        # verifica il cavo scelto
        for i in wire.values():
            if 'Ok' in i and 'Chosed' in i:
                return "save"
            if 'Bomb' in i and 'Chosed' in i:
                return "dead"
    


        return wire[list(wire.keys())[0]][1], wire[list(wire.keys())[1]][1] 
        
    if biscotto == "NotChange":
        for i in wire.values():
            if 'Ok' in i and 'Chosed' in i:
                return "save"
            if 'Bomb' in i and 'Chosed' in i:
                return "dead"

SaveWithChange = 0

for i in range(100):
    if bomb("Change") == "save":
        SaveWithChange += 1

SaveWithOutChange = 100 - SaveWithChange


print(f'''

SaveWithChange: {SaveWithChange}%

SaveWithOutChange: {SaveWithOutChange}%

In conclusione si hanno più probabilità di salvarsi effettuando 
il cambio di cavo. Approssimativamente, ci sono 2/3 (75%) di 
possibilità di sopravvivere effettuando il cambio di cavo e 
1/3 (25%) di possibilità di sopravvivere senza effettuare lo 
scambio di cavo.
''')