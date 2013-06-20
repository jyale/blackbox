#
# This is used to verify ring signatures
# Pass the signature and the file as command line parameters


import sys,os,hashlib,random,Crypto.PublicKey.RSA, urllib2, pickle
from subprocess import call
from ring import ring

# check command line args are provided
if len(sys.argv)-1 < 2:
	sys.exit("Usage: python2.7 signer.py [signature] [file]")

# get the facebook ids we'll use to get PUBLIC keys

size = len(sys.argv)-2
pubs = range(size)
# name of file to verify signature against
filename = sys.argv[len(sys.argv)-1]
print 'filename: ', filename

print 'reading signature...'
# read the signature from file
sigfilename = sys.argv[1]
f = open(sigfilename,'r')
ids, pubs, sig = pickle.load(f)

###################################

f = open(filename,'rb')
msg3 = f.read()


############################



# now verify just using public keys

s = ring(pubs)
print (s.verify(msg3,sig))
if s.verify(msg3,sig):
	print "file was signed by one of the following: ", ids

