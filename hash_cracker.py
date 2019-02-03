import random
import hashlib
import os
import time

#Welcome message to display when file is run
welcome = '''
 _   _           _       _____                _             
| | | |         | |     /  __ \              | |            
| |_| | __ _ ___| |__   | /  \/_ __ __ _  ___| | _____ _ __ 
|  _  |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
| | | | (_| \__ \ | | | | \__/\ | | (_| | (__|   <  __/ |   
\_| |_/\__,_|___/_| |_|  \____/_|  \__,_|\___|_|\_\___|_|   
                                                            


For a list of commands, type: "help"
                                                            '''

os.system('clear')
print(welcome)
current_algorithm = ''
current_dictionary = '/usr/share/dict/words'
verbose = False

help_info = '''
	To start the program, type: start
	To get a list of the supported protocols, type: protocols
	To get the current dictionary list being used, type: dictionary
	To exit the program, type: c
	To change your settings, type: change
	To get the current status of your setting, type: status
	'''

supported_algorithms = 'MD5, SHA256, SHA512'

# Crack the hash
def crack(chosen_algorithm, hashtc, salt):
	
	# Loop over dictionary file
	start = time.time()
	for i in words:
		j = bytes(i + salt, 'utf-8')
		hashed = getattr(hashlib, chosen_algorithm)(j).hexdigest()
		if hashed == hashtc:
			end = time.time()
			print('Hash found, the password is: ', i)
			print('Time took to complete: ', (end-start))
			break

# Main
while True:
	
	try:
		beginning = input('> ')
	except KeyboardInterrupt:
		print('')
		exit()

	if beginning == 'help':
		print(help_info)
	elif beginning == 'start':
		# Hash to crack
		hash_to_crack = input('Hash to crack: ').lower()
		salt = input('Salt: ')

		# Open dictionary file if it exists
		try:
			words = open(current_dictionary).read().splitlines()
		except FileNotFoundError:
			print('Invalid file or directory\n')

		# Run crack() based on algorithm
		if current_algorithm == 'md5':
			crack('md5', hash_to_crack, salt)
			#print('Hash was not found')
		elif current_algorithm == 'sha256':
			crack('sha256', hash_to_crack, salt)
			#print('Hash was not found...')
		elif current_algorithm == 'sha512':
			crack('sha512', hash_to_crack, salt)
			
			#print('Hash was not found...')
		else:
			print('Hash algorithm not supported, type: "algorithms", to check the supported hash functions')

	elif beginning == 'algorithms':
		print(supported_algorithms)
	elif beginning == 'dictionary':
		print(curent_dictionary)
	elif beginning == 'clear':
		os.system('clear')
	elif beginning == 'c':
		exit()
	elif beginning == 'change':
		print('''
1. Algorithm
2. Dicionary
3. Verbose\n''')

		# Change settings category 
		while True:
			try:
				choice = input('change > ')
			except KeyboardInterrupt:
				print('')
				exit()

			if choice == '1':
				current_algorithm = input('change/algorithm > ').lower()
				break
			elif choice == '2':
				current_dictionary = input('change/dictionary > ')
				break
			elif choice == '3':
				verbose = True
			else:
				print('Not an option')
	elif beginning == 'status':
		print('Dicionary file: ', current_dictionary)
		print('Algorithm: ', current_algorithm, '\n')
	elif beginning == 'info':
		print('''
Hash cracker takes a hash and appends the provided salt to it.
After that, it loops through a dictionary file and hashes 
every single word using the hash algorithm provided. After
each hash, it checks whether it matches the hash to be cracked.\n''')
	else:
		print('Unknown command')
		