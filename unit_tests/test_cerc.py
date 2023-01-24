from math import pi

from app.cerc import Cerc


class TestCerc:

    def setup_method(self):
        print('This is executed first')
        self.cerc = Cerc(4, 'red')

    def teardown_method(self):
        print('Method is executed at the end')


    def test_arie_cerc(self):
        assert self.cerc.arie_cerc() == pi * 16, 'Error, aria nu functioneaza corect'

    def test_diametru_cerc(self):
        assert self.cerc.diametru_cerc() == 8, 'Error, diametrul nu functioneaza corect'

    def test_circumferinta_cerc(self):
        assert self.cerc.circumferinta_cerc() == pi * 8, 'Error, circumferinta nu functioneaza corect'

    def test_descriere_cerc(self):
        assert self.cerc.descriere_cerc() == ('red', 4), 'Error, descrierea nu functioneaza corect'

    def test_descriere_metode_cerc(self):
        assert self.cerc.descriere_metode_cerc() == f'Aria cercului = {pi * 16},' \
        f' diametrul = 8, circumferinta = {pi * 8}', 'Error, descrierea metodelor nu functioneaza corect'

