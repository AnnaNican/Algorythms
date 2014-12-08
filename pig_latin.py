

##author: Anna Nicanorova
# Pig Latin
#http://meetupresources.herokuapp.com/whiteboard.html

# Write a method the takes in a string and returns the pig latin equivalent. 
# Pig Latin takes the first consonant, moves it to the end of the word and places “ay” at the end. 
# If the string starts with a consonant do nothing. “pig” = “igpay”, “banana” = “ananabay”


##Input
original = raw_input('Enter a word:')
input_word = original.lower()



def pig_latin(word):
	for i, c in enumerate(word):
		#print i, c
		# form words beginning with consonants
		if c in ('a', 'e', 'i', 'o', 'u'):
			##If the words beginning with vowels, all you need to do is add "-yay"
			if i == 0:
				result = str(word + '-yay')
				print result
				break
			else:
				# form words beginning with consonants
				print(i)
				consonant = word[:i]
				print str("The consontant:" + consonant)
				newword =word[i:]
				result = str(newword + "-" + consonant+ "ay")
				print result
				break

	
pig_latin(input_word)