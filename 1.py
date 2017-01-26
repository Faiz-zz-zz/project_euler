total = 0
array = [3, 6, 9, 12, 15, 18, 21, 24, 27]
for i in range(1, 1000):
	num = sum(map(int, list(str(i))))
	if ((num in array) or (i%10 == 5 or i%10 == 0)):
		total += i
		print i

print total		
#answer  234168