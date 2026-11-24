# 1
# Sisestatakse 15 arvu.
# M‰‰rata, mitu neist on t‰isarvud.
# for kasutades

for i in range(15):
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on t‰isarv.")
        else:
            print(f"{arv} ei ole t‰isarv.")
    except ValueError:
        print("Palun sisestage arv.")

# while kasutades
i = 0
while i < 15:
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on t‰isarv.")
        else:
            print(f"{arv} ei ole t‰isarv.")
    except ValueError:
        print("Palun sisestage arv.")
    i += 1
# while True ja break kasutades
i = 0
while True:
    try:
        arv=float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            print(f"{arv} on t‰isarv.")
        else:
            print(f"{arv} ei ole t‰isarv.")
        i += 1 # arvu lugemine, ainult siis kui sisestus on ıige
        if i==15:
            break
    except ValueError:
        print("Palun sisestage arv.")

# 2
# K¸si kasutajalt arv A ja leia kıigi naturaalarvude summa vahemikus 1 kuni A.
# for kasutades

try:
    A = int(input("Sisesta arv A: "))
    summa = 0
    for i in range(1, A + 1):
        summa += i
    print(f"Summa vahemikus 1 kuni {A} on {summa}.")
except ValueError:
    print("Palun sisestage t‰isarv.")

# 3
# Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).

korrutis=1
for i in range (8):
    try:
         arv=float(input(f"{i+1}. arv: "))
         if arv > 0:
             korrutis *= arv 
    except ValueError:
        print("Palun sisestage arv.")
print(f"Positiivsete arvude korrutis on {korrutis}.")

# 4
# Koosta programm, mis v‰ljastab ekraanile arvude ruudud vahemikus 10 kuni 20. 10^2, 11^2, 12^2, ..., 20^2

for i in range(10, 21):
    print(f"{i} ruut on {i ** 2}")
# while 
i = 10
while i <= 20:
    print(f"{i}^2 = {i**2}")
    i += 1

# 5
# Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N v‰‰rtus sisestatakse klaviatuurilt.
# ıpilased kirjutavad ise

try: 
    N = int(input("Sisesta arvude kogus N: "))
    summa = 0
    for i in range (N):
        try:
            arv = float(input(f"{i+1}. arv: "))
            if arv < 0:
                summa += arv
        except ValueError:
            print("Palun sisestage arv.")
    print(f"Negatiivsete arvude summa on {summa}.")
except ValueError:
    print("Palun sisestage t‰isarv")

# 6
# Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis m‰‰rab sisestatud arvude seast:

# negatiivsete arvude arvu,

# positiivsete arvude arvu,

# nullide arvu.
# (N v‰‰rtus sisestatakse klaviatuurilt.)

try:
    N = int(input("Sisesta arvude kogus N: "))
    negatiivsed = 0
    positiivsed = 0
    nullid = 0
    for i in range(N):
        try:
            arv = float(input(f"{i + 1}. arv: "))
            if arv < 0:
                negatiivsed += 1
            elif arv > 0:
                positiivsed += 1
            else:
                nullid += 1
        except ValueError:
            print("Palun sisestage arv.")
    print(f"Negatiivsete arvude arv: {negatiivsed}")
    print(f"Positiivsete arvude arv: {positiivsed}")
    print(f"Nullide arv: {nullid}")
except ValueError:
    print("Palun sisestage t‰isarv.")


    

