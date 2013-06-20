# command line decrypter

from encrypt import decrypt_file
import sys

if len(sys.argv) == 3:
	decrypt_file(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
	decrypt_file(sys.argv[1], sys.argv[2], sys.argv[3])
else:
	print 'Usage: python decrypter.py [key] [input file] [output file]'

