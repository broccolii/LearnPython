#number = 23
#running = True
#while running:
#	guess = int(raw_input('Enter an integer : '))
#	if guess == number:
#		print 'Congratulations, you guessed it.' # New block starts here print "(but you do not win any prizes!)" # New block ends here 
#		break	
#	elif guess < number:
#		print 'No, it is a little higher than that' # Another block
#	# You can do whatever you want in a block ...
#	else:
#		print 'No, it is a little lower than that'
#	# you must have guess > number to reach here
#		print 'Done'
#	# This last statement is always executed, after the if statement is executed
#else:
#	print 'dddddd'
#	

def printMax(a, b):
	if a > b:
		print a,"is maximum"
	else:
		print b,'is maximum'

printMax(4, 3)

def say(message, times = 1): print message * times

myArray = []
myArray.append('an item')
shoplist = ['apple', 'mange', 'carrot', 'banana']
print 'I have',len(shoplist), 'items to purcharse.'
shoplist.pop()
print shoplist
a = [1, 2, 3, 4]
print a[0:2]



name = "Swaroop"

if name.find('warasdf'):
	print 'yes'
	
if -1 == 1:
	print '-1123'
print name.find("asdfasdf")

print '-------------------------'
class Person: 
	def sayHi(self):
		print 'Hello, how are you?'

p = Person()
p.sayHi()

import os
print os.name