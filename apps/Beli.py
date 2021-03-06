class Beli:

    #Abstarction
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet = wallet
        self.__item = ""
        self.__amount = ""
        self.__level = ""
        self.__isEnough = False

    #Method BuyFood
    def buyFood(self, item, amount, level = 0):
        if self.__wallet < item.getPrice() * amount:
            print ("Uang Anda tidak cukup")
            self.__isEnough = False
        else:
            self.__isEnough = True
            self.__wallet -= item.getPrice() * amount
            item.setPedas(level)
            item.sellProduct(amount)
    
    #Method BuyDrink
    def buyDrink(self, item, amount, variant = "Original"):
        self.__wallet -= item.getPrice() * amount
        item.setVariant(variant)
        item.sellProduct(amount)


    #Encapsulation Getter
    def infoWallet(self):
        return self.__wallet

    #Encapsulation Setter
    def setInfoBuyerFood(self, nama, item, amount, level):
        self.__name = nama
        self.__item = item.getName()
        self.__amount = amount
        self.__level = level
        if item.getPrice() * amount < self.__wallet:
            self.__isEnough == False
        else:
            self.__isEnough == True
    
    def infoBuyerFood(self):
        if self.__isEnough == True:
            return f"{self.__name} : {self.__item} Level Pedas {self.__level}  Jumlah {self.__amount}"
        else:
            return f"{self.__name} Uang anda tidak cukup"
