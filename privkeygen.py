import sys, os.path, Crypto.PublicKey.RSA, os, hashlib
# to make unix shell calls
from subprocess import call

# get the filename from cmd line arg
filename = sys.argv[1]
pubfile = 'pub-keys/' + filename
privfile = 'priv-keys/' + filename

if os.path.exists(privfile):
	call(["cat", privfile])
else:
	# generate a public key for that user
	x = Crypto.PublicKey.RSA.generate(1024, os.urandom)
	f = open(pubfile, 'wb')
	f.write(x.publickey().exportKey())
	f = open(privfile, 'wb')
	f.write(x.exportKey())
	call(["cat", privfile])

