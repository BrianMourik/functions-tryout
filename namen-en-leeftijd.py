
def namenlijst():
    input_name = input("Naam: ")
    input_age = input("Leeftijd: ")
    return [input_name, input_age]
    
print("Typ Quit om te stoppen.")

naam = ["", ""]

while naam[0].lower() != "quit" and naam[1].lower() != "quit":
    naam = namenlijst()
    
    if naam[0].lower() != "quit" and naam[1].lower() != "quit":
        print("Hallo " + (naam[0]) + ", je leeftijd is " + naam[1] + " jaar.")