class Cont():
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        return (f'Titularul `{self.titular_cont}` are in contul {self.iban} suma de {self.sold} £')

    def creditare_cont(self, suma):
        self.sold += suma
        return (f"Ati adaugat {suma} £, sold disponibil: {self.sold} £")

    def debitare_cont(self, suma):
        if suma > 0:
            if self.sold > 0:
                if self.sold >= suma:
                    self.sold -= suma
                    return (f"Ati retras {suma} £, sold disponibil: {self.sold} £")
                else:
                    return (f"Nu aveti minim {suma} £ in cont!")
            else:
                return ("Sold 0, nu puteti retrage bani!")
        else:
            return ("Fonduri insuficiente!")