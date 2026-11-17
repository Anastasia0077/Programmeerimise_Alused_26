# pinginaabrid=["Mati","Kati"]
# nimi1=input("Sisesta nimi: ")
# nimi2=input("Sisesta nimi: ")
# if nimi1.isalpha() and nimi2.isalpha():
#     print(f"Tere {nimi1.capitalize()} ja {nimi2.capitalize()}")
#     nimi1=nimi1.capitalize()
#     if nimi1 in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#         print(f"{nimi1} ja {nimi2} on pinginaabrid")
#     else:
#         print("Nad ei ole pinginaabrid")

# else:
#     print("Viga: nimed on valesti sisestatud! Kasuta ainult tähed")

# 3.Remont
# Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav, küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi? Professionaali puhul küsi ka töö hind ruutmeetri kohta ja arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()

try:
    pikkus=float(input("Sisesta pikkus: "))
    laius=float(input("Sisesta laius: "))
    pindala=round(pikkus*laius,2) #ümardamine
    print(f"Pindala on {pindala}")
    remont=input("Kas soovid remonti teha? (jah/ei)").lower() #tähed on väikesed 
    if remont=="jah":
        print("Teeme remonti!")
        try:
            rm_hind=float(input("Sisesta ruutmetri hind: "))
            hind=round(pindala*rm_hind,2)
            print(f"Põranda vahetamise hind on {hind} €")
            ise=input("Kas teeb remondi is?(jah/ei)").lower()
            if ise=="jah":
                print(f"Põranda vahetamise hind on {hind} €")
            else:
                try: 
                    töö_hind=float(input("Töö hind: "))
                    koguhind=round(hind+pindala*töö_hind,2)
                    print(f"Remondi koguhind koos tööga on {koguhind}")
                except ValueError:
                    print("Tööhind on ujukomarv")
        except ValueError:
            print("Viga: ruutmeetri hind on arv")
    else:
        print("Remonti ei tehta!")
except ValueError:
    print("Viga: kasuta numbreid pikkuse ja laiuse sisestamiseks")
