# -*- coding: utf-8 -*-

from minitel.Minitel import Minitel
from minitel.ImageMinitel import ImageMinitel
from PIL import Image
from time import sleep
from math import *

import unidecode

class MinYLPG:
   def __init__(self):
      self.mode='MIXTE'
      self.minitel = Minitel()
      self.minitel.deviner_vitesse()
      self.minitel.identifier()
      self.minitel.definir_vitesse(4800)
      self.minitel.definir_mode(self.mode)
      self.minitel.configurer_clavier(etendu = True, curseur = False, minuscule = True)
      self.minitel.echo(False)
      self.minitel.efface()
      self.minitel.curseur(False)

   def clean_screen(self):
      self.minitel.position(0, 0)
      self.minitel.efface(portee = 'vraimenttout')
      self.minitel.position(1,1)
      self.minitel.taille(largeur = 2, hauteur = 2)

   def close(self):
      self.minitel.sortie.join()
      self.minitel.close()

   def message(self, message):
      message_sans_accent = unidecode.unidecode(message)
      self.minitel.envoyer(message_sans_accent)
      # self.minitel.envoyer(10)
      self.minitel.envoyer(13)

   def switch_mode(self):
      if self.mode == 'MIXTE':
         self.mode = 'VIDEOTEX'
      else:
         self.mode = 'MIXTE'
      self.minitel.definir_mode(self.mode)
      self.clean_screen()

   def follower_alert(self, abonne):
      self.switch_mode()

      if len(abonne) < 20:
         abocent = 2 * ( 10 - floor( len( abonne ) / 2 ) ) + 1
         epaisseur_texte = 2
      elif len(abonne) >= 20 and len(abonne) < 40:
         abocent = 20 - floor( len( abonne ) / 2 ) + 1
         epaisseur_texte = 1
      else:
         abocent = 7
         epaisseur_texte = 1
         abonne = "Achète-toi un nom moins long"

      self.minitel.position(0, 0)
      self.minitel.efface(portee = 'vraimenttout')
      self.minitel.position(0, 0)
      image = Image.open('minylpg/images/ylpg.png')
      image = image.resize((80, 72), Image.NEAREST)
      image_minitel = ImageMinitel(self.minitel)
      image_minitel.importer(image)
      image_minitel.envoyer(0, 0)


      self.minitel.position(10, 2)
      self.minitel.taille(largeur = 2, hauteur = 2)
      self.minitel.couleur(caractere=0, fond=7)
      self.minitel.envoyer("YOU LOOK")
      self.minitel.position(8, 4)
      self.minitel.taille(largeur = 2, hauteur = 2)
      self.minitel.couleur(caractere=0, fond=7)
      self.minitel.envoyer("PRETTY GOOD")
      self.minitel.position(abocent,22)
      self.minitel.taille(largeur = epaisseur_texte, hauteur = 2)
      self.minitel.couleur(caractere=0, fond=7)
      self.minitel.envoyer(abonne)

      self.minitel.bip()

      sleep(5)

      image = Image.open('minylpg/images/ylpgwink1.png')
      image = image.resize((20, 15), Image.NEAREST)
      image_minitel = ImageMinitel(self.minitel)
      image_minitel.importer(image)
      image_minitel.envoyer(20, 9)

      sleep(1.5)

      image = Image.open('minylpg/images/ylpgwink0.png')
      image = image.resize((20, 15), Image.NEAREST)
      image_minitel = ImageMinitel(self.minitel)
      image_minitel.importer(image)
      image_minitel.envoyer(20, 9)
      sleep(3)

      self.switch_mode()
