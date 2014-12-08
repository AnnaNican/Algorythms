

##author: Anna Nicanorova
#Roman Numerals
#http://meetupresources.herokuapp.com/whiteboard.html

# Write a method that converts an integer to its Roman numeral equivalent, i.e., 476 => 'CDLXXVI'. 
# For reference, these are the building blocks for how we encode numbers with Roman numerals: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 
# Choose Between Old-school Roman numerals (no subtraction of 4s and 9s) 4 = IIII, 9 = VIIII etc. 
# Modern Roman numerals (subtraction) 4 = IV, 9 = IX, 14 = XIV, 40 = XL, 44 = XLIV, 90 = XC, 944 = CMXLIV



####Lookup table
integer = ["1", "5", "10", "50", "100", "500", "1000"]
roman = ["I", "V", "X", "L", "C", "D", "M"]
#make a dictionary
roman_nums = zip(integer, roman)
roman_nums_dict = dict(roman_nums)
#create ref
arabic = roman_nums_dict.keys()
roman = roman_nums_dict.values()
# print roman_nums_dict.get('1') Check dictionary call


####Input 
number = int(raw_input('Enter a number between 1 and 3999: '))


#algorythm formula

def convert_to_roman(number):
	global result
	#look up if there is a direct substiture
	if (number % 5 == 0 or number == 1): # look up if the number exists in the dictionary
		for i in arabic:
			if i == str(number):
				result =  roman_nums_dict.get(i)
				print result
				#deal with numbers mod 5 == 0, but not in lookup
	elif (number %10 == 0):
		result = str((number/10) * roman_nums_dict.get('10'))
		print result
	#deal with numbers less than 5 differently
	elif number < 5:
		#substitute numbers
		#for every one, put I
		quotent =  number/1
		result = str(number * "I")
		if quotent == 4:
			result = "IV"
		print result
	# or find the remained and find best aproximation
	else:
		remainder =  number % 5
		print remainder
		if remainder <= 3: # then search the number to the left and add 1's to the number
			closest_num_left = number - remainder
			closest_roman_num_left = roman_nums_dict.get(str(closest_num_left))
			print closest_num_left
			print closest_roman_num_left
			result = str(closest_roman_num_left + remainder*"I")
			print result
		elif remainder >3: #if remainder more than
			closest_num_right = number + 1
			closest_roman_num_right = roman_nums_dict.get(str(closest_num_right))
			print closest_num_right
			print closest_roman_num_right
			#place the number on the left of the closest_roman_num_right
			result = str("I" + closest_roman_num_right)
			print result 





convert_to_roman(20)



	# for roman, arabic in roman_nums_dict.iteritems():
	# 	if arabic == str(number):
	# 		print keys


#alternative wat to create a dict out of lists
# roman_nums = {}
# for i in range(len(roman)):
# 	roman_nums[roman[i]] = integer[i]