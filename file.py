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



import glob


def number_tries(file_name):
	dir_list = []
	for file in glob.glob("*.txt"):
		dir_list.append(file)


	if file_name in dir_list:
		file = open(file_name,'r')
		line_list = file.readlines()
		file.close()

		status = False
		# in normal status, we don't have such line

		for line in line_list:
			line_chrs = line.strip().strip()
			try:
				if line_chrs[0].isnumeric() and 'times we spend on this project...' in ' '.join(line_chrs[1:]):
					status = True
					# it means, now, we have the line,
					#  wich have this txt inside: "***** times we spend on this project..."
					break
			except(IndexError):
				pass
		if status == True:
			for line in line_list:
				line_chrs = line.strip().split()
				try:
					if line_chrs[0].isnumeric() and 'times we spend on this project...' in ' '.join(line_chrs[1:]):
						try_counter = str(int(line_chrs[0]) + 1)
				except(IndexError):
					pass
		else:
			file = open(file_name , 'w')
			try_counter = '1'
			file.write('')
			file.close()
		# untile here, we have number of tries.
	else:
		try_counter = '1'
		file = open(file_name,'x')
		file.close()
	# and at the end, we have number of tries
	# as a log file.
	return try_counter.zfill(5)

try_counter = number_tries('result.txt')