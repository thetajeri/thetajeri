#x = input('Please enter the status: ')
#listed = [x]
#while x.lower() != 'don':
#	print('{} is x'.format(x))
#	x = input('> ')
#	listed.append(x)
#del listed[-1]
#print('\nYour list is here:\n{}'.format('-'.join(listed))
#counter = 0
#file = open('result.txt' , 'wt')
#file.write('')
#ile.close()
#file = open('result.txt', 'at')
#or this_one in listed:
#	text = '{} {}\n'.format(counter,this_one)
#	file.write(text)
#	counter += 1
#file.close()



from os import listdir


def number_tries(file_name):
	dir_list = listdir()

	if 'result.txt' in dir_list:
		file = open('result.txt','r')
		line_list = file.readlines()
		file.close()

		status = False
		for line in line_list:
			line_chrs = line.strip().strip()
			try:
				if line_chrs[0].isnumeric() and line_chrs[1] == 'times' and line_chrs[2] == 'we':
					status = True
					break
			except(IndexError):
				pass
		if status == True:
			for line in line_list:
				line_chrs = line.strip().split()
				try:
					if line_chrs[0].isnumeric() and line_chrs[1] == 'times' and line_chrs[2] == 'we':
						try_counter = str(int(line_chrs[0]) + 1)
				except(IndexError):
					pass
		else:
			file = open('result.txt' , 'a')
			try_counter = '00001'
			file.write('\n{} times we spend on this project.\n\n'.format(try_counter))
			file.close()
			try_counter = str(int(try_counter) + 1).zfill(5)
		# untile here, we have number of tries.
	else:
		try_counter = '0'
		file = open('result.txt','x')
		file.close()
	# and at the end, we have number of tries
	# as a log file.
	return try_counter.zfill(5)

print(number_tries('result.txt'))
