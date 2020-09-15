import random
import sys

### POKEMON ###
class Pokemon:
	def __init__(self, name, level, health, max_health, type, is_knocked_out):
		self.name 			= name
		self.level 			= level
		self.health 		= health
		self.max_health 	= max_health
		self.type 			= type
		self.is_knocked_out = is_knocked_out 

### DISPLAY INFOMATION - This is the infomation displayed to the user in a turn. ###
	def display_infomation(self, other_pokemon):
		print("> {} attacks with {}!".format(self.name, self.type))
		damage = self.attack(other_pokemon)
		print("> {} takes {} {} damage.".format(other_pokemon.name, damage, self.type))
		print("> {} is at {}/{}HP".format(other_pokemon.name, other_pokemon.health, other_pokemon.max_health))
		if other_pokemon.knocked_out() == True:
			print("> {} faints!".format(other_pokemon.name))
		return print("\n")

### ATTACK - This includes all the damage calculations. ###
	def attack(self, other_pokemon):
		if self.advantage_matrix(other_pokemon) == True:
			damage = self.level * 2 + random.randint(self.level, self.level * 2)
			other_pokemon.lose_health(damage)
			print ("> IT'S SUPER EFFECTIVE!!")
			return damage
		elif self.disadvantage_matrix(other_pokemon) == True:
			damage = self.level * 0.5 + random.randint(self.level, self.level * 2)
			other_pokemon.lose_health(damage)
			print("> It's not very effective...")
			return damage
		else:
			damage = self.level + random.randint(self.level, self.level * 2)
			other_pokemon.lose_health(damage)     
			return damage

### TYPE MATRIX - These functions check whether the attacking pokemon has advantage or disadvantage ###
	def advantage_matrix(self, other_pokemon):
		advantage = False
		advantage_dict = {"fire":"grass", "grass":"water", "water":"fire"}
		for i in advantage_dict.items():
			if i == (self.type, other_pokemon.type):
				advantage = True
				break
			else:
				continue
		return advantage

	def disadvantage_matrix(self, other_pokemon):
		disadvantage = False
		disadvantage_dict = {"grass":"fire", "water":"grass", "fire":"water"}
		for i in disadvantage_dict.items():
			if i == (self.type, other_pokemon.type):
				disadvantage = True
				break
			else:
				continue
		return disadvantage

### HEALTH - These function control all healing and damage to pokemon ###      
	def lose_health(self, damage):
		self.health = self.health - damage
		if self.health <= 0:
			self.health = 0
		return

	def gain_health(self):
		healing = 20 + random.randint(5, 20)
		self.health = self.health + healing
		if self.health > self.max_health:
			self.health = self.max_health
		print("> {} regained {} health.".format(self.name, healing))
		print("> {} is at {}/{}HP".format(self.name, self.health, self.max_health))
		return print("\n")

	def knocked_out(self):
		if self.health <= 0:
			self.is_knocked_out = True
			return self.is_knocked_out
		else:
			return
     

### TRAINER ###
class Trainer:
	def __init__(self, name, current_pokemon, pokemons, potions):
		self.name 				= name
		self.current_pokemon 	= current_pokemon
		self.pokemons 			= pokemons
		self.potions 			= potions


### ATTACK OTHER TRAINER - This function contrains the infomation to attack another trainer ###
	def attack_other_trainer(self, AI_trainer):
		our_pokemon 	= self.pokemons[self.current_pokemon]
		their_pokemon 	= AI_trainer.pokemons[AI_trainer.current_pokemon]
		our_pokemon.display_infomation(their_pokemon)

