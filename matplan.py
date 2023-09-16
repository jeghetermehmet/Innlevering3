måltider = {"Andreas": ["Brød", "Egg", "Pølser"], "Joseph": ["Melk", "Kjøtt", "Salat"], "Ole": ["Sushi:)", "Ost", "Brød"]}
for måltid in måltider: 
        print(måltid)
def sjekker_navn():
    navn = input("Hva het du: ")
    if navn in måltider:
          print(måltider[navn])
    if navn not in måltider:
          print("Navnet ditt er ikke registert!")
sjekker_navn()