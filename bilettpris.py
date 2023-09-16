def beregning_av_bilettpris():
    alder = int(input("Skriv alderen din: "))
    bilettpris = 0
    if alder <= 17:
        bilettpris = 30
    elif alder >= 63:
        bilettpris = 35
    else:
        bilettpris = 50
    print("Bilettprisen for din alder: ", bilettpris, " kroner.")
    #Det kan være lurt å inkludere en ekstra sjekk for å håndtere aldre som er mindre enn 0 eller negative verdier. 
    # I den nåværende versjonen av prosedyren vil den akseptere en negativ alder som inndata, og den vil tilordne billettprisen basert på denne negative alderen, 
    # selv om det kanskje ikke er ønskelig. 
    # Det kan legges til en sjekk for å sikre at alderen er positiv før du fortsetter med beregningen.
    

    