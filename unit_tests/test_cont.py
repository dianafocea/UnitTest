from app.cont import Cont


class TestCont:

    def setup_method(self):
        print("Se executa la inceput")
        self.cont = Cont('RO123456', 'Mitrescu Mircea', 50000)


    def teardown_method(self):
        print("Se executa la final")


    def test_afisare_sold(self):
        assert self.cont.afisare_sold() == "Titularul `Mitrescu Mircea` are in contul RO123456 " \
        "suma de 50000 £", 'Eroare afisare_sold'

    def test_creditare_cont(self):
        assert self.cont.creditare_cont(1000) == "Ati adaugat 1000 £, sold disponibil: 51000 £",\
        'Error, nu s-a putut credita suma'

    def test_debitare_cont(self):
        assert self.cont.debitare_cont(8000) == "Ati retras 8000 £, sold disponibil: 42000 £",\
        'Error, fonduri insuficiente'

