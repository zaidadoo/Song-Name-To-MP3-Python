with open('nodownload.txt', 'w') as checkOut:
    checkOut.write('0')
checkIn = open("nodownload.txt", "r")
if checkIn.read()=='0':
	print("It is zero")
else:
	print("It is one")
input()