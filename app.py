from apps.Makanan import Makanan
from apps.Minuman import Minuman
from apps.Beli import Beli

makanan = [
    Makanan("Nasi Goreng", 10, 12000),
    Makanan("Mie Goreng", 12, 13000)
]

minuman = [

    Minuman("Jus", 10, 3000, "Jeruk"),
    Minuman("Coffe", 10, 3000, "Mocachino")
]

pembeli = []

def Menu():
    i = 0
    y = "y"
    while y == "y":
        i += 1 
        nama = str(input("Masukan Nama Anda : "))
        uang = int(input("Masukan Jumlah Uang Anda : "))
        jumlah = int(input("Masukan Jumlah Pesanan : "))
        level = int(input("Masukan Level kepedasan : "))
        for i,x in enumerate(makanan):
            print (f"{i+1}.{x.getName()} Rp.{x.getPrice()}")

        pilih = int(input("Silahkan Pilih Menu : "))

        if pilih == 1:
            menu = makanan[0]
        elif pilih == 2:
            menu = makanan[1]

        i.Beli(nama, uang)
        i.buyFood(menu, jumlah, level)
        pembeli.append(i)
        y = input("Masuk : ")
        

    

Menu()
