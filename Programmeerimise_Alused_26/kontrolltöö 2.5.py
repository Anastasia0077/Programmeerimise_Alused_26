# Loo uus projekt.
# Kopeeri antud kood failisse.
# Otsi ja paranda programmis vead.
# Lisa kommentaar, kus kirjelda, mis parandatud oli.

 
# Kood:
print("Kolmnurga kontroll") # parandan "´" --> "
a=float(input("Sisesta 1. külje pikkus => ")) #lisan "float" ja üks ")"
b=float(input("Sisesta 2. külje pikkus => ")) # puudub üks ")"
c=float(input("Sisesta 3. külje pikkus => "))
if a+b>c and a+c>b and b+c>a: # parandan "or" --> "and" ja lisan ":"
    print("Kolmnurk on olemas")
    if a==b==c: # parandan "=" --> "=="
        print("Kolmnurk on võrdkülgne")
    elif a==b or b==c or a==c: # parandan "else if" --> "elif" ja lisan "a == c"
        print("Kolmnurk on võrdhaarne")
    else:
        print("Kolmnurk on erikülgne") # lisan taane
else:
    print("Sellist kolmnurka ei ole olemas")
print()
print("Hinde arvutamine")
punktid=int(input("Sisesta punktide arv (0-100) => "))
if punktid<0 or punktid>100: # parandan "and" --> "or"
    print("Vigane punktide arv")
elif punktid>=90: # parandan muudetud tingimuste järjekorda (suuremast väiksemani)
    print("Hinne: 5")
elif punktid>=75:
    print("Hinne: 4")
elif punktid>=50:
    print("Hinne: 3")
else:
    print("Hinne: 2")
print()
print("Pileti hind")
vanus=int(input("Sisesta oma vanus => "))
if vanus<7:
    print("Pilet on tasuta")
elif 7<=vanus<=18 or vanus>=65: # parandan "=>" --> ">="
    print("Pileti hind on 3 €")
else: # puudub ":"
    print("Pileti hind on 6 €") # puudub ")"
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
