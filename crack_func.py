import hash_cracker_joshua as main
import settings
import time
import hashlib

# Function to make output file if requested
def make_output_file(word, output_file, salt, hashed):
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
			f.write('The Word for the hash {} with salt {} is: {}'.format(hashed, salt, word))
			f.close()
			print('\nEverything was written to file succesfully!')
		elif exists == 'n' or exists == 'N':
			print('Please change the output file name in settings')	
	else:
		print('\nEverything was written to {} succesfully\n'.format(output_file))
		f.write('The Word for the hash {} with salt {} is: {}'.format(hashed, salt, word))
		f.close()

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
