from apps.Makanan import Makanan
from os import system
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

keranjang = []

def Pembeli():
    print("1.Beli\n2.Lihat Pesanan\n3.Bayar\n4.Keluar")
    pilih = int(input("Silahkan Pilih Menu : "))

    if pilih == 1:
        buyFood()
        Pembeli()
        system.clear()

    elif pilih == 2:
        print (f"Anda membeli : {keranjang[0].getName()}")
        h = input ("Enter untuk kembali")
        Pembeli()
        system.clear()

    elif pilih == 3:
        pass

    elif pilih == 4:
        auth()


def auth():
    peran = str(input("Silahkan pilih peran anda : "))
    if peran == 1:
        print("Anda masuk sebagai Penjual")
    elif peran == 2:
        print("Anda masuk sebagai Pembeli")

def buyFood():
    i = 0
    y = "y"
    while y == "y":

        warning = "Mohon hanya input angka saja"

        i =+ 1 
        nama = str(input("Masukan Nama Anda : "))

        try:
            uang = int(input("Masukan Jumlah Uang Anda : "))

        except:
            print(warning)
            uang = int(input("Masukan Jumlah Uang Anda : "))

        for i, x in enumerate(makanan):
            print (f"{i+1}.{x.getName()} Rp.{x.getPrice()}")

        try:
            pilih = int(input("Silahkan Pilih Menu (Input hanya angka saja) : "))
        except:
            print(warning)
            pilih = int(input("Silahkan Pilih Menu (Input hanya angka saja) : "))
        
        opt = pilih - 1
        menu = makanan[opt]
        keranjang.append(menu)
        
        try:
            jumlah = int(input("Masukan Jumlah Pesanan : "))
        except:
            print(warning)
            jumlah = int(input("Masukan Jumlah Pesanan : "))
        
        print("1.Tidak Pedas\n2.Pedas Lumayan\n3.Sangat Pedas\n4.Extra Pedas")

        try:
            level = int(input("Masukan Level Kepedasan : "))
            while level < 1 or level > 4:
                print("Mohon Masukan angka dari 1 sampai 4 saja!")
                level = int(input("Masukan Level Kepedasan : "))
        except:
            level = int(input("Masukan Level Kepedasan : "))
            while level < 1 or level > 4:
                print("Mohon Masukan angka dari 1 sampai 4 saja!")
                level = int(input("Masukan Level Kepedasan : "))

        i = Beli(nama, uang)
        i.buyFood(menu, jumlah, level)
        i.setInfoBuyerFood(nama, menu, jumlah, level)
        pembeli.append(i)
        y = input("Masuk : ")

Pembeli()
