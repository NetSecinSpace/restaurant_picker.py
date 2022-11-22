import random
import optparse
import random


restaurant_list_complex = (
	('MT Club', 'y', 'breakfast', 'american'),
	('MT Club', 'y', 'lunch', 'american'),
	('MT Club', 'y', 'dinner', 'american'),
	('Kobe', 'y', 'lunch', 'asian'),
	('Kobe', 'y', 'dinner', 'asian'),
	('Mighty Mo', 'y', 'lunch', 'american'),
	('Mighty Mo', 'y', 'dinner', 'american'),
	('Jakers', 'y', 'lunch', 'american'),
	('Jakers', 'y', 'dinner', 'american'),
	('Roadhouse Diner', 'n', 'lunch', 'american'),
	('Roadhouse Diner', 'n', 'dinner', 'american'),
	('Fire Pizza', 'y', 'lunch', 'american'),
	('Celtic Cowboy', 'y', 'lunch', 'american'),
	('Celtic Cowboy', 'y', 'dinner', 'american'),
	('Tracys', 'n', 'breakfast', 'american'),
	('Tracys', 'n', 'lunch', 'american'),
	('Tracys', 'n', 'dinner', 'american'),
	('Cafe Rio', 'n', 'lunch', 'mexican'),
	('Cafe Rio', 'n', 'dinner', 'mexican'),
	('The Block', 'y', 'lunch', 'american'),
	('The Block', 'y', 'dinner', 'american'),
	('Mackenzie River', 'y', 'lunch', 'american'),
	('Mackenzie River', 'y', 'dinner', 'american'),
	('Smoked BBQ', 'n', 'lunch', 'american'),
	('Mod Pizza', 'n', 'lunch', 'american'),
	('Mod Pizza', 'n', 'dinner', 'american'),
	('MT Sub Shop', 'n', 'lunch', 'american'),
	('MT Sub Shop', 'n', 'dinner', 'american'),
	('Pho 10', 'n', 'lunch', 'asian'),
	('Pho 10', 'n', 'dinner', 'asian'),
	('Maple Garden', 'y', 'lunch', 'asian'),
	('Maple Garden', 'y', 'dinner', 'asian'),
	('Taco Treat', 'y', 'lunch', 'mexican'),
	('Taco Treat', 'y', 'dinner', 'mexican'),
	('Chucks Oriental Palance', 'n', 'lunch', 'asian'),
	('Chucks Oriental Palance', 'n', 'dinner', 'asian'),
	('Terriyaki Madness', 'n', 'lunch', 'asian'),
	('Terriyaki Madness', 'n', 'dinner', 'asian'),
	('Fiesta En Jalisco', 'n', 'lunch', 'mexican'),
	('Fiesta En Jalisco', 'n', 'dinner', 'mexican'),
	('Pit Stop', 'y', 'lunch', 'american'),
	('Pit Stop', 'y', 'dinner', 'american'),
	('MT Pints', 'y', 'lunch', 'american'),
	('MT Pints', 'y', 'dinner', 'american'),
	('Taco Del X', 'n', 'dinner', 'mexican'),
	('Taco Del X', 'n', 'dinner', 'mexican'),
	('Taco Johns', 'n', 'breakfast', 'mexican'),
	('Taco Johns', 'n', 'lunch', 'mexican'),
	('Taco Johns', 'n', 'dinner', 'mexican'),
	('Fuddruckers', 'y', 'lunch', 'american'),
	('Fuddruckers', 'y', 'dinner', 'american'),
	('Fords Drive In', 'n', 'lunch', 'american'),
	('Fords Drive In', 'n', 'dinner', 'american'),
	('Buffalo Wild Wings', 'y', 'lunch', 'american'),
	('Buffalo Wild Wings', 'y', 'dinner', 'american'),
	('Halftime', 'y', 'breakfast', 'american'),
	('Halftime', 'y', 'lunch', 'american'),
	('Halftime', 'y', 'dinner', 'american'),
	('3Ds', 'y', 'lunch', 'asian'),
	('3Ds', 'y', 'dinner', 'asian'),
	('Little Athens', 'n', 'lunch', 'greek'),
	('Little Athens', 'n', 'dinner', 'greek'),
	('Pita Pit', 'n', 'lunch', 'american'),
	('Pita Pit', 'n', 'dinner', 'american'),
	('Jimmy Johns', 'n', 'lunch', 'american'),
	('Jimmy Johns', 'n', 'dinner', 'american'),
	('R&R', 'y', 'breakfast', 'american'),
	('R&R', 'y', 'lunch', 'american'),
	('R&R', 'y', 'dinner', 'american'),
	('Black Bear Diner', 'n', 'breakfast', 'american'),
	('Black Bear Diner', 'n', 'lunch', 'american'),
	('Black Bear Diner', 'n', 'dinner', 'american'),
	('Boston', 'y', 'lunch', 'american'),
	('Boston', 'y', 'dinner', 'american'),
	('Chilis', 'y', 'lunch', 'american'),
	('Chilis', 'y', 'dinner', 'american'),
	('P Gibson', 'y', 'lunch', 'american'),
	('P Gibson', 'y', 'dinner', 'american'),
	('5 on Black', 'n', 'lunch', 'brazilian'),
	('5 on Black', 'n', 'dinner', 'brazilian'),
	('Jersey Mikes', 'n', 'lunch', 'american'),
	('Jersey Mikes', 'n', 'dinner', 'american'),
	('A&K Diner', 'n', 'lunch', 'korean')
)
#example of line in rlc ('MT Club', 'y', 'breakfast', 'american')

#get arguments, such as, what meal of the day, alcohol or not, and maybe even type of food someday
def get_args():
	parser = optparse.OptionParser()
#	parser.set_default("-m", "lunch")
#	parser.set_default("-a", "n")
#	parser.set_default("-t", "american")
	parser.add_option("-m", "--meal", dest="meal",
					  help="What meal of the day is it")
#	parser.add_option("-a", "--alcohol", dest="alc_check",
#					  help="(y/n) on booze")
#	parser.add_option("-t", "--type", dest="type_food",
#					help="pick a food type")
	(options, arguments) = parser.parse_args()
	#if options.meal:
	#	parser.parse_args(args=-a, y)

	if not options.meal:
		parser.error("[-] dude what meal is it? (breakfast, lunch, dinner) Type -m and the meal choice")
#	elif not options.alc_check:
#		parser.error("[-] do you want to drink? (y,n) Type -a and y or n")
	return options

options = get_args()

#check for if the user wants alcohol or not. If no then both y and n are shown so that all options are available
#def haz_booz():
#	booze_check = []
#	for restaurants in range( len(restaurant_list_complex)):
#		if (restaurant_list_complex[restaurants])[1]  == options.alc_check:
#			booze_check.append(restaurant_list_complex[restaurants][0:3])
##			print(restaurant_list_complex[restaurants][0:3])
#	return (booze_check)

#haz_booz()


for meal_time in range(len(restaurant_list_complex)):
	meal_check = []
	if (restaurant_list_complex[meal_time])[2] == options.meal:
		meal_check.append(restaurant_list_complex[meal_time][0])
		print(restaurant_list_complex[meal_time][0:2])
	#return meal_check

