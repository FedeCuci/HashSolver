from clistuff2 import cliStuff
import hashlib
import time
import os

class Crack:

	supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']


	def __init__(self, algorithm, dictionary, input_file, hashc, output_file, salt, verbose):
		self.algorithm = algorithm
		self.dictionary = dictionary
		self.input_file = input_file
		self.hashc = hashc
		self.output_file = output_file
		self.salt = salt
		self.verbose = verbose

	def crack(self):

			if self.algorithm not in self.supported_algorithms:
				print('You must choose a supported algorithm: sha512, sha256, md5')
				return None

			n = 0

			start = time.time()
			
			for i in self.dictionary:
				n += 1
				j = bytes(i + self.salt, 'utf-8')
				hashed = getattr(hashlib, self.algorithm)(j).hexdigest()
				# Verbose could be checked here and improve readability but would likely slow down the program
				if self.verbose is True:
					print(hashed) # This is the only extra line for verbose... How can it be improved?
				if hashed == self.hashc:
					end = time.time()
					print('\nHash found, the password is: ', i)
					print('\nTime took to complete: ', (end-start))
					print('Words tried: ', n)
					if self.output_file:
						self.make_output_file(i, self.output_file, self.salt, self.hash)
						return True
						break
					else:
						return True
						break
			
			print('Hash was not found in table. Try another table?')

	def with_input_file(self):

		if self.algorithm not in self.supported_algorithms:
			print('You must choose a supported self.algorithm: sha512, sha256, md5')
			return None

		m = 0
		n = 0
		self.results = {}
		self.salts = []

		start = time.time()
		
		for i in self.input_file:
			x = i.split(' ')
			to_hash = x[0]
			salt = x[1]
			print('Hashes to calculate: {}'.format(len(self.input_file) - m))
			m += 1
			l = to_hash.lower()
			for k in self.dictionary:
				n += 1
				j = bytes(k + salt, 'utf-8')
				hashed = getattr(hashlib, self.algorithm)(j).hexdigest()
				# if self.verbose:
				# 	print(hashed)
				if hashed == l:
					end = time.time()
					print('\nHash found, the password is: ', k)
					print('\nTime took to complete: ', (end-start))
					print('Words tried: ', n)
					self.results[hashed] = k
					self.salts.append(self.salt)

		if self.output_file:
			self.make_output_file()
			return True
		else:
			return True

	def make_output_file(self):

		n = 0

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
				for i, j in self.results.items():
					f.write('The Word for the hash {} with salt {} is: {}\n'.format(i, self.salts[n], j))
					n += 1
				print('\nEverything was written to file succesfully!')
				f.close()
			elif exists == 'n' or exists == 'N':
				print('Please change the output file name in settings')	
		else:
			for i, j in self.results.items():
				f.write('The Word for the hash {} with salt {} is: {}\n'.format(i, self.salts[n], j))
				n += 1