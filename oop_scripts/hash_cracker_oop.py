import hashlib
import time
import os

class CrackHash:

	supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']

	def __init__(self, algorithm, dictionary, crack, verbose):
		self.algorithm = algorithm
		self.dictionary = dictionary
		self.crack = crack
		self.verbose = verbose

		def input_file(self):
			pass

		def output_file(self):
			try:
				if self.output_file[-4:] == '.txt':
					f = open(self.output_file, 'x')
				else:
					f = open(self.output_file + '.txt', 'x')
			except FileExistsError:
				exists = input('File already exists, replace it? (y/n) ')
				if exists == 'y' or exists == 'Y':
					if self.output_file[-4:] == '.txt':
						f = open(self.output_file, 'w+')
					else:
						f = open(self.output_file + '.txt', 'w+')
					f.write('The Word for the hash {} with salt {} is: {}'.format(self.hash, self.salt, word))
					f.close()
					print('\nEverything was written to file succesfully!')
				elif exists == 'n' or exists == 'N':
					print('Please change the output file name in settings')	
	else:
		print('\nEverything was written to {} succesfully\n'.format(output_file))
		f.write('The Word for the hash {} with salt {} is: {}'.format(hashed, salt, word))

		def central(self):
			pass

		def settings(self):
			pass	

		def crack(self):
			if self.algorithm not in supported_algorithms:
				print('You must choose a supported algorithm: sha512, sha256, md5')
				return None

			n = 0

			start = time.time()

			for i in dictionary:
				n += 1
				j = bytes(i + salt, 'utf-8')
				hashed = getattr(hashlib, chosen_algorithm)(j).hexdigest()
				# Verbose could be checked here and improve readability but would likely slow down the program
				if self.verbose is True:
					print(hashed) # This is the only extra line for verbose... How can it be improved?
				if hashed == hash_to_crack:
					end = time.time()
					print('\nHash found, the password is: ', i)
					print('\nTime took to complete: ', (end-start))
					print('Words tried: ', n)
					if self.output_file:
						make_output_file(i, self.output_file, self.salt, self.hash)
						return True
						break
					else:
						return True
						break
			
			print('Hash was not found in table. Try another table?')

def main():
	while True: 
		
		beginning = getInput('')
		#if beginning in ['help', 'crack','algorithms', 'clear', 'c', 'status', 'info']:
		#	commands[beginning]()
			# run command
		#else:
		#	print('Unknown command')

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


if __name__ == '__main__':
	main()