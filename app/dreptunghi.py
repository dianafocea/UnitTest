
class Dreptunghi():
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def perimetru_dreptunghi(self):
        return self.lungime + self.latime

    def descriere1_dreptunghi(self):
        return self.lungime, self.latime, self.culoare

    def descriere2_dreptunghi(self):
        return (f"Dreptunghiul are lungimea = {self.lungime}, latimea = {self.latime}, "
              f"culoarea = {self.culoare} ")

