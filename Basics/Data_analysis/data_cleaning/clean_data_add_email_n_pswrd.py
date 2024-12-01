import re, random

def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter+=1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails

def get_necessary(ord_nums: list) -> str:
	return chr(random.choice(ord_nums))

def pwrd(pass_length:int) -> str:
	assert type(n) == int and n >=12
	lower = [x for x in range(ord('a'),ord('z')+1)]
	upper = [x for x in range(ord('A'),ord('Z')+1)]
	nums = [x for x in range(ord('0'), ord('9')+1)]
	symbols = [ord(symbol) for symbol in'!@#$%^&*()-+']
	altogether = lower+upper+nums+symbols
	result = []
	for cha in [lower, upper, nums, symbols]:
		result.append(get_necessary(cha))
	while len(result) != pass_length:
		result.append(get_necessary(altogether))
	random.shuffle(result)
	final = ''.join(result)
	return final

def re_check(my_string: str):
	pattern = r'^[a-zA-Z.-]+$'
	return re.match(pattern, my_string)

def check_len(entry: list) -> list:
	prepared = prepare_strings(entry)
	for cell in prepared[1:5]:								#from second line to -1
		#	cell = cell.strip()								#doubling
		if len(cell) < 1 or cell[0].islower() or (			#check len, first letter, letters in name,surname and city 
			cell != prepared[3] and not re_check(cell)):
			return False
	'''for letter in cell: 									#another implementation of the above
		if letter in '!@#$%^&*()_=+':						#or letter.isaplha()
			return False'''
	number = prepared[3]
	if not (len(number) == 7 and number.isdigit()):			#check phone number
		return False
	return prepared[1:3]

def prepare_strings(my_list: list) -> list:
	new_list = [x.strip() for x in my_list]
	return new_list
	
new_header = 'EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY\n'
names = []
text = []
result = []
na_data = []

with open ('task_file.txt') as f:
	for line in f.readlines()[1:]: #pay attention - it starts from 2nd line since readline had been called
		people = line.split(',')
		person = check_len(people)
		if person:
			names.append(person)
		text.append(people)
	
new_names = email_gen(names)
new_dict = {}
for n in range(len(names)):
	name = names[n][0] + names[n][1]
	new_dict[name] = new_names[n]

with open ('task_file.txt', 'w') as f1, open('bad_results.txt', 'w') as f2:

	f1.write(new_header)
	for line in text:
		line = [x.strip() for x in line]
		name_surname = line[1]+line[2]
		name_surname = name_surname.replace(' ','')
		if name_surname in new_dict:
			email = new_dict[name_surname]
			password = pwrd(12)
			result_line = [email]+[password]+line[1:]
			#line.append(password+'\n')
			my_string = ', '.join(result_line)
			my_string += '\n'
			result.append(my_string)
			f1.write(my_string)
		else:
			my_string = ', '.join(line)
			my_string+='\n'
			na_data.append(my_string)
			f2.write(my_string)

with open ('task_file1.txt') as f:
	for line in f.readlines():
		print(line)