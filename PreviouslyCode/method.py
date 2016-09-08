def factorial(count):
	if num == 1:
		return 1
	elif num == 0: 
		return 0
	else:
		return num * factorial(num - 1)
	
def fibonacci(num):
	if num < 1:
		print('输入有误')
		return -1
	elif num == 1 or num == 2:
		return 1
	else:
		return fibonacci(num - 1) + fibonacci(num - 2)
count = 0
def hanoi(n, x, y ,z):
	global count
	count += 1
	print('count == ',count)
	if n == 1:
		print (x, '-->', z ,count)
	else:
		hanoi(n-1, x, z, y)
		print(x, '-->', z, count)
		hanoi(n-1, y, x, z)
	
print(hanoi(18, 'x', 'y', 'z'))
