
# DEFINITION DES FONCTIONS


def writeAll(nombrePx, longPx, largPx, ref):
    with open(nomProjet + '.txt', 'a') as f:
        f.write("-" + nombrePx + " fois " + longPx + " x " + largPx + "mm\n")
        f.close
    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("-" + nombrePx + " fois " + longPx +
                 " x " + largPx + "mm - " + ref + "\n")
        fc.close


# INPUT
nomProjet = input("Nom du projet :\n")
dimensions = input(
    "Entrer les dimensions du meuble sous le format : hauteur;Largeur;Profondeur (en mm) :\n")
li = list(dimensions.split(";"))
epaisseurMontant = int(input("Entrer l'épaisseur des montants :\n"))
epaisseurPetit = int(input("Entrer l'épaisseur des étagères :\n"))
hauteurSocle = int(input("Entrer la hauteur du socle (0 si pas de socle):\n"))
epaisseurFond = int(input("Entrer Epaisseur du fond (0 si pas de fond):\n"))
recouvrement = int(input(
    "Taper '1' si portes et socle en recouvrement, sinon taper '0' :\n"))
nbCaisson = int(input("Entrer le nombre de caisson :\n"))

# VARIABLES
taillePxMax = 1200
hauteurTotale = int(li[0])
largeurTotale = int(li[1])
profondeurTotale = int(li[2])
if recouvrement != 0:
    profMontant = profondeurTotale - epaisseurPetit
else:
    profMontant = profondeurTotale
profondeurInt = int((profondeurTotale - epaisseurFond -
                    recouvrement * epaisseurPetit))
hauteurInterieur = (hauteurTotale - hauteurSocle - epaisseurPetit)
hauteurMontantInter = (hauteurTotale - epaisseurPetit)
largeurInt = (largeurTotale - 2 * epaisseurMontant)
nbMontant = nbCaisson - 1

# CREATION FICHIERS TXT
with open(nomProjet + '.txt', 'w') as f:
    f.write("En " + str(epaisseurMontant) + "mm d'épaisseur\n")
    f.close

with open(nomProjet + 'detail.txt', 'w') as fc:
    fc.write(nomProjet + "\nDimensions : " + str(dimensions) + "mm\n")
    fc.write("Epaisseur Montant : " + str(epaisseurMontant) +
             " mm ; Etagères : " + str(epaisseurPetit) + "mm\n")
    fc.write("Hauteur du socle : " + str(hauteurSocle) + " mm\nEpaisseur du fond : " +
             str(epaisseurFond) + " mm\nRecouvrement : " + str(recouvrement) + "\n\n")
    fc.close

writeAll(str(2), str(hauteurTotale), str(profMontant), "Montants Exterieurs")

if nbCaisson > 1:
    writeAll(str(nbMontant), str(hauteurMontantInter),
             str(profondeurInt), "Montants Interieurs")

if epaisseurPetit < epaisseurMontant:
    with open(nomProjet + '.txt', 'a') as f:
        f.write("\nEn " + str(epaisseurPetit) + "mm d'épaisseur\n")
        f.close

writeAll(str(1), str(largeurTotale), str(profMontant), "Corniche")

for i in range(nbCaisson):
    largeurcaisson = int(input("Caisson " + str(i+1) + " - Entrer la largeur (" +
                         str(largeurInt) + " mm disponible) :\n"))  # reponse < Largeur int
    porte = int(input("Caisson " + str(i) +
                " : Entrer le nombre de porte :\n"))  # reponse : 0,1 ou 2
    nbEtageres = int(input("Entrer le nombre d'étagère du caisson :\n")) + 1

    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("\nCaisson " + str(i+1) + "\nLargeur : " + str(largeurcaisson) +
                 " mm\nNombre de porte : " + str(porte) + "\nNombre d'étagères : " + str(nbEtageres) + "\n")
        fc.close

    if recouvrement != 0:
        hporte = hauteurTotale - hauteurSocle - 4
        lporte = int((largeurcaisson / porte) - (porte * 4))
        writeAll(str(porte), str(hporte), str(lporte), "Portes")
        if hauteurSocle != 0 and i < 2:
            writeAll(str(1), str((largeurTotale)),
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

    largeurInt = largeurInt - largeurcaisson - epaisseurMontant

if epaisseurFond > 0:
    largFond = largeurTotale + 20 - 2 * epaisseurMontant
    hauteurFond = hauteurInterieur + 20

    with open(nomProjet + '.txt', 'a') as f:
        f.write("\nEn " + str(epaisseurFond) + "mm d'épaisseur\n")
        f.close
    with open(nomProjet + 'detail.txt', 'a') as fc:
        fc.write("\n\nFond\n")
        fc.close
    if largFond > taillePxMax:
        largFond = largFond / 2
    writeAll(str(2), str(hauteurFond), str(largFond), "Fond")
