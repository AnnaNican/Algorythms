
#LargestPrime
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

#find factors
number = 600851475

factors = []
for i in range(1, number):
	if number % i == 0:
		factors.append(i)


#find factors that are prime
primefactors = []

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for i in factors:
	if is_prime(i) == True:
		primefactors.append(i)

result = max(primefactors)
print result