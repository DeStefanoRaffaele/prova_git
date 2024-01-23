# -*- coding: iso-8859-15 -*-
s = "Prova"
s1 = "Prova1"
print(s.upper())
print(s.lower())
print(s[2:])

# supponiamo di voler gestire una persona che possa essere in grado di 
# presentare se stessa al pubblico

# Cosa significa?

# Analizziamo la consegna:
# Una persona è un componente che offre la possibilità di effettuare una presentazione
# sì, ma cosa si intende per "persona"?
# Possiamo pensare che una [persona] sia in grado di <comunicare> il proprio [nome] e il
# proprio [cognome].
#
# +--------------------------+
# | Persona                  |
# +--------------------------+
# |   nome       alfanum.    |
# |   cognome    alfanum.    |
# +--------------------------+
# |   presentatestesso()     |
# +--------------------------+
#
class Persona:
    def __init__(self, nome, cognome): # costruttore
        self.nome = nome
        self.cognome = cognome
        
    def presentati(self):
        print("Ciao, piacere di conoscerti, mi chiamo", 
             self.cognome, self.nome)
        
paperone = Persona("Paperon", "De' Paperoni")
archimede = Persona("Archimede", "Pitagorico")
pico = Persona("Pico", "De' Paperis")

lista = [paperone, archimede, pico]
lista.reverse()

for p in lista:
    p.presentati()
    
