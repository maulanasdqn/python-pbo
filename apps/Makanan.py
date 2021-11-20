from apps.Product import Product

class Makanan(Product):
    def __init__(self,name, qty, price, pedas = 0):
        super().__init__(name, qty, price)
        self.__pedas = 0

    def setPedas(self, pedas):
        self.__pedas = pedas

    def infoProduct(self):
        print (f"Nama : {self.getName()}\nHarga : Rp.{self.getPrice()}\nLevel Pedas : {self.__pedas}")

    


