


#Multiple of3&5
#https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

array = list(range(0, 1000))
numbers = []

for i,j in enumerate(array):
	if (i % 3 == 0) or (i % 5 == 0):
		numbers.append(i)

result = sum(numbers)
print result
