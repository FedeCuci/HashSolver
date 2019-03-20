# Hash-Solver

Hash solver is a little python program that uses a dictionary file to compute a hash provided by the user. It loops over the dictionary file, and hashes every single word that is in it, until it finds the one that matches with the one that the user provided. It has several additional functionalities such as adding salts, calculating multiple hashes by providing an input file, verbose...


Hash solver is a simple script written in Python 3 which should facilitate the calculation of hashes. This hash solver
gives the user several functionalities and flexibility, however remains very simple. 

This hash solver works by receiving a given hash and looping over all the hashes of all the words within a given dictionary file. 

There are several other solutions but hash-solver is a good option for the command line. The functionalities that this hash solver includes are:
	1. Algorithms: md5, sha256, sha512
	2. Input/hash file: A custom input file containing all the hashes the user wants to compute
	3. Verbose
	4. Dictionary: A default and/or custom dictionary file in which to check the given hash from
	5. Output file: An option to return all the results in a separate text file
	6. Salt: An option to append a salt to the provided hashes

<h1> How to use Hash Solver </h1>

You can run the file with Python 3 by running:
	python3 main.py

<h3> Useful commands: </h3>
	- settings: change the settings of the program (listed above)
	- status: check the current status of your settings
	- crack: crack the hash/es with the current settings
	- c: quit the program


