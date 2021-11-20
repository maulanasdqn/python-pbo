class Beli:
    def __init__(self, name, wallet):
        self.__name = name
        self.__wallet =  wallet

    def buyFood(self, item, amount, level = 0):
        self.__wallet -= item.getPrice() * amount
        item.setPedas(level)
        item.sellProduct(amount)
        item.infoProduct()

    def infoWallet(self):
        return self.__wallet

    def infoBuyer(self):
        return self.__name
