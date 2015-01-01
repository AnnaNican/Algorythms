
from random import randint

##author: Anna Nicanorova
# Shuffle
#http://meetupresources.herokuapp.com/whiteboard.html


#Without using a shuffle or sort write your own shuffle method for an array. 
#The method will take an array and returns a new array with all of the elements in a random order. 
#One important property of a good shuffle method is that every permutation is equally likely.

array = [1,2,3,4,5]
length = len(array)

for i,j in enumerate(array):
	print i
	print j
	# generate a random element between zero and length
	new_pos = randint(0,length)
	# for every j replace i with a random number
	j = new_pos
	print j
	# if permutation has already occured, redo the generation