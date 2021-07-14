x = input('Please enter the status: ')
listed = [x]
while x.lower() != 'don':
	print('{} is x'.format(x))
	x = input('> ')
	listed.append(x)
del listed[-1]
print('\nYour list is here:\n{}'.format('-'.join(listed)))

counter = 0
file = open('result.txt' , 'wt')
file.write('')
file.close()
file = open('result.txt', 'at')
for this_one in listed:
	text = '{} {}\n'.format(counter,this_one)
	file.write(text)
	counter += 1
file.close()
