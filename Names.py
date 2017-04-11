import sys
import random

names = ["Adalger", "Adalrad", "Alburg", "Antonia", "Baius", "Baldrecht"
, "Bernard", "Bruna", "Caldwell", "Carlysle", "Celestus", "Cypran"
, "Dagmar", "Dalibor", "Digory", "Dividia", "Druchtbald", "Ebrehar"
, "Eldritch", "Engelmar", "Eucharius", "Faltrice", "Fenicia", "Florian"
, "Frodegaard", "Gailhem", "Gaius", "Gerald", "Grosso", "Guardia"
, "Hadburg", "Haldor", "Helga", "Hyppolytus", "Hudrich", "Idalia"
, "Isarn", "Ivar", "Jaelle", "Jaromir", "Joachim", "Ketill"
, "Knightwine", "Knut", "Laborans", "Landrich", "Leifwin"
, "Llywellyn", "Lucretius", "Lydia", "Maban", "Madwen", "Magnus" 
, "Marozia", "Milo", "Mordecai", "Nadalger", "Nantelm", "Narcissus"
, "Narduin", "Nivard", "Norman", "Octavius", "Odelgarde", "Olivier" 
, "Oswin", "Ottokar", "Palmeria", "Pascal", "Patrick", "Portia" 
, "Priam", "Procopius", "Proxima", "Pura", "Quentin", "Quirinius"
, "Radax", "Ratfrid", "Regulus", "Reinmar", "Reinnolt", "Roland" 
, "Roman", "Rosso", "Rothard", "Rufus", "Sadrabald", "Sampson"
, "Sapphira", "Savius", "Severin", "Sigmund", "Snorri", "Soave"
, "Sonofrida", "Styrbiorn", "Suspecta", "Sylvius", "Taimar"
, "Tedesca", "Theogaarde", "Tiberius", "Transmundus", "Tumidia"
, "Udelo", "Unica", "Urith", "Urso", "Valens", "Veneria"
, "Venuto", "Villano", "Virgilia", "Volker", "Vrolijk"
, "Walantrude", "Waldred", "Whitehelm", "Wojciech", "Wolfhardt"
, "Wyburg", "Yael", "Ysoria", "Zawissus", "Zwentibold"]


def getName():
	return random.choice(names)

#for x in range(0, 20):
#	print(random.choice(names))

