print("\n"*100) if __name__ == '__main__' else exit()

class Persona:

    def __init__(self, nome, cognome, età) -> None:
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def generalità(self):
        return f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}"""
 
    def cambio_generalità(self):
        scelta = input(f"""cosa vorresti cambare di {self.nome} 
        1 - Cambio nome             -- {self.nome}
        2 - Cambio cognome          -- {self.cognome}
        3 - Cambio età              -- {self.età}
        -> """)
        if scelta == "1": self.nome =       input("\nInserisci nuovo nome: ")
        if scelta == "2": self.cognome =    input("\nInserisci nuovo cognome: ")
        if scelta == "3": self.età =        input("\nInserisci nuova età: ")


class Studente(Persona):

    def __init__(self, nome, cognome, età, corso_di_studi):
        super().__init__(nome, cognome, età)
        self.corso_di_studi = corso_di_studi

    def scheda_personale(self):
        return f"""{self.generalità()}
        Profilo: studente
        corso di studio: {self.corso_di_studi}
"""
    
    def cambio_corso(self):
        self.corso_di_studi = input(f"""In che materia voresti cambiare, dello studente: {self.nome} {self.cognome}
        {self.corso_di_studi} --> """)

class Insegnante(Persona):
    
    def __init__(self, nome, cognome, età, materie_insegnate):
        super().__init__(nome, cognome, età)
        self.materie_insegnate = materie_insegnate

    def scheda_personale(self):
        return f"""{self.generalità()}
        Profilo: insegnante
        materie insegnate: {" e ".join(self.materie_insegnate)}
"""
    
    def aggiungi_materia_insegnata(self):
        scelta = input(f"""che materia vorresti aggiungere?\n       {" e ".join(self.materie_insegnate)}  +  """)
        if scelta not in self.materie_insegnate:
            self.materie_insegnate.append(scelta)
        else:
            print("Questo/a insegnante ha già questa materia")


studente1 = Studente("Pietro", "Bof", "15", "Matematica")
insegnante1 = Insegnante("Elena", "Cason", "23", ["Inglese", "scienze"])

print(studente1.scheda_personale())
print(insegnante1.scheda_personale())

