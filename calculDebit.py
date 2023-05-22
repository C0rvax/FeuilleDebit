

import math


def writeAll(nombrePx, longPx, largPx, ref):
    with open(nomProjet + '.txt', 'a') as f:
        f.write("-" + nombrePx + " fois " + longPx + " x " + largPx + "mm\n")
        f.close
    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("-" + nombrePx + " fois " + longPx +
                 " x " + largPx + "mm - " + ref + "\n")
        fc.close


fond = 0
ratio = 100
hauteurSocle = 0
EpaisseurPorte = 0

nomProjet = input("Nom du projet :\n")
dimensions = input(
    "Entrer les dimensions du meuble sous le format : hauteur;Largeur;Profondeur (en mm) :\n")
li = list(dimensions.split(";"))
hauteurTotale = int(li[0])
LargeurTotale = int(li[1])
profondeurTotale = int(li[2])

EpaisseurMontant = int(input("Entrer l'épaisseur des montants :\n"))
EpaisseurEtagere = int(input("Entrer l'épaisseur des étagères :\n"))
hauteurSocle = int(input("Entrer la hauteur du socle (0 si pas de socle):\n"))
hauteurInterieur = (hauteurTotale - hauteurSocle - EpaisseurEtagere)
hauteurMontantInter = (hauteurTotale - EpaisseurEtagere)
LargeurInt = (LargeurTotale - 2 * EpaisseurMontant)
fond = int(input("Entrer Epaisseur du fond :\n"))
Portes = int(input("Entrer le nombre de portes :\n"))
if Portes != 0:
    recouvrement = input("Portes en recouvrement ? Taper O/N :\n")
    if recouvrement in ("o", "O"):
        EpaisseurPorte = EpaisseurEtagere
profondeurInt = int((profondeurTotale - fond - EpaisseurPorte))

NbMontants = int(input("Nombre de montants supplémentaire :\n"))
if NbMontants != 0:
    ratio = input(
        "Entrer la position des montants en l'exprimant en % ( par exemple : '50;30;20' pour 2 montants) :\n")
    liRatio = list(ratio.split(";"))

Caisson = []
for i in range(NbMontants + 1):
    message = "Caisson " + \
        str(i + 1) + " - Etagère par nombre : Taper N ; Etagère par hauteur : Taper H\n"
    x = input(message)
    if x in ("N", "n"):
        nb = int(input("Entrer le nombre d'étagère du caisson :\n"))
    else:
        nb = hauteurInterieur // int(input("hauteur des étagères :\n"))
    Caisson.append(nb)

print(Caisson)

with open(nomProjet + '.txt', 'a') as f:
    f.write("En " + str(EpaisseurMontant) + "mm d'épaisseur\n")
    f.close

profMontant = int(profondeurTotale - EpaisseurPorte)
writeAll(str(2), str(hauteurTotale), str(profMontant), "Montants Exterieurs")

if NbMontants != 0:
    writeAll(str(NbMontants), str(hauteurMontantInter),
             str(profondeurInt), "Montants Interieurs")

if EpaisseurEtagere < EpaisseurMontant:
    with open(nomProjet + '.txt', 'a') as f:
        f.write("\n")
        f.write("En " + str(EpaisseurEtagere) + "mm d'épaisseur\n")
        f.close
writeAll(str(1), str(LargeurTotale), str(profMontant), "Corniche")

if Portes != 0 and EpaisseurPorte != 0:
    hporte = hauteurTotale - hauteurSocle - 4
    lporte = int((LargeurTotale / Portes) - (Portes * 4))
    writeAll(str(Portes), str(hporte), str(lporte), "Portes")
    if hauteurSocle != 0:
        writeAll(str(1), str((LargeurTotale)),
                 str(hauteurSocle), "Bandeau Socle")

if ratio == 100:
    nbEtageres = int(Caisson[0])
    if Portes != 0 and EpaisseurPorte == 0:
        hporte = hauteurInterieur - 4
        lporte = int((LargeurTotale / Portes) -
                     (Portes * 4) - (2 * EpaisseurMontant))
        writeAll(str(Portes), str(hporte), str(lporte), "Portes")

    if hauteurSocle != 0 and EpaisseurPorte == 0:
        nbEtageres += 1
        hsocle = hauteurSocle - EpaisseurEtagere
        writeAll(str(1), str((LargeurInt)), str(hsocle), "Bandeau Socle")

    writeAll(str(nbEtageres), str(LargeurInt), str(profondeurInt), "Etageres")
else:
    for i in range(len(liRatio)):

        largeurcaisson = (LargeurInt - NbMontants *
                          EpaisseurMontant) * int(liRatio[i]) / 100

        if Portes != 0 and EpaisseurPorte == 0:
            hporte = hauteurInterieur - 4
            lporte = largeurcaisson - 4
            writeAll(str(1), str(hporte), str(lporte), "Porte")

        if hauteurSocle != 0 and EpaisseurPorte == 0:
            writeAll(str(1), str(largeurcaisson), str(hauteurSocle), "Socle")

        writeAll(str(Caisson[i]), str(largeurcaisson),
                 str(profondeurInt), "Etagère")
