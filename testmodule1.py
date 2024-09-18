import random
from module1 import welcome_page
nomorSlot = random.randint(1,4)

welcome_page("Selamat datang di permainan kami")

nameUser = input("siapa nama kamu : ")
while nameUser == "":
    nameUser = input("isi dulu namamu kocak : ")
    
print(f"Selamat datang Di Game Slot {nameUser} !.")

bentuk_Hoki = "$"
hoki = [bentuk_Hoki] * 4

while True :
    tempat_hoki = hoki.copy()
    tempat_hoki[nomorSlot-1] = "GACOR"
    hasil1 = ' '.join(hoki)
    hasil2 = ' '.join(tempat_hoki)
    
    print(f"Halo {nameUser} perhatikan 4 dolar di bawah ini \n {hasil1}")
    
    pilihanKu = int(input("Dolar keberapakah paling Gacor? 1/2/3/4 : "))
    while pilihanKu >= int(5):
        pilihanKu = int(input("isi antara angka 1 hingga 4 : "))
    konfirmasi = input(f"Pilihan mu adalah nomor {pilihanKu}, apakah mau melanjutkannya? [y/n]")
    
    if konfirmasi == "n":
        print("program dihentikan")
        exit()
    elif konfirmasi == "y" or konfirmasi == "Y":
        if pilihanKu == nomorSlot:
            print(f"{hasil2} \n kamu menang !!!!")
        else: 
            print(f"{hasil2} \n maaf kamuu kalahhh")
    else:
        print("silahkan Ulangi program")
    play_again = input("\n \n apakah kamu ingin bermain kembali? [y/n] : ")
    if play_again == "y" or konfirmasi == "Y":
        nomorSlot = random.randint(1, 4)  
    else : 
        print("program selesai")
        break 