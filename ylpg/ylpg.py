#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from minitel.Minitel import Minitel
from minitel.ImageMinitel import ImageMinitel
from PIL import Image
from time import sleep
from math import *

minitel = Minitel()

minitel.deviner_vitesse()
minitel.identifier()
minitel.definir_vitesse(4800)
minitel.definir_mode('VIDEOTEX')
minitel.configurer_clavier(etendu = True, curseur = False, minuscule = True)
minitel.echo(False)
minitel.efface()
minitel.curseur(False)
with open("abon.txt", "r") as abon:
 abonne = abon.read()

txtepais = 2

if len(abonne) < 20:
	abocent = 2*(10-floor(len(abonne)/2))+1
elif len(abonne) >= 20 and len(abonne) < 40:
	abocent = 20-floor(len(abonne)/2)+1
	txtepais = 1
else:
	abocent = 7
	txtepais = 1
	abonne = "achète-toi un nom moins long"
minitel.position(0, 0)
minitel.efface(portee = 'vraimenttout')

minitel.position(0, 0)
image = Image.open('ylpg.png')
image = image.resize((80, 72), Image.NEAREST)
image_minitel = ImageMinitel(minitel)
image_minitel.importer(image)
image_minitel.envoyer(0, 0)


minitel.position(10, 2)
minitel.taille(largeur = 2, hauteur = 2)
minitel.couleur(caractere=0, fond=7)
minitel.envoyer("YOU LOOK")
minitel.position(8, 4)
minitel.taille(largeur = 2, hauteur = 2)
minitel.couleur(caractere=0, fond=7)
minitel.envoyer("PRETTY GOOD")
minitel.position(abocent,22)
minitel.taille(largeur = txtepais, hauteur = 2)
minitel.couleur(caractere=0, fond=7)
minitel.envoyer(abonne)

"""
minitel.taille(largeur = 2, hauteur = 2)
minitel.couleur(caractere = 'vert')
minitel.envoyer('PyMinitel')
minitel.position(6, 9)
minitel.envoyer('___________')
"""
"""
textes = [
    # ---------------------
    "1",
    "2",
    "3 ",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "1",
    "2",
    "3",
    "4",
    "5 ",
    "6",
    "7",
    "8",
    "9",
    "10",
    "1",
    "2",
    "3",
    "4",
    "5"
]

ligne = 0
for texte in textes:
    minitel.position(1, ligne)
    minitel.envoyer(texte)
    ligne += 1
"""
minitel.bip()

sleep(5)

image = Image.open('ylpgwink1.png')
image = image.resize((20, 15), Image.NEAREST)
image_minitel = ImageMinitel(minitel)
image_minitel.importer(image)
image_minitel.envoyer(20, 9)

sleep(1.5)

image = Image.open('ylpgwink0.png')
image = image.resize((20, 15), Image.NEAREST)
image_minitel = ImageMinitel(minitel)
image_minitel.importer(image)
image_minitel.envoyer(20, 9)


minitel.sortie.join()
minitel.close()
