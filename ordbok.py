ordbok = {"melk": 14.90, "brød": 24.90, "yoghurt": 12.90, "pizza":39.90}
print(ordbok)
varenavn1 = input("Skriv et varenavn: ")
pris1 = float(input("Skriv prisen til varenavnet: "))
varenavn2 = input("Skriv et varenavn: ")
pris2 = float(input("Skriv prisen til varenavnet: "))
ordbok[varenavn1]=pris1
ordbok[varenavn2]=pris2



telefonbok = {"Arne": 22334455, 
              "Lisa": 95959595, 
              "Jonas": 97959795, 
              "Peder": 12345678}
navn = input("Skriv et navn: ")
if navn in telefonbok:
    nummer = telefonbok[navn] 
else:
    nummer = input("Hva er telefonnummeret til " + navn + "?") 
    nummer = int(nummer)
    telefonbok[navn]=nummer
fakta = {"Norge": {"Hovedstaden": "Oslo", "Språk": "Norsk", "Innbyggere": 12345678}, 
         "Spania": {"Hovedstaden": "Madrid", "Språk": "Spansk", "Innbyggere": 234567888},
         "Sverige": {"Hovedstaden": "Stockholm", "Språk": "Svensk", "Innbyggere": 378394901}}
land=input("Gi et land navn: ")

if land in fakta:
    print("Hovedstaden til " + land + " er " + fakta[land]["Hovedstaden"] )
    print("I", land, "snakker folk", fakta[land]["Språk"] )
    print(land, "har", fakta[land]["Innbyggere"], "innbygger.")
else: 
    print("Jeg kjenner ikke dette landet.")

flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"], 
               "sverige" : ["blått", "gult"],
               "danmark" : ["rødt", "hvitt"],
               "finland" : ["hvitt", "blått"],
               "japan" : ["rødt", "hvitt"],
               "gabon" : ["grønt", "gult", "blått"],
               "storbritannia" : ["rødt", "blått", "hvitt"],
               "chile" : ["blått", "hvitt", "rødt"]}
print(flaggOrdbok)
flaggOrdbok["tyrkia"]=["rødt", "hvitt"]
def skrivut_farge():
    land=input("Skriv hvilke landets farge du vil skrive ut: ")
    if land.lower() in flaggOrdbok:
        print(flaggOrdbok[land])