### CHANGE POKEMON - Allows trainers to change pokemon ###
	def change_pokemon(self, change):
		except_count	= 0
		pokemon_picked	= False
		while pokemon_picked == False:
			try:
				if self.pokemons[change].is_knocked_out == True:
					print("> {} is knocked out!".format(self.pokemons[change].name))
					print("> Select a Pokémon...")
					print("> Input 1 to 6")
					change = int(input()) - 1
					continue

				elif self.pokemons[change] == self.pokemons[self.current_pokemon]:
					print("> {} is already fighting!".format(self.pokemons[self.current_pokemon].name))
					print("> Select a Pokémon...")
					print("> Input 1 to 6")
					change = int(input()) - 1
					continue

				else:
					self.current_pokemon = change
					print("> {} sends out {}".format(self.name, self.pokemons[self.current_pokemon].name) + "\n")
					return self.current_pokemon
			except:
				except_count = except_count + 1
				print("> An exception error occurred while changing Pokémons")
				if except_count >= 5:
					print(">>> Too many exception errors occurred, closing loop.")
					sys.exit(1)
				continue

### USE POTIONS - Allows the trainers to use potions to heal pokemon ###
	def use_potions(self):
		our_pokemon = self.pokemons[self.current_pokemon]
		print("> {} used a potion on {}".format(self.name, our_pokemon.name))
		Pokemon.gain_health(our_pokemon)
		self.potions = self.potions - 1
		return

### WHITED OUT ###
	def whited_out(self):
		counter = 0
		for i in self.pokemons:
			if i.is_knocked_out == True:
				counter += 1
		if counter == int(len(self.pokemons)):
			print("> {} is out of pokemon!".format(self.name))
			print("> {} whites out!".format(self.name))
			return True
		else:
			return False

