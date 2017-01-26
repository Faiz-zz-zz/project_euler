import math
prime_numbers = [2]
def primality(number, prime_numbers):
	for i in range(3, number, 2):
		counter = 0
		prime = 0
		while counter == 0 and prime < len(prime_numbers):
			if i%prime_numbers[prime] == 0:
				counter += 1
			prime += 1
		# print counter, i		
		if counter == 0:
			prime_numbers.append(i)
		print i	

primality(100000, prime_numbers)
num = 600851475143
for i in prime_numbers:
	if num%i == 0:
		while num%i == 0:
			print i
			num = num/i

print num			