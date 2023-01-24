from math import pi

class Cerc():
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def arie_cerc(self):
        return pi * (self.raza ** 2)

    def diametru_cerc(self):
        return self.raza * 2

    def circumferinta_cerc(self):
        return 2 * pi * self.raza

    def descriere_cerc(self):
        return self.culoare, self.raza

    def descriere_metode_cerc(self):  # metoda separata pt verificarea tuturor metodelor cercului
        return (f"Aria cercului = {self.arie_cerc()}, diametrul = {self.diametru_cerc()},"
                f" circumferinta = {self.circumferinta_cerc()}")