class GAME:

	def encounter_pick():
		encounter_picked = False
		while encounter_picked == False:
			try:
				print("Who do you wish to fight?")
				print("## Ash: 1 	## Gary: 2") 
				print("## Aurore: 3 	## Prof. Oak: 4")
				encounter = int(input())
				print()

				if encounter == 1:
					print("> You enter battle with Ash!" + "\n")
					encounter_picked = True
					encounter = ash
					return encounter

				elif encounter == 2:
					print("> You enter battle with Gary!" + "\n")
					encounter_picked = True
					encounter = gary
					return encounter

				elif encounter == 3:
					print("> You enter battle with Aurore!" + "\n")
					encounter_picked = True
					encounter = aurore
					return aurore

				elif encounter == 4:
					print("> You enter battle with Prof. Oak!" + "\n")
					print("> GOOD LUCK MEMELORD" + "\n")
					encounter_picked = True
					encounter = prof_oak
					return prof_oak

				else:
					print("> That is not a trainer!" + "\n")
					continue
			except:
				print("\n" + "> An exception error occurred, try again." + "\n")
				continue
		# print("\n" + "BATTLE!")
		# return encounter

	def encounter(AI_trainer):
		close_game 		= False
		except_count	= 0
		battle_turn		= 0
		AI_pkmn 		= 0
		while player.whited_out() == False:
			battle_turn = battle_turn + 1
			print("ROUND " + str(battle_turn))
			turn = 1
			battle_loop = False
			if turn == 1:

				if player.pokemons[player.current_pokemon].is_knocked_out == True:
					print("##pkmn")
					Battle.pkmn()
					print("> Select a Pokémon...")
					print("> Input 1 to 6")
					x = int(input()) - 1
					player.change_pokemon(x)
					battle_loop = True
				
				while battle_loop == False:
					try: 
						print("########################## {}'s turn".format(player.name).upper())
						print("#########################>[L:{}] [{}/{}HP] - {} <".format(player.pokemons[player.current_pokemon].level, player.pokemons[player.current_pokemon].health, player.pokemons[player.current_pokemon].max_health, player.pokemons[player.current_pokemon].name))
						print("#########################>[L:{}] [{}/{}HP] - {}".format(AI_trainer.pokemons[AI_trainer.current_pokemon].level, AI_trainer.pokemons[AI_trainer.current_pokemon].health, AI_trainer.pokemons[AI_trainer.current_pokemon].max_health, AI_trainer.pokemons[AI_trainer.current_pokemon].name))
						print("WHAT WOULD YOU LIKE TO DO?" + "\n" + "1: FIGHT 	2: pkmn" + "\n" + "3: PACK 	4: RUN")
						move = int(input())
						print()

						if move == 1:
							print("##FIGHT")
							player.attack_other_trainer(AI_trainer)
							battle_loop = True

						elif move == 2:
							print("##pkmn")
							Battle.pkmn()
							print("> Select a Pokémon...")
							print("> Input 1 to 6")
							x = int(input()) - 1
							if x == -1:
								battle_loop = False
							else:
								player.change_pokemon(x)
								battle_loop = True

						elif move == 3:
							print("##PACK")
							if player.potions <= 0:
								print("You don't have any potions left!" + "\n")
								battle_loop = False
							else:
								player.use_potions()
								print("You have {} potions left!".format(player.potions) + "\n")
								battle_loop = True

						elif move == 4:
							print("##RUN")
							print("> Can't Escape" + "\n")
							battle_loop = False

						elif move == 666:
							print("##BREAKING")
							battle_loop = True
							close_game = True
							break
						
						else:
							print("## ")
							print("> Invalid move, try again.")
							continue

					except:
						except_count = except_count + 1
						print("> An exception error occurred while in menus." + "\n")
						if except_count >= 5:
							print("Too many exception errors occurred.")
							print("> BREAKING")
							sys.exit(1)
						continue

			if close_game == True:
				break

			if AI_trainer.whited_out() == True:
				print("\n" + "You defeated {}!".format(AI_trainer.name))
				print("Congratulations!")
				break

			input("Press Enter to continue..." + "\n" + "\n")
			turn = 2

			if turn == 2:
				print("########################## {}'s turn".format(AI_trainer.name).upper())
				if AI_trainer.pokemons[AI_trainer.current_pokemon].health <= 8 and AI_trainer.pokemons[AI_trainer.current_pokemon].health != 0 and AI_trainer.potions > 0:
					AI_trainer.use_potions()

				elif AI_trainer.pokemons[AI_trainer.current_pokemon].is_knocked_out == True:
					AI_pkmn = AI_pkmn + 1
					AI_trainer.change_pokemon(AI_pkmn)

				else:
					AI_trainer.attack_other_trainer(player)

			input("Press Enter to continue..." + "\n" + "\n")
			turn = 1
			continue
						



class Battle:

	def pkmn():
		print("> CURRENT POKEMON")
		print("> A: Active, KO: Knocked Out" + "\n")
		nr = 0
		for i in player.pokemons:
			nr = nr + 1
			# KOed Pokemon #
			if i.is_knocked_out == True:
				print("[L:" + str(i.level) + "] "+ "[{}/{}HP]".format(i.health, i.max_health))
				print("[KO] " + i.name.upper() + " ({})".format(nr) + "\n")
				continue
			# Active Pokemon #
			elif i.name == player.pokemons[player.current_pokemon].name:
				print("[L:" + str(i.level) + "] "+ "[{}/{}HP]".format(i.health, i.max_health))
				print("[A] " + i.name.upper() + " ({})".format(nr) + "\n")
				continue

			else:
				print("[L:" + str(i.level) + "] "+ "[{}/{}HP]".format(i.health, i.max_health))
				print("    " + i.name.upper() + " ({})".format(nr) + "\n")

	def menu_pack():
		pass

	def menu_run():
		pass


### TRAINER LIST ###

