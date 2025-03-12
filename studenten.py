import json

studenten =[]

print("Welkom bij studenteninvoersysteem")
print("")

while True:
    naam = input("Geef de naam van de student: ")
    leeftijd = int(input("Voer de leeftijd in: "))
    vaakgebied = input("Voer het vaakgebied in: ")
    cijfer = float(input("Voer het cijfer in: "))

    studenten.append({"naam" : naam,
                      "leeftijd" : leeftijd,
                      "vaakgebied" : vaakgebied,
                      "cijfer" : cijfer})
    
    meer = input("Wil je nog een student toevoegen? (ja/nee): ").strip().lower()
    if meer != "ja":
        break
    
    with open("studenten.json", "w") as file:
        json.dump(studenten, file, indent = 4)

