import sys,os,hashlib,random,Crypto.PublicKey.RSA
import urllib2
from subprocess import call
from ring import ring

# get the facebook ids we'll use to get PUBLIC keys
pubs = range(len(sys.argv))

print 'getting public keys.....'

# get the public keys
for x in range(1,len(sys.argv)):
	id = sys.argv[x]

	# make sure the keys have been generated
	response = urllib2.urlopen('http://mahan.webfactional.com/pubkeygen.php?id=' + id)

	# get the public key
	response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/' + id)
	html = response.read()
	pub = Crypto.PublicKey.RSA.importKey(html)

	# get the private key
	response = urllib2.urlopen('http://mahan.webfactional.com/priv-keys/' + id)
	html = response.read()
	priv = Crypto.PublicKey.RSA.importKey(html)
	
	# save the public key in a list
	pubs[x] = pub
	# set first to private key

#	print priv.exportKey()
	print
#	print pub.exportKey()

print pubs

print 'getting private key...'

# make sure the private key have been generated
response = urllib2.urlopen('http://mahan.webfactional.com/pubkeygen.php?id=privtest')
# get the private key
response = urllib2.urlopen('http://mahan.webfactional.com/priv-keys/privtest')
html = response.read()
privtest = Crypto.PublicKey.RSA.importKey(html)
pubs[0] = privtest

# signer's public key
response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/privtest')
html = response.read()
pubtest = Crypto.PublicKey.RSA.importKey(html)

size=4
# two messages to sign
msg1,msg2 = 'hello','world!'

# ring signature object
r = ring(pubs)

# sign the messages
s1,s2 = r.sign(msg1,0),r.sign(msg2,0)

# now verify just using public keys
pubs[0] = pubtest
s = ring(pubs)
print (s.verify(msg1,s1) and s.verify(msg2,s2) and not s.verify(msg1,s2))
