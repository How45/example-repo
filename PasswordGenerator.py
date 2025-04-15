import string
import random
# 051.9X2[39g3N2_{F9mM

def listCase(String):
	listCase = []

	for i in range(len(String)):
		listCase.append(String[i])

	return listCase

def randomPass(upperCase,lowerCase,digitsCase,punctuationCase):
	flag = 0
	password = ""

	while flag != 20:
		r = random.randrange(0,4)

		if r == 0:
			password = password + upperCase[random.randrange(len(upperCase))]
			flag += 1

		elif r == 1:
			password = password + lowerCase[random.randrange(len(lowerCase))]
			flag += 1

		elif r == 2:
			password = password + digitsCase[random.randrange(len(digitsCase))]
			flag += 1

		elif r == 3:
			password = password + punctuationCase[random.randrange(len(punctuationCase))]
			flag += 1

	return password

def reverse(a,s):
	t = False
	num = 0
	while t == False:

		for i in range(len(a)-1):
			num = a[i] + num
			print(a[i])
			print(num)
			

			if num == 9:
				break

			elif num > 9:
				num = 0

			elif a[i] == a[len(a)-1]:
				break

			else:
				print(" ")
		t = True
	return True

	

def main():
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	digits = string.digits
	punctuation = string.punctuation

	upperCase = listCase(upper)
	lowerCase = listCase(lower)
	digitsCase = listCase(digits)
	punctuationCase = listCase(punctuation)

	print(randomPass(upperCase,lowerCase,digitsCase,punctuationCase))

if __name__ == '__main__':
	main()
