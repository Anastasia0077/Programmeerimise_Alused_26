#Lihtne If Lause 
# try:
#     x = int(input("Sisesta arv: "))
#     if x > 0:
#         print("Positiivne arv")
#         print("See rida on ka if-i sees"))
#     print("See rida täidetakse alati") 
# except ValueError: 
#     print("Valed andmed")

#2.3 if...else lause
# if tingimus:
#     tegevus_True
# else:
#     tegevus_False
# try: 
#     x = int(input("Sisesta arv: "))
#     if x == 1:
#         print("Õige")
#     else:
#         print("Vale")
# except ValueError:
#     print("Valed andmed")

# vastus = input("Kas soovid jätkata? (jah/ei) ")
# if vastus.lower() == "jah":
#     print("Jätkame!")
# else:
#     print("Head aega!")

# x = int(input("Sisesta arv -5 kuni 5: "))
# if x < -5:
#     print("Vähe")
# elif -5 <= x <= 5:
#     print("OK")
# else:
#     print("Palju")

#2.5 if lause sees if lause
#muuda koodi nii, et kastajalt küsime vanust, kui nimi on sobib

# try:
#     vanus = int(input("Vanus: "))
#     if vanus >= 18:
#         juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
#         if juhiluba.lower() == "jah":
#             print("Võid autot juhtida.")
#         else:
#             print("Kõigepealt tee juhiload.")
#     else:
#         print("Oled autojuhtimiseks liiga noor.")
# except ValueError:
#     print("Valed andmed. Sisesta täisarv.")

#2.6 
try:
    nimi = input("Sisesta nimi: ")
    if nimi.isalpha():
        print("Nimi sobib.")
        vanus = int (input("Vanus: "))
        if vanus >= 18:
            juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võib autot juhtida.")
            else:
                print("Kõigepealt tee juhiload.")
        else:
            print("Oled autojuhtimiseks liiga noor.")
    else: 
        print("Nimes tohib olla ainult tähti!")

except ValueError:
    print("Valed andmed. Sisesta täisarv")
print("Ainult tähed:", nimi.isalpha())


# print("Suurtähtedega:", nimi.isupper())
# print("Algab suurtähega:", nimi.istitle())
# if nimi.isalpha():
#     print("Nimi sobib.")
# else:
#     print("Nimes tohib olla ainult tähti!")