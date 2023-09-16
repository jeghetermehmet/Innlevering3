my_list = []
my_list.append(2)
my_list.append(4)
my_list.append(1)
my_list.append(6)
print(my_list[0])
print(my_list[2])

# Opprett en tom liste
navneliste = []

# Be brukeren om å oppgi 4 navn og legg dem til i listen
for i in range(4):
    navn = input("Skriv inn et navn: ")
    navneliste.append(navn)

# Sjekk om brukeren har lagt inn navnet mitt i lista
mitt_navn = "Mehmet" 
if mitt_navn in navneliste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

ny_list= []
Produkt = 1
Summen = 0
for tall in my_list:
    Summen += tall
    Produkt *= tall
ny_list.append(Produkt)
ny_list.append(Summen)

siste_list = ny_list + my_list
siste_list.pop()
siste_list.pop()

