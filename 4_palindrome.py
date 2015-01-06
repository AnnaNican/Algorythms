
#Palindromic Number
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit 
# numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


result = []

#find palindrome
def is_palindrome(n):
	s = str(n)
	return s == s[::-1]

#find all palindromes produced by 3-digit numbers
for x in range(100, 1000):
	for y in range(100, 1000):
		product = x*y
		if is_palindrome(product) == True:
			result.append(product)
			print x
			print y


lastelement_id = len(result) -1
result = sorted(result)
answer = result[lastelement_id]

print answer