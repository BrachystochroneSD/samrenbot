#!/usr/bin/env python
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

textes = [
    # ---------------------
"pas de soucis @KwaKwak on reviendra ;)",
"Virriathus: raid à la chaine xD",
"SherlockThomes: Tu as un autre jeu?",
"ethan_squadsp050: @edward_retrodecouverte dommage",
"ModérateurVérifiéStreamlabs: Merci pour ton follow gdlosc59!",
"upperleftcorner: Heureusement y'a d'autres épisodes de Layton",
"ModérateurVérifiéStreamlabs: Merci pour ton follow dadapokemondu61!",
"SherlockThomes: Ah ok",
"mir16200: oh la ref",
"Keemaes: Ca va permettre de regarder ton stream une fois avec plaisir KwaKwak",
"sursutique: @edward_retrodecouverte c peut etre pas un si mauvais moment que ça Kappa",
"LUL",
"Ghanlow_: Kwakwak j'ai un jeu pour toi !!",
"dylanxw3: Tu va faire un Live Yo Kai Watch 3 ? sa serai sympas c'est trop sous coter",
"aubbruu: La petite réf au Coeur a ses raisons ;)",
";)",
"antho3913234: Bon ben y'a plus qu'à recommencer le jeu /P",
"SherlockThomes: Je vais te suivre quand même.",
"VIPAbonné(e) depuis 3 mois (badge 3 mois)Creille_Zhaie: accordéon, ça va avec prof layton x)",
"SherlockThomes: Tu vas faire quoi comme autre jeu?",
"ModérateurVérifiéStreamlabs: Merci pour ton follow Letha21!",
"Ghanlow_: Kwakwak j'ai trouvé un jeu !",
"ModérateurVérifiéStreamlabs: Merci pour ton follow libilline!",
"SherlockThomes: Okay",
"Twitch Primeking_bowzer: Prononcé Ghost of Sushi Ma bien sur XD",
"Julbizar: Et tu aimes Pokemon, c'est parfait",
"dylanxw3: Tu poura tester Yo Kai Watch 3? crée par Level 5 aussi",
"antho3913234: Fais-tu des vidéos youtube ?",
"VIPAbonné(e) depuis 3 mois (badge 3 mois)Creille_Zhaie: 3ds je crois",
"Abonné(e) depuis 3 mois (badge 3 mois)Bajicof: oui",
"dylanxw3: 3DS tres sous coter et remplit de référence",
"SherlockThomes: @antho3913234 je voudrais savoir aussi",
"Abonné(e) depuis 3 mois (badge 3 mois)Bajicof: sur switch on sait pas quand il va sortir",
"naglagla83: saluuuuuuut kwakwak",
"edward_retrodecouverte: je te laisse le choix ;)",
"dylanxw3: C'est le 4 sur Switch =D",
"edward_retrodecouverte: Fais nous découvrir qqun :D",
"Twitch Primeking_bowzer: Le Raid du coeur !",
"ModérateurVérifiéStreamlabs: Merci pour ton follow antho3913234!",
"mir16200: Cursedware",
"romano_c: un grand raid...implique... de grandes responsabilités...",
"ModérateurVérifiéStreamlabs: Merci pour ton follow king_bowzer!",
"edward_retrodecouverte: alors raid/ strubble",
"dylanxw3: Ui fait nous découvrire =D",
"edward_retrodecouverte: sympa ;)",
"ModérateurVérifiéStreamlabs: Merci pour ton follow Quayle57!",
]





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

sleep(3)

minitel.definir_mode('MIXTE')
minitel.efface(portee = 'vraimenttout')
minitel.position(1,1)
minitel.taille(largeur = 2, hauteur = 2)
ligne = 0
for texte in textes:
    minitel.envoyer(texte)
    minitel.envoyer(10)
    minitel.envoyer(13)
    ligne += 1



minitel.sortie.join()
minitel.close()
