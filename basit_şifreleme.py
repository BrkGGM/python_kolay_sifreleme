import os 
alfabe =[" ","a","A","b","B","c","C","ç","Ç","d","D","e","E","f","F","g","G","ğ","Ğ","h","H","ı","I","i","İ","j","J","k","K","l","L","m","M","n","N","o","O","ö","Ö","p","P","r","R","s","S","ş","Ş","t","T","u","U","ü","Ü","v","V","y","Y","z","Z","w","W","q","Q","x","X","1","2","3","4","5","6","7","8","9","0",".",",",":",";","*","(",")","!","'","^","+","%","&","/","=","?","-","|","_","#","~","{","}","[","]",'"']

#not akıl sağlığımı yitirmemek için uyuyicam sabah'a da unutma encrypt işlemi başarılı decrypt'i hallediceksin yaparsın hadi


def number2binary(sayi,key):
    global binary_yazi 
    binary_yazi = ""
    sayi += key
    while(len(binary_yazi) < 11):
        binary_yazi += str(sayi % 2)
        sayi = sayi // 2
    binary_yazi = binary_yazi[::-1]
    


def binary2number(binary,key):
    binary = binary[::-1]
    list_binary = ([*binary])
    i = len(list_binary)
    global toplam_sayi 
    toplam_sayi = 0
    for i in range(i):
#        print ("i:", i)
        if int(list_binary[i]) == 0:
            pass
            
        else:
#            print("listbinari : ", list_binary[i])
            toplam_sayi += 2**i
#            print(toplam_sayi)
    toplam_sayi = toplam_sayi - key
    
    





def encrypt(yazi,key):
    list_yazi = ([*yazi])
    global encrypted_yazi
    encrypted_yazi = ""
    i = len(list_yazi)
    for i in range(i):
        alfabe_sira = alfabe.index(list_yazi[i])
        number2binary(alfabe_sira,key)
        encrypted_yazi += binary_yazi
        encrypted_yazi += " "


def decrypt(yazi,key):
    list_yazi = yazi.split()
    global decrypted_yazi
    decrypted_yazi = ""
    i = len(list_yazi)
    for i in range(i):
        binary2number(list_yazi[i],key)
        harf = alfabe[toplam_sayi]
        decrypted_yazi += harf


input("""
    ###############################################
    #           Süper Binary Şifreleme            #
    #                                             #
    #                                by BurakGGM  #
    ###############################################


    Devam etmek için ENTER'a basınız
    """)

while(True):
    

    os.system("cls")

    sec = input("""
    | 
    | Şifrelemek için 1
    | Deşifrelemek için 2
    | Çıkmak için 99'a
    | Basıp ENTER'a basınız
    |

    >> """)

    if int(sec) == 1:
        os.system("cls")
        sifrelencek_yazi = input("""
    |
    | 
    | Şifrelemek istediğiniz yazıyı giriniz ve ENTER'a basınız
    | 
    | Sonra da Anahtarı (1-923 arası bir sayı) girip enter'a basınız
    |

    Not: abidik bubidik karakterler kullanmayın Örnek :'$' , '“' tarzı karakterler kullanmayın hata verir

    >> """)
        key = int(input("    >>"))
        encrypt(sifrelencek_yazi,key)
        print(f"""
    Şifrelenmiş yazınız hazır
########################################################
{encrypted_yazi}
########################################################
    """)
        print("Menüye dönmek için ENTER'a basınız")
    


    elif int(sec) == 2:
        os.system("cls")
        sifrelencek_yazi = input("""
    |
    | 
    | Deşifrelemek istediğiniz yazıyı giriniz ve ENTER'a basınız
    | 
    | Sonra da Anahtarı (1-923 arası bir sayı) girip enter'a basınız
    |

    >> """)
        key = int(input("    >>"))
        decrypt(sifrelencek_yazi,key)
        print(f"""
Şifrelenmiş yazınız hazır
########################################################
{decrypted_yazi}
########################################################
    """)
        print("Menüye dönmek için ENTER'a basınız")

    elif int(sec) == 99:
        break
    else:
        print("HATA : Lütfen 1 ya da 2'den farklı bir karakter girmeyiniz")

    input()