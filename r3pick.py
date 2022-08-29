import random
import optparse


restaurant_list_complex = (
	('MT Club', 'y', 'any', 'american'),
	('Kobe', 'y', 'lunch/dinner', 'asian'),
	('Mighty Mo', 'y', 'lunch/dinner', 'american'),
	('Jakers', 'y', 'lunch/dinner', 'american'),
	('Roadhouse Diner', 'n', 'lunch/dinner', 'american'),
	('Fire Pizza', 'y', 'lunch', 'american'),
	('Celtic Cowboy', 'y', 'lunch/dinner', 'american'),
	('Tracys', 'n', 'any', 'american'),
	('Cafe Rio', 'n', 'lunch/dinner', 'mexican'),
	('The Block', 'y', 'lunch/dinner', 'american'),
	('Mackenzie River', 'y', 'lunch/dinner', 'american'),
	('Smoked BBQ', 'n', 'lunch', 'american'),
	('Mod Pizza', 'n', 'lunch/dinner', 'american'),
	('MT Sub Shop', 'n', 'lunch/dinner', 'american'),
	('Pho 10', 'n', 'lunch/dinner', 'asian'),
	('Maple Garden', 'y', 'lunch/dinner', 'asian'),
	('Taco Treat', 'n', 'lunch/dinner', 'mexican'),
	('Amigo Lounge', 'y', 'lunch/dinner', 'mexican'),
	('Chucks Oriental Palance', 'n', 'lunch/dinner', 'asian'),
	('Terriyaki Madness', 'n', 'lunch/dinner', 'asian'),
	('Fiesta En Jalisco', 'n', 'lunch/dinner', 'mexican'),
	('Pit Stop', 'y', 'lunch/dinner', 'american'),
	('MT Pints', 'y', 'lunch/dinner', 'american'),
	('Taco Del X', 'n', 'lunch/dinner', 'mexican'),
	('Taco Johns', 'n', 'any', 'mexican'),
	('Fuddruckers', 'y', 'lunch/dinner', 'american'),
	('Fords Drive In', 'n', 'lunch/dinner', 'american'),
	('Buffalo Wild Wings', 'y', 'lunch/dinner', 'american'),
	('Halftime', 'y', 'any', 'american'),
	('3Ds', 'y', 'lunch/dinner', 'asian'),
	('Little Athens', 'n', 'lunch/dinner', 'greek'),
	('Pita Pit', 'n', 'lunch/dinner', 'american'),
	('Jimmy Johns', 'n', 'lunch/dinner', 'american'),
	('R&R', 'y', 'any', 'american'),
	('Black Bear Diner', 'n', 'any', 'american'),
	('2K', 'n', 'lunch', 'american'),
	('Boston', 'y', 'lunch/dinner', 'american'),
	('Chilis', 'y', 'lunch/dinner', 'american'),
	('P Gibson', 'y', 'lunch/dinner', 'american'),
	('5 on Black', 'n', 'lunch/dinner', 'brazilian'),
	('Jersey Mikes', 'n', 'lunch/dinner', 'american')
)

# alc_check = 'y'
time_check = 'lunch'

def get_args():
	parser = optparse.OptionParser()
	parser.set_default("-m", "lunch")
	parser.set_default("-a", "n")
	parser.add_option("-m", "--meal", dest="meal",
					  help="What meal of the day is it")
	parser.add_option("-a", "--alcohol", dest="alc_check",
					  help="(y/n) on booze")
	(options, arguments) = parser.parse_args()
	#if options.meal:
	#	parser.parse_args(args=-a, y)

	if not options.meal:
		parser.error("[-] dude what meal is it? (breakfast, lunch, dinner)")
	elif not options.alc_check:
		parser.error("[-] do you want to drink? (y,n)")
	return options

options = get_args()

def haz_booz():
	booze_check = []
	for restaurants in range( len(restaurant_list_complex)):
		if (restaurant_list_complex[restaurants])[1]  == options.alc_check:
			booze_check.append(restaurant_list_complex[restaurants][0:3])
#			print(restaurant_list_complex[restaurants][0:3])
	return (booze_check)

haz_booz()

#def big():
#	all_test = []#
#	for restaurants in range( len(restaurant_list_complex)):
#		if (restaurant_list_complex[restaurants])[1]  == options.alc_check: and
#		if (restaurant_list_complex[restaurants])[2] == options.meal:
#			all_test.append(restaurant_list_complex[restaurants][0])
#			print(all_test)



#if options.meal == ((restaurant_list_complex)[2]):
#	print(restaurant_list_complex)

for meal_time in range(len(restaurant_list_complex)):
	meal_check = []
	if (restaurant_list_complex[meal_time])[2] == options.meal:
		meal_check.append(restaurant_list_complex[meal_time][0])
		print(restaurant_list_complex[meal_time][0:2])
#	return meal_check


#print(haz_booz())
#print((haz_booz())[0][2])

#for meal_time in range(len(booze_check)):
#	if (booze_check[meal_time])[2] == options.meal:
#		print haz_booz()

#for meal_time in range(len(haz_booz())):
#	if (haz_booz(meal_time))[3] == options.meal:
#	if (haz_booz(meal_time)[3]) == options.meal:
#		print(restaurant_list_complex[meal_time][0])

#def meal_check():
#	what_meal = []
#	for meal_time in range(len(haz_booz()[3])):
#		if haz_booz()[3] == options.meal:
#			what_meal.append(haz_booz()[1])
#			print(what_meal)

#meal_check()

#-----------------------------------------------------

#for restaurants in haz_booz():
#	what_meal = []
#	if (restaurant_list_complex[restaurants])[2] == time_check:
#		what_meal.append(restaurant_list_complex[restaurants][0])

#for restaurants in haz_booz():
#	for time in range (len(haz_booz())):
#		if (restaurant_list_complex[time])[2] == time_check:
#			print(restaurant_list_complex[time])[0]

#for restaurants in range( len(restaurant_list_complex)):
#    if (restaurant_list_complex[restaurants])[1]  == 'y':
#        print(restaurant_list_complex[restaurants][0])

#for restaurants in haz_booz():
#	for r in range (len(restaurant_list_complex)):
#		if (restaurant_list_complex[r])[3] == 'american':
#			print( restaurant_list_complex[r])[0]
