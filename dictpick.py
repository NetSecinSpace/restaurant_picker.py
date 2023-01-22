import random
import optparse
#from randomdict import RandomDict

#rest_dict = { 'Dict1': {'name': 'MT Club', 'alcohol': 'y'},
#{ 'Dict2': {'name': 'Kobe', 'alcohol': 'n'},
#{ 'Dict3': {'name': 'Mighty Mo', 'alcohol': 'y'}
#}}}
#print(rest_dict)


rest_dict = { '1': {'name': 'MT Club', 'alcohol': 'y'},
'2': {'name': 'Kobe', 'alcohol': 'n'}}
#print("\nNested dictionary 2-")
#print(rest_dict)
#print(rest_dict['2']['alcohol'])



# alc_check = 'y'
#time_check = 'lunch'

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

#	if not options.meal:
#		parser.error("[-] dude what meal is it? (breakfast, lunch, dinner)")
#	elif not options.alc_check:
#		parser.error("[-] do you want to drink? (y,n)")
	return options

options = get_args()
print("alcohol arg")
print(options.alc_check)
print("meal arg")
print(options.meal)

print("items")
print(rest_dict.items())
print("keys")
print(rest_dict.keys())
print("values")
print(rest_dict.values())

print("rest list")
rest_list=list(rest_dict.values())
print(rest_list)

print("random")
r = random.choice(rest_list)
print(r)

#------------------------
#r = RandomDict() # use it just like a regular python dict
#r['a'] = True
#r['b'] = 2
#
#print(r.random_key())
#print(r.random_value())
#print(r.random_item())

#cnn_arch=list(cnn_arch.values())[]

#look at this
#https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key

#for key in rest_dict:
#	print "the key name is" + key + "and its value is" + rest_dict[key]

#def haz_booz():
#	booze_check = []
#	for names in range (rest_dict):
#		if (rest_dict.values()[1] == options.alc_check:
#			print(rest_dict)
#	return (booze_check)

#haz_booz()

#=====
##def haz_booz():
##	booze_check = []
##	for restaurants in range( len(restaurant_list_complex)):
##		if (restaurant_list_complex[restaurants])[1]  == options.alc_check:
##			booze_check.append(restaurant_list_complex[restaurants][0:3])
##			print(restaurant_list_complex[restaurants][0:3])
##	return (booze_check)

##haz_booz()

#def big():
#	all_test = []#
#	for restaurants in range( len(restaurant_list_complex)):
#		if (restaurant_list_complex[restaurants])[1]  == options.alc_check: and
#		if (restaurant_list_complex[restaurants])[2] == options.meal:
#			all_test.append(restaurant_list_complex[restaurants][0])
#			print(all_test)



#if options.meal == ((restaurant_list_complex)[2]):
#	print(restaurant_list_complex)

##for meal_time in range(len(restaurant_list_complex)):
##	meal_check = []
##	if (restaurant_list_complex[meal_time])[2] == options.meal:
##		meal_check.append(restaurant_list_complex[meal_time][0])
##		print(restaurant_list_complex[meal_time][0:2])
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
