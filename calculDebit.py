# CONSTANTES
cheminDossier = r'D:\\Code\DATA'
hauteurPxMax = 2500
largeurPxMax = 1220
epaisseurMin = 10
epaisseurMax = 100
largeurMeubleMax = 100000

# DEFINITION DES FONCTIONS


def writeAll(nombrePx, longPx, largPx, ref):
    with open(fichierFournisseur, 'a') as f:
        f.write("-" + nombrePx + " fois " + longPx + " x " + largPx + "mm\n")
        f.close
    with open(fichierDetail, 'a') as fc:
        fc.write("-" + nombrePx + " fois " + longPx +
                 " x " + largPx + "mm - " + ref + "\n")
        fc.close


def verif(phrase, min, max):
    entree = input(phrase + " =\n")
    while not entree.isdigit() or not min <= int(entree) <= max:
        entree = input(phrase + " MIN " + str(min) +
                       " ; MAX " + str(max) + " =\n")
        # while not min <= int(entree) <= max:
        #    entree = input(phrase + " :\n")
    return int(entree)


# INPUT
nomProjet = "Feuille Débit - " + input("Nom du projet :\n")
hauteurTotale = verif("Hauteur Totale (en mm)", 0, hauteurPxMax)
largeurTotale = verif("Largeur Totale (en mm)", 0, largeurMeubleMax)
profondeurTotale = verif("Profondeur Totale (en mm)", 0, largeurPxMax)
epaisseurMontant = verif(
    "Epaisseur des montants (en mm)", epaisseurMin, epaisseurMax)
epaisseurPetit = verif(
    "Epaisseur des portes et étagères (en mm)", epaisseurMin, epaisseurMax)
hauteurSocle = verif("Hauteur du socle (0 si pas de socle)", 0, hauteurTotale)
epaisseurFond = verif("Epaisseur du fond (0 si pas de fond)", 0, epaisseurMax)
recouvrement = verif(
    "Taper '1' si portes et socle en recouvrement, sinon taper '0'", 0, 1)
nbCaisson = verif("Nombre de caisson", 1, 20)

# VARIABLES
fichierFournisseur = cheminDossier + "\\" + nomProjet + '.txt'
fichierDetail = cheminDossier + "\\" + nomProjet + 'detail.txt'
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
with open(fichierFournisseur, 'w') as f:
    f.write("En " + str(epaisseurMontant) + "mm d'épaisseur\n")
    f.close

with open(fichierDetail, 'w') as fc:
    fc.write(nomProjet + "\nh" + str(hauteurTotale) + "xl" +
             str(largeurTotale) + "xp" + str(profondeurTotale) + "mm\n")
    fc.write("Epaisseur Montant : " + str(epaisseurMontant) +
             " mm ; Etagères : " + str(epaisseurPetit) + "mm\n")
    fc.write("Hauteur du socle : " + str(hauteurSocle) + " mm\nEpaisseur du fond : " +
             str(epaisseurFond) + " mm\nRecouvrement : " + str(recouvrement) + "\n\n")
    fc.close

# ECRITURE TXT
writeAll(str(2), str(hauteurTotale), str(profMontant), "Montants Exterieurs")

if nbCaisson > 1:
    writeAll(str(nbMontant), str(hauteurMontantInter),
             str(profondeurInt), "Montants Interieurs")

if epaisseurPetit < epaisseurMontant:
    with open(fichierFournisseur, 'a') as f:
        f.write("\nEn " + str(epaisseurPetit) + "mm d'épaisseur\n")
        f.close

writeAll(str(1), str(largeurTotale), str(profMontant), "Corniche")

for i in range(nbCaisson):
    if nbCaisson > 1:
        largeurcaisson = verif("Caisson " + str(i+1) + " - Entrer la largeur (" +
                               str(largeurInt) + " mm disponible)", 0, largeurInt)
    else:
        largeurcaisson = largeurInt
    porte = verif("Caisson " + str(i+1) +
                  " : Entrer le nombre de porte", 0, 2)
    nbEtageres = verif("Entrer le nombre d'étagère du caisson", 0, 50) + 1

    with open(cheminDossier + "\\" + nomProjet + 'detail.txt', 'a') as fc:
        fc.write("\nCaisson " + str(i+1) + "\nLargeur : " + str(largeurcaisson) +
                 " mm\nNombre de porte : " + str(porte) + "\nNombre d'étagères : " + str(nbEtageres) + "\n")
        fc.close

    if recouvrement != 0:
        if porte != 0:
            hporte = hauteurTotale - hauteurSocle - 4
            lporte = int((largeurcaisson / porte) - (porte * 4))
            writeAll(str(porte), str(hporte), str(lporte), "Portes")
        if hauteurSocle != 0 and i < 2:
            writeAll(str(1), str((largeurTotale)),
                     str(hauteurSocle), "Bandeau Socle")
    else:
        if porte != 0:
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

    with open(fichierFournisseur, 'a') as f:
        f.write("\nEn " + str(epaisseurFond) + "mm d'épaisseur\n")
        f.close
    with open(fichierDetail, 'a') as fc:
        fc.write("\n\nFond\n")
        fc.close
    if largFond > largeurPxMax:
        largFond = largFond / 2
    writeAll(str(2), str(hauteurFond), str(largFond), "Fond")
