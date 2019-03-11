import hash_cracker_joshua

def settings():

	current_algorithm = ''
	current_salt = ''
	current_dictionary = '/usr/share/dict/words'
	current_output_file = ''
	hash_to_crack = ''
	verbose = False
	output_file = False
	supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']

	while True:
		# print('thhis is:')
		val = hash_cracker_joshua.getInput('settings')

		if val == '1':
			current_algorithm = hash_cracker_joshua.getInput('settings/algorithm').lower()
		elif val == '2':
			current_dictionary = hash_cracker_joshua.getInput('settings/dictionary')
		elif val == '3':
			if verbose == True:
				verbose = False
			else:
				verbose = True
			print('Verbose: ', str(verbose))

		elif val == '4':
			input_file_choice = hash_cracker_joshua.getInput('Would you like to use an input file? (y/n)')
			if input_file_choice == 'y' or input_file_choice == 'Y':
				while True:
					current_input_file = hash_cracker_joshua.getInput('settings/Input-file name')
					# Open dictionary file if it exists
					try:
						words = open(current_dictionary).read().splitlines()
					except FileNotFoundError:
						print('Invalid dictionary directory\n')
						break

					if current_input_file[-4:] != '.txt':
						print('You must enter a ".txt" file.')
					else:
						words = open(current_dictionary).read().splitlines()		
					
			else:
				print('')
		elif val == '5':
			output_file_choice = hash_cracker_joshua.getInput('Would you like to use an output file? (y/n)')
			if output_file_choice == 'y' or output_file_choice == 'Y':
				output_file = True
				current_output_file = hash_cracker_joshua.getInput('settings/Output-file name')
			else:
				print('')
		elif val == '6':
			current_salt = hash_cracker_joshua.getInput('salt')
		elif val == 'list':
			print('''
Type: "help" + "command name" for a list of available options.
1. Algorithm
2. Dicionary
3. Verbose
4. Input file
5. Output file\n''')
		elif val == 'status':
			status()
		elif val == 'c' or val == 'x':
			hash_cracker_joshua.main(verbose, current_salt, current_dictionary, hash_to_crack, current_algorithm, output_file)
			print('>>>>>>>>>>>>>>>>>>>>', current_algorithm)
		elif val == 'help':
			print('Type: "help command_name" for help')
		elif val == 'help input file' or val == 'help Input file' or val == 'help 4':
			print('''
Input file: a file containing several hashes to be cracked.
Make sure there is one hash per line.\n''')
		elif val == 'help output file' or val == 'Outpute file' or val == 'help 5':
			print('''
Output file: the file that will be created with the final results
of the program.\n''')
		elif val == 'help dictionary' or val == 'help Dicionary' or val == 'help 2':
			print('''
Dictionary: directory of the dictionary file that you would like
to use to compute the hash/hashes provided.\n''')
		elif val == 'help verbose' or val == 'help Verbose' or val == 'help 3':
			print('''
Verbose: Show all the hashes being calculated live.''')
		elif val == 'help algorithm' or val == 'help Algorithm' or val == 'help 1':
			print('''
Algorithm: which hashing algorithm should the program use to crack the hash.
This needs to be the same algorithm as the hash you are trying to crack''')
		else:
			print('Not an option')