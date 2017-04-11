import random 
import sys
import Names

ans = True

while ans:

	name = input("What is the first name of your character? (press enter to quit)")

	if name == "":
		sys.exit()
	else:

		char = {} 
		alx = ["Lawful ", "Neutral ", "Chaotic "]
		aly = ["Good ", "Neutral ", "Evil "]

		nameStr = ["Strong", "Powerful", "Stable", "Big", "Forceful", "Unstoppable"
		, "Destroyer", "Crusher", "All Powerful"]
		nameDex = ["Dexterous", "Quick", "Speedy", "Agile", "Adept", "Nimble", "Shadow"
		, "Sneaky", "Sneaker", "Backstabber", "Deceptive", "Twinkle Toes", "Fleet Footed"]
		nameCon = ["Hearty", "Heavy", "Stout", "Portly", "Beefy", "Large", "Wall"
		, "Muscle", "Diabetic", "Fat", "Tank", "Unmovable"]
		nameInt = ["Intelligent", "Professor", "Scholar", "Astute", "Profound", "Brain"
		, "Knowledgeable", "Well Read", "Nerd", "Graduated", "Wizard", "Four Eyed"]
		nameWis = ["Wise", "Old", "Sage", "Spiritual", "Enlightened", "Rational"
		, "Crucified", "All Knowing", "Master", "Sensei", "One Eyed", "Cosmic"]
		nameCha = ["Charismatic", "Dazzling", "Beautiful", "Appealing", "Alluring"
		, "Lover", "Companion", "Mistress", "Well Endowed", "Smooth Talker"
		, "Whisperer", "Sensual", "Smooth"]
		nameDef = ["Royal", "Unknown", "Lost", "Child", "Loner", "Wanderer"
		, "Unforgiven", "Shackled", "Prisoner", "Connoisseur", "Jester", "Oaf"
		, "Aloof", "Lazy", "Fallen", "Hilbilly", "Confused", "Slave", "Runaway"
		, "Artist", "Loser", "Defeated", "Deadbeat", "Gambler", "Outsider"
		, "Poet", "Homeless" ]

		race = ["Human", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc"]

		classList = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk"
		, "Paladin", "Ranger", "Rogue", "Sorcerer", "Wizard"]
		classStr = ["Barbarian", "Fighter", "Paladin", "Druid"]
		classDex = ["Druid", "Ranger", "Rogue"]
		classCon = ["Barbarian", "Fighter"]
		classInt = ["Cleric", "Sorcerer", "Wizard"]
		classWis = ["Cleric", "Paladin", "Monk"]
		classCha = ["Bard", "Rogue"]

		clericTrait = ["Air ", "Animal ", "Earth ", "Fire ", "Plant ", "Water ", "Weather "]
		druidTrait = ["AnimalCompanion ", "Air ", "Animal ", "Earth ", "Fire ", "Plant "
		, "Water ", "Weather "]
		rangerTrait = ["Archery ", "Two-Handed "]
		sorcererTrait = ["Aberrant ", "Abyssal ", "Arcane ", "Celestial ", "Destined "
		, "Draconic ", "Elemental ", "Fey ", "Infernal ", "Undead "]

		char['str'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		char['dex'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		char['con'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) 
		char['int'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		char['wis'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		char['cha'] = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		char['alx'] = random.choice(alx)
		char['aly'] = random.choice(aly)

		if( char['str'] > char['dex'] and char['str'] > char['con'] and char['str'] > char['int'] 
		and char['str'] > char['wis'] and char['str'] > char['cha']):
			char['name'] = name + " " + Names.getName() + " The " +  random.choice(nameStr)
			char['class'] = random.choice(classStr)
		elif( char['dex'] > char['str'] and char['dex'] > char['con'] and char['dex'] > char['int'] 
		and char['dex'] > char['wis'] and char['dex'] > char['cha']):
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameDex)
			char['class'] = random.choice(classDex)
		elif( char['con'] > char['str'] and char['con'] > char['dex'] and char['con'] > char['int'] 
		and char['con'] > char['wis'] and char['con'] > char['cha']):
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameCon)
			char['class'] = random.choice(classCon)
		elif( char['int'] > char['str'] and char['int'] > char['dex'] and char['int'] > char['con'] 
		and char['int'] > char['wis'] and char['int'] > char['cha']):
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameInt)
			char['class'] = random.choice(classInt)
		elif( char['wis'] > char['str'] and char['wis'] > char['dex'] and char['wis'] > char['con'] 
		and char['wis'] > char['int'] and char['wis'] > char['cha']):
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameWis)
			char['class'] = random.choice(classWis)
		elif( char['cha'] > char['str'] and char['cha'] > char['dex'] and char['cha'] > char['con'] 
		and char['cha'] > char['int'] and char['cha'] > char['wis']):
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameCha)
			char['class'] = random.choice(classCha)
		else: 
			char['name'] = name + " " + Names.getName() + " The " + random.choice(nameDef)
			char['class'] = random.choice(classList)	

		char['race'] = random.choice(race)

		if char['class'] == "Cleric":
			char['class'] = random.choice(clericTrait) + "Cleric"
		elif char['class'] == "Druid": 
			char['class'] = random.choice(druidTrait) + "Druid"
		elif char['class'] == "Ranger":
			char['class'] = random.choice(rangerTrait) + "Ranger"
		elif char['class'] == "Sorcerer":
			char['class'] = random.choice(sorcererTrait) + "Sorcerer" 

		print("Character name: " + char['name'])
		#print("Race: ", char['race'])
		#print("Class: ", char['class'])
		#print("strength = ", char['str'])
		#print("dexterity = ", char['dex'])
		#print("constitution = ", char['con'])
		#print("intelligence = ", char['int'])
		#print("wisdom = ", char['wis'])
		#print("charisma = ", char['cha'])
		char['ali'] = "Alignment = " +  char['alx'] + char['aly']
		
		char['age'] = random.randint(1, 20) + random.randint(1, 20) 
		+ random.randint(1, 20) + 10

		fileName = name + '.txt'
		file = open(fileName, 'w+')


		file.write(str(char['name']))
		file.write("\n")
		file.write("Age: " + str(char['age']) + " years")
		file.write("\n")
		file.write("Race: " + char['race'])
		file.write("\n")
		file.write("Class: " + str(char['class']))
		file.write("\n")
		file.write(str(char['ali']))
		file.write("\n")
		file.write("Strength: " + str(char['str']))
		file.write("\n")
		file.write("Dexterity: " + str(char['dex']))
		file.write("\n")
		file.write("Constitution: " + str(char['con']))
		file.write("\n")
		file.write("Intelligence: " + str(char['int']))
		file.write("\n")
		file.write("Wisdom: " + str(char['wis']))
		file.write("\n")
		file.write("Charisma: " + str(char['cha']))

		file.close()
