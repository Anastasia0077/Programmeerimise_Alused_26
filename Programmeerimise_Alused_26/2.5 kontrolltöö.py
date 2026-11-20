# Loo uus projekt.
# Kopeeri antud kood failisse.
# Otsi ja paranda programmis vead.
# Lisa kommentaar, kus kirjelda, mis parandatud oli.

 
# Kood:

print("Vali programm: ")
print("1 - Kolmnurga kontroll") #puudub teine "
print("2 - Hinde arvutamine")
print("3 - Pileti hind")

Valik=input("Sisesta valik (1-3) => ")
try:
    if Valik == "1":
        print("Kolmnurga kontroll") #parandasin jutumagrid
        x = float(input("Sisesta 1. külje pikkus => "))
        y = float(input("Sisesta 2. külje pikkus => "))
        z = float(input("Sisesta 3. külje pikkus => "))
        if x <= 0 or y <= 0 or z <= 0:
            print("Vigane külje pikkus")
    a=input("Sisesta 1. külje pikkus => ")
    b=float(input("Sisesta 2. külje pikkus => ")) #puudub üks ")"
    c=float(input("Sisesta 3. külje pikkus => "))
    if a+b>c or a+c>b or b+c>a: # puudub üks ":"
        print("Kolmnurk on olemas")
        if a=b=c:
            print("Kolmnurk on võrdkülgne")
        else if a==b or b==c:
            print("Kolmnurk on võrdhaarne")
        else:
        print("Kolmnurk on erikülgne")
    else:
        print("Sellist kolmnurka ei ole olemas")
    print()
    print("Hinde arvutamine")
    punktid=int(input("Sisesta punktide arv (0-100) => "))
    if punktid<0 and punktid>100:
        print("Vigane punktide arv")
    elif punktid>=50:
        print("Hinne: 3")
    elif punktid>=75:
        print("Hinne: 4")
    elif punktid>=90:
        print("Hinne: 5")
    else:
        print("Hinne: 2")
    print()
    print("Pileti hind")
    vanus=int(input("Sisesta oma vanus => "))
    if vanus<7:
        print("Pilet on tasuta")
    elif 7<=vanus<=18 or vanus=>65:
        print("Pileti hind on 3 €")
    else: # puudub üks ":"
        print("Pileti hind on 6 €") # puudub üks ")"

# Programmi tulemus:

 
# Kolmnurga kontroll
# Sisesta 1. külje pikkus => 3
# Sisesta 2. külje pikkus => 4
# Sisesta 3. külje pikkus => 5
# Kolmnurk on olemas
# Kolmnurk on erikülgne

# Hinde arvutamine
# Sisesta punktide arv (0-100) => 82
# Hinne: 4

# Pileti hind
# Sisesta oma vanus => 70
# Pileti hind on 3 €
# Lisaülesanne:

# Muuda programmi nii, et alguses kuvatakse menüü ja kasutaja valib, millist osa käivitada:
 
# Vali programm:
# 1 - Kolmnurga kontroll
# 2 - Hinde arvutamine
# 3 - Pileti hind
# Sisesta valik (1-3) =>
# Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

# Lisa kolmnurga osasse kontroll, kas kolmnurk on täisnurkne (Pythagorase teoreem).
# Kolmnurga osa ei tohi lubada sisestada nulli või negatiivset külje pikkust.
# Lisaülesande tulemus (näide):

 
# Vali programm:
# 1 - Kolmnurga kontroll
# 2 - Hinde arvutamine
# 3 - Pileti hind
# Sisesta valik (1-3) => 1
# Kolmnurga kontroll
# Sisesta 1. külje pikkus => 3
# Sisesta 2. külje pikkus => 4
# Sisesta 3. külje pikkus => 5
# Kolmnurk on olemas
# Kolmnurk on erikülgne
# Kolmnurk on täisnurkne
# Töö esitamine

# Salvesta projekt GitHubi. Visual Studios vali Git → Create Git Repository, logi sisse oma GitHubi kontoga ja vajuta Create and Push.
# ⚠️ Eemalda linnuke kastist Private repository, sest muidu õpetaja sinu tööd ei näe.
# Kontrolli, et kood on GitHubis. Ava brauseris oma repositoorium ja veendu, et seal on sinu .py fail, mitte ainult .gitignore ja .gitattributes.
# Kopeeri link aadressiribalt. Kui repositoorium on brauseris avatud, kopeeri aadress brauseri ülevalt aadressiribalt. Näiteks:
# https://github.com/kasutajanimi/Hindeline-too
# Lisa link Moodle’isse. Vajuta selles ülesandes Lisa esitus, kleebi link tekstikasti ja vajuta Salvesta muudatused.
