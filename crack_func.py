import hash_cracker_joshua as main
import settings
import time
import hashlib

# Function to make output file if requested
def make_output_file(results, salts, output_file='cracked_hashes.txt'):

	n = 0

	try:
		if output_file[-4:] == '.txt':
			f = open(output_file, 'x')
		else:
			f = open(output_file + '.txt', 'x')
	except FileExistsError:
		exists = input('File already exists, replace it? (y/n) ')
		if exists == 'y' or exists == 'Y':
			if output_file[-4:] == '.txt':
				f = open(output_file, 'w+')
			else:
				f = open(output_file + '.txt', 'w+')
			for i, j in results.items():
				f.write('The Word for the hash {} with salt {} is: {}\n'.format(i, salts[n], j))
				n += 1
			print('\nEverything was written to file succesfully!')
			f.close()
		elif exists == 'n' or exists == 'N':
			print('Please change the output file name in settings')	
	else:
		for i, j in results.items():
			f.write('The Word for the hash {} with salt {} is: {}\n'.format(i, salts[n], j))
			n += 1

		print('\nEverything was written to {} succesfully\n'.format(output_file))
		f.close()

def input_file(chosen_algorithm, dictionary, input_file, output_file, verbose):

	m = 0
	n = 0
	results = {}
	salts = []

	start = time.time()
	
	for i in input_file:
		x = i.split(' ')
		to_hash = x[0]
		salt = x[1]
		print('Hashes to calculate: {}'.format(len(input_file) - m))
		m += 1
		l = to_hash.lower()
		for k in dictionary:
			n += 1
			j = bytes(k + salt, 'utf-8')
			hashed = getattr(hashlib, chosen_algorithm)(j).hexdigest()
			if verbose:
				print(hashed)
			if hashed == l:
				end = time.time()
				print('\nHash found, the password is: ', k)
				print('\nTime took to complete: ', (end-start))
				print('Words tried: ', n)
				results[hashed] = k
				salts.append(salt)

	if output_file:
		make_output_file(results, salts, output_file)
		return True
	else:
		make_output_file(results, salts)
		return True


def general(verbose, input_file, salt, dictionary, hash_to_crack, chosen_algorithm, output_file):

	if chosen_algorithm not in main.supported_algorithms:
		print('You must choose a supported algorithm: sha512, sha256, md5')
		return None

	hash_to_crack = main.getInput('Hash to crack')

	n = 0

	start = time.time()

	for i in dictionary:
		n += 1
		j = bytes(i + salt, 'utf-8')
		hashed = getattr(hashlib, chosen_algorithm)(j).hexdigest()
		# Verbose could be checked here and improve readability but would likely slow down the program
		if verbose is True:
			print(hashed) # This is the only extra line for verbose... How can it be improved?
		if hashed == hash_to_crack:
			end = time.time()
			print('\nHash found, the password is: ', i)
			print('\nTime took to complete: ', (end-start))
			print('Words tried: ', n)
			if output_file:
				make_output_file(i, output_file, salt, hash_to_crack)
				return True
				break
			else:
				return True
				break
	
	print('Hash was not found in table. Try another table?')
