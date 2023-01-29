import random
import argparse

restaurant_list = (
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
#example of line('MT Club', 'y', 'breakfast', 'american')

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-a", "--alcohol", dest="alc_check", default="n", help="(y/n) on booze for this meal")
	parser.add_argument("-m", "--meal", dest="meal", help="What meal of the day is it")
	options = parser.parse_args()
	#check to make sure that the meal time is selected since there is no default on that field
	if not options.meal:
		parser.error("[--] dude what meal is it? (breakfast, lunch, dinner) Type -m as an arg")
	return options

options = get_args()

def filter_restaurants(restaurant_list, options):
	# Find all rows that match the criteria
	matching_rows = [row[0] for row in restaurant_list if row[2] == options.meal and row[1] == options.alc_check]
	return matching_rows

def pick_random_restaurant(restaurant_list, options):
	# Narrow down the list of restaurants based on the options
	filtered_list = filter_restaurants(restaurant_list, options)
	# Pick a random value from the filtered list
	if filtered_list:
		random_restaurant = random.choice(filtered_list)
		return random_restaurant
	else:
		return "No restaurants matching the criteria were found."

random_restaurant = pick_random_restaurant(restaurant_list, options)

print(random_restaurant)

