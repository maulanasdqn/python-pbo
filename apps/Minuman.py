from apps.Product import Product

class Minuman(Product):
    def __init__(self,name, qty, price, variant):
        super().__init__(name, qty, price)
        self.__variant = variant

    def setVariant(self, variant):
        self.__variant = variant

    def infoProduct(self):
        return f"Nama : {self.getName()}\nHarga : Rp.{self.getPrice()}\nVariant : {self.__variant}"

