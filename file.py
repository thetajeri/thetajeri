x = input('Please enter the status: ')
listed = [x]
while x.lower() != 'don':
	print('{} is x'.format(x))
	x = input('> ')
	listed.append(x)
print('\nYour list is here:\n{}'.format(listed))
