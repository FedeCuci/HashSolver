import random
import hashlib
import os
import time
import settings
import crack_func

def getInput(text):
	try:
		choice = input('{}> '.format(text))
	except KeyboardInterrupt:
		print('')
		exit()
	return choice

# actions = {
# 	'settings': settings,
# 	'1' : algorithm_option,
# 	'2': algorithm_option,
# 	'3' : algorithm_option
# }

# cmd = input('Enter Command: ')

# if cmd in actions.keys:
# 	actions[cmd](val)

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

# Global variables
os.system('clear') # Clear the screen
print(welcome)

current_algorithm = ''
salt = ''
current_dictionary = '/usr/share/dict/words'
current_output_file = ''
hash_to_crack = ''
output_file = ''
verbose = False
input_file = ''
supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']

# Print out the current status of settings
def status(verbose=False, input_file='', salt='', dictionary='/usr/share/dict/words', chosen_algorithm='', output_file=False):
	print('\nDictionary file: ', dictionary)
	print('Algorithm: ', chosen_algorithm)
	print('Verbose: ', str(verbose))
	print('Output file: ', output_file)
	print('Salt: ', salt)
	print('Input file: ', input_file, '\n')

help_info = '''
 Crack: crack your hash/es with current settings
 Settings: change your settings
 Status: Get an overview of your current settings
	'''

# def printStatement():
# 	pass
# commands = {
# 		'help': printStatement, 
# 		'crack': crack_func.general,
# 		'algorithms', 'clear', 'c', 'status', 'infor'}
def main(verbose=False, input_file='', salt='', dictionary='/usr/share/dict/words', hash_to_crack='', chosen_algorithm='', output_file=False):

	dictionary = open(current_dictionary).read().splitlines()

	while True: 
		
		beginning = getInput('')
		# if beginning in ['help', 'crack','algorithms', 'clear', 'c', 'status', 'info']:
		# 	commands[beginning]()
		# else:
		# 	print('Unknown command')

		if beginning == 'help':
			print(help_info)
		elif beginning == 'settings':
			print('''
	Type: "help" + "command name" for a list of available options.
	1. Algorithm
	2. Input file
	3. Verbose
	4. Dictionary
	5. Output file
	6. Salt\n''')

			settings.settings(verbose, input_file, salt, dictionary, hash_to_crack, chosen_algorithm, output_file)

			# Change settings category 
			
		elif beginning == 'crack':

			if input_file:
				crack_func.input_file(chosen_algorithm, dictionary, input_file, output_file, verbose)
			else:
				crack_func.general(verbose, input_file, salt, dictionary, hash_to_crack, chosen_algorithm, output_file)

			# # Run crack() based on algorithm
			# if chosen_algorithm in supported_algorithms:
			# 	crack(chosen_algorithm, verbose, input_file, output_file)
			# else:
			# 	print('You must choose a hashing algorithm in: settings/algorithm')

		elif beginning == 'algorithms':
			print(supported_algorithms)
		elif beginning == 'clear':
			os.system('clear')
			print(welcome)
		elif beginning == 'c':
			exit()
		elif beginning == 'status':
			status(verbose, input_file, salt, dictionary, chosen_algorithm, output_file)
			
		elif beginning == 'info':
			print('''
	Hash cracker takes a hash and appends the provided salt to it.
	After that, it loops through a dictionary file and hashes 
	every single word using the hash algorithm provided. After
	each hash, it checks whether it matches the hash to be cracked.\n''')
		else:
			print('Unknown command')

if __name__ =='__main__':
	main(verbose, input_file, salt, current_dictionary, hash_to_crack, current_algorithm, output_file)