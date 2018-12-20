# if ve else deyimlerini len() ile kullanmak:
kullanıcıAdı = input("Kullanıcı adı girin: ")
parola       = input("Parola girin: ")
toplam_uzunluk = len(kullanıcıAdı)+len(parola)
if toplam_uzunluk > 40:
    print("Kullanıcı adı ve Parolanız 40 karakterden az olmalı.")
else:
    print("Sisteme giriş yapabilirsiniz.")
