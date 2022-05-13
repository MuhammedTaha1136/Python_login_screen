ad = str(input("Adınızı Giriniz :"))
parola = str(input("Parolanızı Giriniz :")) 

if ad == "muhammed taha" :
    if parola == "1234" :
        print("HOŞGELDİNİZ")
        print("-----------")
    else :
        print("hatalı parola")
        hatalı = input("parolanızımı unuttunuz ? :")

        if hatalı == "evet" :
            print("-------- parolanızı değiştirmek için yazdığınız kodu kontrol ediniz --------")
            parola_degistir = input("parola değiştir :")
            print("parolanız başarıyla değişti.")
            
            

        elif hatalı == "hayır" :
            print("parolanızı kontrol edip tekrar giriniz.")
else :
    print("hatalı isim")






    



