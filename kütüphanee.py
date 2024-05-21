menü = """
         -Python Kütüphanesine Hoş Geldiniz-
      
     1) Kitap Ver
     2) Kitap Al
     3) Tümünü Listele
     Q) Çikiş


"""
liste = list()

def kitapver(kitap: tuple, liste: list):
    liste.append(kitap)
    print("Verdiğiniz kitap için teşekkür ederiz.")

def kontrol(kitap: tuple, liste: list):
    if kitap in liste:
        return True
    else:
        return False

def kitapal(kitap: tuple, liste: list):
    if kontrol(kitap, liste):
        liste.remove(kitap)
        print("Kitabi başarila aldiniz, iyi okumalar...")
    else:
        print("İstediğiniz kitap mevcut değildir.")

def listele(liste: list):
    for a in liste:
        print("Kitap Adi :  {}    Yazar Adı: {}".format(a[1], a[0]))

while True:
    print(menü)
    secim = input("İşlem numarasini giriniz : ")

    if secim == "1":
        yazar = input("Yazar adi : ")
        kitap_adi = input("Kitap adi : ")
        kitap = (yazar, kitap_adi)
        kitapver(kitap, liste)
    elif secim == "2":
        yazar = input("Yazar adi : ")
        kitap_adi = input("Kitap adi : ")
        kitap = (yazar, kitap_adi)
        kitapal(kitap, liste)
    elif secim == "3":
        listele(liste)
    elif secim.upper() == "Q":
        print("Çikiş yapiliyor...")
        quit()
    else:
        print("Hatali seçim yaptiniz!")

    input("Ana menüye dönmek için Enter'a basiniz.")