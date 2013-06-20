import sys,os,hashlib,random,Crypto.PublicKey.RSA, pickle
import urllib2
from subprocess import call
# my ring signature implementation
from ring import ring
# used to shuffle a list
from random import shuffle

if len(sys.argv)-1 < 2:
	sys.exit("Usage: python2.7 signer.py [signerID] [other IDs] [file]")

# which user is the signer
z = 0

# file to sign
filename = sys.argv[len(sys.argv)-1]

size = len(sys.argv)-2
# get the facebook ids we'll use to get PUBLIC keys
pubs = range(size)
# store all the facebook ids
ids = range(size)
print pubs
print 'getting public keys.....'

# get the public keys
for x in range(1,size + 1):
	id = sys.argv[x]
	# remove any remaining facebook url
	id = id.replace("https://www.facebook.com/", "")	
	id = id.replace("http://www.facebook.com/", "")

	# make sure the keys have been generated
	response = urllib2.urlopen('http://mahan.webfactional.com/pubkeygen.php?id=' + id)

	# get the public key
	response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/' + id)
	html = response.read()
	pub = Crypto.PublicKey.RSA.importKey(html)
	
	# save the public key in a list
	pubs[x-1] = pub
	# save the facebook id in a list
	ids[x-1] = id

#	print priv.exportKey()
	print
#	print pub.exportKey()

print pubs

id = sys.argv[z+1]
id = id.replace("https://www.facebook.com/", "")	
id = id.replace("http://www.facebook.com/", "")

# make sure private key has been generated
response = urllib2.urlopen('http://mahan.webfactional.com/pubkeygen.php?id=' + id)

# get the private key
response = urllib2.urlopen('http://mahan.webfactional.com/priv-keys/' + id)
html = response.read()
priv = Crypto.PublicKey.RSA.importKey(html)
pubs[z] = priv

# now shuffle keys into random order along with ids
# do this by shuffling the indices
list1_shuf = []
list2_shuf = []
index_shuf = range(len(pubs))
shuffle(index_shuf)
for i in index_shuf:
    list1_shuf.append(pubs[i])
    list2_shuf.append(ids[i])

#shuffle(pubs)

pubs = list1_shuf
ids = list2_shuf

print pubs
print ids

# find the private key to use to sign
for i in range(len(pubs)):
	if(pubs[i].has_private()) :
		z = i

# write message to file
# msg = 'hello'
# f = open('message','w')
#pickle.dump(msg,f)

# two messages to sign
# f = open('message','r')
# msg1 = pickle.load(f)

##############################

# msg = 'hello'
# f = open('message','wb')
# f.write(msg)

#### READ THE FILE TO SIGN ###
f = open(filename,'rb')
msg1 = f.read()


#################################

# ring signature object
r = ring(pubs)

# sign the messages
s1 = r.sign(msg1,z)

# save the signature to file
f = open('sigs/' + filename[7:] + '-sig','w')

# now verify just using public keys
id = sys.argv[1]
id = id.replace("https://www.facebook.com/", "")	
id = id.replace("http://www.facebook.com/", "")

response = urllib2.urlopen('http://mahan.webfactional.com/pub-keys/' + id)

html = response.read()
pub = Crypto.PublicKey.RSA.importKey(html)

pubs[z] = pub

# save the list of facebook ids, their corresponding public keys, and the signature
pickle.dump([ids,pubs,s1],f)

s = ring(pubs)
print s.verify(msg1,s1)

print ids
