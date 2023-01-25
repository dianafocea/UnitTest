from app.angajat import Angajat


class TestAngajat():

    def setup_method(self):
        print("Se executa la inceput")
        self.angajat = Angajat('Mitrescu', 'Mircea', 4500)


    def teardown_method(self):
        print("Se executa la final")


    def test_nume_complet(self):
        assert self.angajat.nume_complet() == 'Mitrescu Mircea', 'Error, numele nu corespunde'

    def test_salariu_lunar(self):
        assert self.angajat.tichete == 500, 'Error, valoarea de tichet nu corespunde'
        assert self.angajat.salariu_lunar() == 5000, 'Error, salariul lunar nu corespunde'

    def test_salariu_anual(self):
        assert self.angajat.salariu_anual() == 60000, 'Error, salariul anual nu corespunde'

    def test_marire_salariu(self):
        assert self.angajat.marire_salariu(5) == 4725.0, 'Error, marire_salariu nu functioneaza corect'

    def test_descriere(self):
        assert self.angajat.descriere() == 'Angajat: Mitrescu Mircea, salariu_baza: 4500 lei, ' \
        'salariu_lunar: 5000, salariu_anual: 60000', 'Error, descrierea nu functioneaza corect'