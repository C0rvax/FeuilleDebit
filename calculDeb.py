

import math


def writeAll(nombrePx, longPx, largPx, ref):
    with open(nomProjet + '.txt', 'a') as f:
        f.write("-" + nombrePx + " fois " + longPx + " x " + largPx + "mm\n")
        f.close
    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("-" + nombrePx + " fois " + longPx +
                 " x " + largPx + "mm - " + ref + "\n")
        fc.close


nomProjet = input("Nom du projet :\n")
dimensions = input(
    "Entrer les dimensions du meuble sous le format : hauteur;Largeur;Profondeur (en mm) :\n")
li = list(dimensions.split(";"))
hauteurTotale = int(li[0])
LargeurTotale = int(li[1])
profondeurTotale = int(li[2])

epaisseurMontant = int(input("Entrer l'épaisseur des montants :\n"))
epaisseurPetit = int(input("Entrer l'épaisseur des étagères :\n"))
hauteurSocle = int(input("Entrer la hauteur du socle (0 si pas de socle):\n"))
epaisseurFond = int(input("Entrer Epaisseur du fond (0 si pas de fond):\n"))
Recouvrement = int(input(
    "Taper '1' si portes et socle en recouvrement, sinon taper '0' :\n"))
NbCaisson = int(input("Entrer le nombre de caisson :\n"))

if Recouvrement != 0:
    profMontant = profondeurTotale - epaisseurPetit
else:
    profMontant = profondeurTotale
profondeurInt = int((profondeurTotale - epaisseurFond -
                    Recouvrement * epaisseurPetit))
hauteurInterieur = (hauteurTotale - hauteurSocle - epaisseurPetit)
hauteurMontantInter = (hauteurTotale - epaisseurPetit)
LargeurInt = (LargeurTotale - 2 * epaisseurMontant)
nbMontant = NbCaisson - 1


with open(nomProjet + '.txt', 'a') as f:
    f.write("En " + str(epaisseurMontant) + "mm d'épaisseur\n")
    f.close

with open(nomProjet + 'detail.txt', 'a') as fc:
    fc.write(nomProjet + "\nDimensions : " + str(dimensions) + "mm")
    fc.write("Epaisseur Montant : " + str(epaisseurMontant) +
             " mm ; Etagères : " + str(epaisseurPetit) + "mm")
    fc.write("Hauteur du socle : " + str(hauteurSocle) + " mm\nEpaisseur du fond : " +
             str(epaisseurFond) + " mm\nRecouvrement : " + str(Recouvrement) + "\n\n")
    fc.close

writeAll(str(2), str(hauteurTotale), str(profMontant), "Montants Exterieurs")

if NbCaisson > 1:
    writeAll(str(nbMontant), str(hauteurMontantInter),
             str(profondeurInt), "Montants Interieurs")

if epaisseurPetit < epaisseurMontant:
    with open(nomProjet + '.txt', 'a') as f:
        f.write("\n")
        f.write("En " + str(epaisseurPetit) + "mm d'épaisseur\n")
        f.close

writeAll(str(1), str(LargeurTotale), str(profMontant), "Corniche")

for i in range(NbCaisson):
    largeurcaisson = int(input("Caisson " + str(i+1) + " - Entrer la largeur (" +
                         str(LargeurInt) + " mm disponible) :\n"))  # reponse < Largeur int
    porte = int(input("Caisson " + str(i) +
                " : Entrer le nombre de porte :\n"))  # reponse : 0,1 ou 2
    nbEtageres = int(input("Entrer le nombre d'étagère du caisson :\n")) + 1

    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("\nCaisson " + str(i+1) + "\nLargeur : " + str(largeurcaisson) +
                 " mm\nNombre de porte : " + str(porte) + "\nNombre d'étagères : " + str(nbEtageres) + "\n")
        fc.close

    if Recouvrement != 0:
        hporte = hauteurTotale - hauteurSocle - 4
        lporte = int((largeurcaisson / porte) - (porte * 4))
        writeAll(str(porte), str(hporte), str(lporte), "Portes")
        if hauteurSocle != 0 and i < 2:
            writeAll(str(1), str((LargeurTotale)),
                     str(hauteurSocle), "Bandeau Socle")
    else:
        hporte = hauteurInterieur - 4
        lporte = int(largeurcaisson / porte - porte * 4)
        writeAll(str(porte), str(hporte), str(lporte), "Portes")
        if hauteurSocle != 0:
            writeAll(str(1), str((largeurcaisson)),
                     str(hauteurSocle), "Bandeau Socle")
    writeAll(str(nbEtageres), str(largeurcaisson),
             str(profondeurInt), "Etageres")

    LargeurInt = LargeurInt - largeurcaisson - epaisseurMontant
