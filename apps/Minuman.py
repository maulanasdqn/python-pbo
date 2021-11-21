from apps.Product import Product

class Minuman(Product):

    #Abstarction (Constructor)
    def __init__(self,name, qty, price, variant):
        super().__init__(name, qty, price)
        self.__variant = variant

    #Encapsulation (Setter)
    def setVariant(self, variant):
        self.__variant = variant

    #Encapsulation (Getter)
    def infoProduct(self):
        return f"Nama : {self.getName()}\nHarga : Rp.{self.getPrice()}\nVariant : {self.__variant}"