### ASH ###
lvl = random.randint(3, 9)
charmander_ash 	= Pokemon("Charmander (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)
lvl = random.randint(3, 9)
bulbasaur_ash 	= Pokemon("Bulbasaur (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9)
squirtle_ash   	= Pokemon("Squirtle (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
caterpie_ash	= Pokemon("Caterpie (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9) + 2
gyarados_ash	= Pokemon("Gyarados (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9) + 3
victreebel_ash	= Pokemon("Victreebel (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)

ash 	= Trainer("Ash", 0, [charmander_ash, bulbasaur_ash, squirtle_ash, caterpie_ash, victreebel_ash, gyarados_ash], random.randint(3, 5))

### GARY ###
lvl = random.randint(3, 9)
squirtle_gary   = Pokemon("Squirtle (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
vulpix_gary		= Pokemon("Vulpix (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)
lvl = random.randint(3, 9)
bellsprout_gary	= Pokemon("Bellsprout (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9) + 2
scyther_gary	= Pokemon("Scyther (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9) + 3
arcanine_gary	= Pokemon("Arcanine (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)

gary 	= Trainer("Gary", 0, [squirtle_gary, vulpix_gary, bellsprout_gary, scyther_gary, arcanine_gary], random.randint(3, 5))

### AURORE ###
lvl = random.randint(3, 9)
bulbasaur_aurore 	= Pokemon("Bulbasaur (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9)
poliwag_aurore 		= Pokemon("Poliwag (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
mudkip_aurore		= Pokemon("Mudkip (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
sunflora_aurore		= Pokemon("Sunflora (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9) + 2
charmeleon_aurore	= Pokemon("Charmeleon (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)
lvl = random.randint(3, 9) + 4
persian_aurore		= Pokemon("Persian (Normal)", lvl, float(lvl * 10), lvl * 10, "Bite", False) 

aurore 		= Trainer("Aurore", 0, [bulbasaur_aurore, poliwag_aurore, mudkip_aurore, sunflora_aurore, charmeleon_aurore, persian_aurore], random.randint(3, 5))

### Prof. Oak
lvl = 1
magikarp_oak	= Pokemon("Magikarp (Water)", 1, float(lvl * 50), lvl * 50, "Water", False)
lvl = 99
missingno_oak	= Pokemon("MissingNo (?????)", lvl, float(lvl * 10), lvl * 10, "?????", False)

prof_oak 	= Trainer("Prof. Oak", 0, [magikarp_oak, missingno_oak,], 0)

### PLAYER ###
lvl = random.randint(3, 9)
charmander 	= Pokemon("Charmander (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)
lvl = random.randint(3, 9)
bulbasaur 	= Pokemon("Bulbasaur (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)
lvl = random.randint(3, 9)
squirtle 	= Pokemon("Squirtle (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
slowbro 	= Pokemon("Slowbro (Water)", lvl, float(lvl * 10), lvl * 10, "water", False)
lvl = random.randint(3, 9)
flareon 	= Pokemon("Flareon (Fire)", lvl, float(lvl * 10), lvl * 10, "fire", False)
lvl = random.randint(3, 9)
bellsprout	= Pokemon("Bellsprout (Grass)", lvl, float(lvl * 10), lvl * 10, "grass", False)

### GAME ###
print()
print("--- WELCOME TO POKÉFOLIO ---" + "\n" + "You will start with 6 pokemons that have random levels between 3-9" + "\n")
player	= Trainer("Player", 0, [charmander, bulbasaur, squirtle, slowbro, flareon, bellsprout], random.randint(3, 5))

print("### OVERVIEW ###")
print("NAME:" + player.name)
pokemons_string = ""
for i in player.pokemons:
	pokemons_string 	= pokemons_string + "[L:{}] ".format(i.level) + str(i.name) + ", "
pokemon_string_final	= pokemons_string.strip(", ")
pokemon_string_final 	= pokemon_string_final + "."
print("pkmn:", pokemon_string_final)
print("PACK: " + str(player.potions) + " Potions" + "\n")

print("### LETS START ###")
AI_trainer = GAME.encounter_pick()
GAME.encounter(AI_trainer)

print("\n" + "Game Over!" + "\n")

input("Press Enter to continue..." + "\n" + "\n")

