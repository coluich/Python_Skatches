class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    @classmethod
    def from_string(cls, stringa_persona, *args):
        nome, cognome, età, residenza = stringa_persona.split("-")
        return cls(nome, cognome, età, residenza, *args)
    
    @classmethod
    def occupazione(cls):
        if cls.__name__ == "Studente":
            return("Studente")
        else:
            return("Insegnante")

    def scheda_personale(self):
        scheda = f"""
        Nome: {self.nome}
        Cognome: {self.cognome}
        Età: {self.età}
        Residenza: {self.residenza}\n"""
        return scheda

    def modifica_scheda(self):
        print("""Modifica Scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza""")

        scelta = input("Cosa Desideri Modificare?")
        if scelta == "1":
            self.nome = input("Nuovo Nome --> ")
        elif scelta == "2":
            self.cognome = input("Nuovo cognome --> ")
        elif scelta == "3":
            self.età = input("Nuovo età --> ")
        elif scelta == "4":
            self.residenza = input("Nuovo residenza --> ")


class Studente(Persona):
    profilo = "Studente"

    def __init__(self, nome, cognome, età, residenza, corso_di_studio):
        super().__init__(nome, cognome, età, residenza)
        self.corso_di_studio = corso_di_studio

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Studente.profilo}
        Corso Di Studi:{self.corso_di_studio}
        ***"""
        return super().scheda_personale() + scheda

    def cambio_corso(self, corso):
        self.corso_di_studio = corso
        print("Corso Aggiornato")

class Insegnante(Persona):
    profilo = "Insegnante"

    def __init__(self, nome, cognome, età, residenza, materie=None):
        super().__init__(nome, cognome, età, residenza)
        if materie is None:
            self.materie = []
        else:
            self.materie = materie

    def scheda_personale(self):
        scheda = f"""
        Profilo:{Insegnante.profilo}
        Materie Insegnate:{self.materie}
        ***"""
        return super().scheda_personale() + scheda

    def aggiungi_materia(self, nuova):
        if nuova not in self.materie:
            self.materie.append(nuova)
        print("Elenco Materie Aggiornato")    




iron_man = "Tony-Stark-40-Torre Stark"
zuck = "Mark-Zuck-33-California"

insg1 = Insegnante.from_string(iron_man, "ingegnaria")
stud1 = Studente.from_string(zuck, "SEO")

print(insg1.scheda_personale())
print(stud1.scheda_personale())