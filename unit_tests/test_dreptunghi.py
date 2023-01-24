from app.dreptunghi import Dreptunghi

class TestDreptunghi:

    def setup_method(self):
        print('This is executed first')
        self.dreptunghi = Dreptunghi(5, 2, 'red')

    def teardown_method(self):
        print('Method is executed at the end')

    def test_schimba_culoarea(self):
        self.dreptunghi.schimba_culoarea('green')
        assert self.dreptunghi.culoare == 'green', 'Error, schimba_culoarea nu functioneaza corect'
        assert self.dreptunghi.descriere1_dreptunghi() == (5, 2, "green"), 'Error, descrie/schimba_culoarea nu functioneaza corect'

    def test_arie_dreptunghi(self):
        assert self.dreptunghi.arie_dreptunghi() == 10, 'Error, aria nu functioneaza corect'

    def test_perimetru_dreptunghi(self):
        assert self.dreptunghi.perimetru_dreptunghi() == 7, 'Error, perimetrul nu functioneaza corect'

    def test_descriere1_dreptunghi(self):
        assert self.dreptunghi.descriere1_dreptunghi() == (5, 2, 'red'), 'Error, descrierea nu functioneaza corect'


    def test_descriere2_dreptunghi(self):
        assert self.dreptunghi.descriere2_dreptunghi() == "Dreptunghiul are lungimea = 5, " \
        "latimea = 2, culoarea = red ", 'Error, descrierea nu functioneaza corect'

