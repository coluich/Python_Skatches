# Dizionario di esempio
wire = { "r":['Bomb', 'Chosed'], "g":['Bomb', None], "b":['Ok', None] }

# Valore da cercare
valore_da_rimuovere = ['Bomb', None]

# Trova e rimuovi la chiave corrispondente al valore
wire = {k: v for k, v in wire.items() if v != valore_da_rimuovere}

print(wire)
