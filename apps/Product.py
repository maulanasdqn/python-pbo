class Product:
    
    __tax = 2.04
    __totalProduct = 0

    #Constructor (Abstraction)
    def __init__(self, productName, productQty, productPrice):
        self.__name = productName
        self.__qty = productQty
        self.__price = productPrice
        self.__tax = Product.__tax
        Product.__totalProduct += 1

    #Getter (Encapsulation)
    def getName(self):
        return self.__name

    #Getter (Encapsulation)
    def getPrice(self):
        return self.__price * self.__tax 

    #Polymorphism
    def getJumlah(cls):
        return cls.__totalProduct

    def getQty(self):
        return self.__qty

    #Setter (Encapsulation) / (Method Behaviour)
    def setPrice(self, price):
        self.__price = price

    #Setter (Encapsulation) / (Method Behaviour)
    def sellProduct(self, buy):
        self.__qty -= buy

    def infoProduct(self):
        return f"Nama : {self.__name}\nHarga : {self.__price}\nStok : {self.__qty}"





