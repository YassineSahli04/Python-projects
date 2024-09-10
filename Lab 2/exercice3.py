#NAME: Yassine Sahli
#Student Number: 300383586
def notefinale(devoirsMoyenne, partiel, examen):
    note = devoirsMoyenne*0.25 + partiel*0.25 + examen*0.5
    return note
note_finale = notefinale(86, 97,79)
print(f"Voici votre note finale: {note_finale}" )
    
