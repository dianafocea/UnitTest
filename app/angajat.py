class Angajat():
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.tichete = 500 #am adaugat un atribut ajutator pentru a testa functionalitatea metodelor

    def nume_complet(self):
        return f'{self.nume} {self.prenume}'

    def salariu_lunar(self):
        return self.salariu + self.tichete

    def salariu_anual(self):
        return self.salariu_lunar() * 12

    def marire_salariu(self, proc):
        self.salariu = self.salariu + (self.salariu * proc / 100)
        print(f"Salariul marit cu {proc}%: {self.salariu} lei")
        return self.salariu

    def descriere(self):
        return(f"Angajat: {self.nume_complet()}, salariu_baza: {self.salariu} lei, "
              f"salariu_lunar: {self.salariu_lunar()}, salariu_anual: {self.salariu_anual()}")