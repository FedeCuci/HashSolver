import hash_cracker_joshua

def settings():

	while True:
				choice = getInput('settings')

				elif choice == '4':
					input_file_choice = input('Would you like to use an input file? (y/n) ')
					if input_file_choice == 'y' or input_file_choice == 'Y':
						while True:
							current_input_file = getInput('settings/Input-file name > ')
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
				elif choice == '5':
					output_file_choice = getInput('Would you like to use an output file? (y/n) ')
					if output_file_choice == 'y' or output_file_choice == 'Y':
						output_file = True
						current_output_file = getInput('settings/Output-file name > ')
					else:
						print('')
				elif choice == 'list':
					print('''
	Type: "help" + "command name" for a list of available options.
	1. Algorithm
	2. Dicionary
	3. Verbose
	4. Input file
	5. Output file\n''')
				elif choice == 'status':
					status()
				elif choice == 'c' or choice == 'x':
					break
				elif choice == 'help':
					print('Type: "help command_name" for help')
				elif choice == 'help input file' or choice == 'help Input file' or choice == 'help 4':
					print('''
	Input file: a file containing several hashes to be cracked.
	Make sure there is one hash per line.\n''')
				elif choice == 'help output file' or choice == 'Outpute file' or choice == 'help 5':
					print('''
	Output file: the file that will be created with the final results
	of the program.\n''')
				elif choice == 'help dictionary' or choice == 'help Dicionary' or choice == 'help 2':
					print('''
	Dictionary: directory of the dictionary file that you would like
	to use to compute the hash/hashes provided.\n''')
				elif choice == 'help verbose' or choice == 'help Verbose' or choice == 'help 3':
					print('''
	Verbose: Show all the hashes being calculated live.''')
				elif choice == 'help algorithm' or choice == 'help Algorithm' or choice == 'help 1':
					print('''
	Algorithm: which hashing algorithm should the program use to crack the hash.
	This needs to be the same algorithm as the hash you are trying to crack''')
				else:
					print('Not an option')