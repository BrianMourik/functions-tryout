a = int(input("Van welk getal wilt u de tafel zien? "))

def tafel(cijfer):
    print("De tafel van " + str(cijfer))
    
    for i in range(1,11):
        print(a * i)

tafel(a)