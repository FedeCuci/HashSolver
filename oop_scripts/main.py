import hashlib
import crypt
import time
import os
import crack

class cliStuff:

	supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']

	def __init__(self, algorithm='', dictionary='/usr/share/dict/words', input_file='', hashc='', output_file='', salt='', verbose=False):
		self.algorithm = algorithm
		self.dictionary = dictionary
		self.input_file = input_file
		self.hashc = hashc
		self.output_file = output_file
		self.salt = salt
		self.verbose = verbose

	def getInput(self, text):
		try:
			self.choice = input('{} > '.format(text))
		except KeyboardInterrupt:
			print('')
			exit()
		return self.choice

	def status(self):
		print('\nDictionary file: ', self.dictionary)
		print('Algorithm: ', self.algorithm)
		print('Verbose: ', str(self.verbose))
		print('Output file: ', self.output_file)
		print('Salt: ', self.salt)
		print('Input file: ', self.input_file, '\n')

	def run(self):
		help_text = '''
Possible options:
	1. Choose your algorithm
	2. Choose your hash/input file
	3. Verbose
	4. Choose your dictionary file
	5. Output file to store the cracked hashed value
	6. Salt

	Help + command/number: Further help specifc to each command
	Status: Current status of your settings
	'''

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
		self.dictionary = open(self.dictionary).read().splitlines()

		while True: 

			
			supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']
			current_directory = os.getcwd()
			val = self.getInput('')

			if val == '1' or val == 'algorithm':
					self.algorithm = self.getInput('settings/algorithm').lower()
			elif val == '2' or val == 'input file':
				while True:
					input_file_choice = self.getInput('Would you like to use a custom hash file? (y/n)')

					if input_file_choice == 'y' or input_file_choice == 'yes':
						self.input_file = self.getInput('Location of hash file')

						try:
							self.input_file = open(self.input_file).read().splitlines()
							# self.input_file = open(os.path.join(directory, self.input_file)).read().splitlines()  
							print('Hash file added succesfully')
							break

						except FileNotFoundError:
							print('File does not exist\n')
							break
					else:
						print('Input file was not added')
						break

			elif val == '3' or val == 'verbose':
				if self.verbose == True:
					self.verbose = False
				else:
					self.verbose = True
				print('Verbose: ', str(self.verbose))

			elif val == '4' or val == 'dictionary':
				dictionary_choice = self.getInput('Would you like to use a custom dictionary file?')
				if dictionary_choice == 'y' or dictionary_choice == 'Y':
					while True:

						# print('Current dictionary:' + current_directory + '/' + self.dictionary)

						self.dictionary = self.getInput('settings/Custom dictionary')
						# Open dictionary file if it exists
						try:
							# Print current directory to user
							
							# Read file for the hashes
							self.dictionary = open(self.dictionary).read().splitlines()
						except FileNotFoundError:
							print('Invalid dictionary directory\n')
							break
						else:			
							if self.dictionary[-4:] != '.txt':
								print('You must enter a ".txt" file.')
							break
						
				else:
					print('Dictionary file was not changed.')

			elif val == '5' or val == 'output file':
				output_file_choice = self.getInput('Would you like to use an output file? (y/n)')
				if output_file_choice == 'y' or output_file_choice == 'Y':
					self.output_file = self.getInput('settings/Output-file name (txt)')
				else:
					print('')
			elif val == '6' or val == 'salt':
				self.salt = self.getInput('salt').lower()
			elif val == 'status':
				self.status()
			elif val == 'c' or val == 'x':
				exit()
			elif val == 'help input file' or val == 'help 2':
				print('''
	Input file: a file containing several hashes to be cracked.
	Make sure there is one hash per line.\n''')
			elif val == 'help output file' or val == 'help 5':
				print('''
	Output file: the file that will be created with the final results
	of the program.\n''')
			elif val == 'help dictionary' or val == 'help 4':
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
	
			#if val in ['help', 'crack','algorithms', 'clear', 'c', 'status', 'info']:
			#	commands[val]()
				# run command
			#else:
			#	print('Unknown command')

			elif val == 'help':
				print(help_text)
				
			elif val == 'crack':
				if self.input_file:
					current = crack.Crack(self.algorithm, self.dictionary, self.input_file, self.hashc, self.output_file, self.salt, self.verbose)
					current.with_input_file()
				else:
					current = crack.Crack(self.algorithm, self.dictionary, self.input_file, self.hashc, self.output_file, self.salt, self.verbose)
					current.crack()

			elif val == 'algorithms':
				print(supported_algorithms)
			elif val == 'clear':
				os.system('clear')
				print(welcome)				
			elif val == 'info':
				print('''
		Hash cracker takes a hash and appends the provided salt to it.
		After that, it loops through a dictionary file and hashes 
		every single word using the hash algorithm provided. After
		each hash, it checks whether it matches the hash to be cracked.\n''')
			elif val == 'hash' or val == '7':
				self.hashc = self.getInput('Hash to crack')
				if self.hashc not in supported_algorithms:
					print('please enter a valid algorithm')
			else:
				print('Unknown command')

def main():
	current = cliStuff()
	current.run()

if __name__ == '__main__':
	main()