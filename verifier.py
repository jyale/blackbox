#
# This is used to verify ring signatures
#

import sys,os,hashlib,random,Crypto.PublicKey.RSA, urllib2, pickle
from subprocess import call
from ring import ring

# check command line args are provided
# if len(sys.argv)-1 < 2:
#        sys.exit("Usage: python2.7 signer.py [signerID] [other IDs] [file]")

# get the facebook ids we'll use to get PUBLIC keys

size = len(sys.argv)-2
pubs = range(size)
# name of file to verify signature against
filename = sys.argv[len(sys.argv)-1]
print 'filename: ', filename

print 'getting public keys.....'

# get the public keys
if (size > 0):
	for x in range(2, size+1):
		id = sys.argv[x]

		# make sure the keys have been generated
		response = urllib2.urlopen('http://mahan.webfactional.com/pubkeygen.php?id=' + id)

		# get the public key
		response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/' + id)
		html = response.read()
		pub = Crypto.PublicKey.RSA.importKey(html)
	
		# save the public key in a list
		pubs[x-1] = pub
		print
if (size > 0):
	response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/' + sys.argv[1])
	html = response.read()
	pub = Crypto.PublicKey.RSA.importKey(html)
	pubs[0] = pub

print pubs
print

print 'reading signature...'
# read the signature from file
sigfilename = 'sigs/' + filename + '-sig'
f = open(sigfilename,'r')
ids, pubs2, sig = pickle.load(f)

# check if we should load public keys from file
if len(sys.argv)-1 < 2:
	pubs = pubs2
	print pubs

# read message from file
#f = open('message','r')
#msg3 = pickle.load(f)

###################################

f = open('uploads/' + filename,'rb')
msg3 = f.read()


############################



# now verify just using public keys

s = ring(pubs)
print (s.verify(msg3,sig))
if s.verify(msg3,sig):
	print "file was signed by one of the following: ", ids

