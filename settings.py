import main
import os
import crack_func

def settings(verbose=False, input_file='', salt='', dictionary='/usr/share/dict/words', hash_to_crack='', chosen_algorithm='', output_file=False):

	print('Type \'help\' for a list of commands')

	supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']
	current_directory = os.getcwd()
	help_text = '''
Possible options:
	1. Choose your algorithm
	2. Choose your dictionary file
	3. Verbose
	4. Input file containing hashes to crack
	5. Output file to store the cracked hashed value
	6. Salt
	Help + command/number: Further help specifc to each command
	Status: Current status of your settings
	'''

	while True:
		val = main.getInput('settings')

		if val == '1' or val == 'algorithm':
			chosen_algorithm = main.getInput('settings/algorithm').lower()
		elif val == '2' or val == 'input file':
			while True:
				input_file_choice = main.getInput('Would you like to use an input file? (y/n)')

				if input_file_choice == 'y' or input_file_choice == 'yes':
					input_file = main.getInput('Location of hash file')

					try:
						input_file = open(input_file).read().splitlines()
						print('Hash file added succesfully')
						break

					except FileNotFoundError:
						print('File does not exist\n')
						break
				else:
					print('Invalid option')
					break

		elif val == '3' or val == 'verbose':
			if verbose == True:
				verbose = False
			else:
				verbose = True
			print('Verbose: ', str(verbose))

		elif val == '4' or val == 'dictionary':
			dictionary = main.getInput('Would you like to use an input file? (y/n)')
			if dictionary == 'y' or dictionary == 'Y':
				while True:
					current_dictionary = main.getInput('settings/Input-file name')
					# Open dictionary file if it exists
					try:
						# Print current directory to user
						print(current_directory + '/' + current_dictionary)
						# Read file for the hashes
						dictionary = open(current_dictionary).read().splitlines()
					except FileNotFoundError:
						print('Invalid dictionary directory\n')
						break

					if current_file[-4:] != '.txt':
						print('You must enter a ".txt" file.')
					else:
						words = open(current_file).read().splitlines()
						break
					
			else:
				print('')
		elif val == '5' or val == 'output file':
			output_file_choice = main.getInput('Would you like to use an output file? (y/n)')
			if output_file_choice == 'y' or output_file_choice == 'Y':
				output_file = main.getInput('settings/Output-file name (txt)')
			else:
				print('')
		elif val == '6' or val == 'salt':
			salt = main.getInput('salt').lower()
		elif val == 'status':
			status()
		elif val == 'c' or val == 'x':
			main.main(verbose, input_file, salt, dictionary, hash_to_crack, chosen_algorithm, output_file)
		elif val == 'help':
			print('Type: "help command_name" for help')
		elif val == 'help input file' or val == 'help 4':
			print('''
Input file: a file containing several hashes to be cracked.
Make sure there is one hash per line.\n''')
		elif val == 'help output file' or val == 'help 5':
			print('''
Output file: the file that will be created with the final results
of the program.\n''')
		elif val == 'help dictionary' or val == 'help 2':
			print('''
Dictionary: directory of the dictionary file that you would like
to use to compute the hash/hashes provided.\n''')
		elif val == 'help verbose' or val == 'help 3':
			print('''
Verbose: Show all the hashes being calculated live.''')
		elif val == 'help algorithm' or val == 'help 1':
			print('''
Algorithm: which hashing algorithm should the program use to crack the hash.
This needs to be the same algorithm as the hash you are trying to crack''')
		elif val == 'help':
			print(help_text)
		else:
			print('Not an option')