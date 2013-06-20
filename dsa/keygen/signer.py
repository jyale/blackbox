#  collect the distributed key parts and combine them into composite key

import sys,os,hashlib,random,Crypto.PublicKey.RSA, urllib2, pickle, facebook
from lrs import sign, verify
from Crypto.Random import random
# used to shuffle a list
from random import shuffle

if len(sys.argv)-1 < 2:
	sys.exit("Usage: python2.7 signer.py [signerID] [other IDs] [file]")

# facebook id / email / cellphone number etc
token = sys.argv[1]
print id

# get facebook id from access token
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
id = str(profile['username'])

print

# list of other ids for anonymity set
anonset = sys.argv[2:len(sys.argv)-1]
print anonset

#['you','are','weak']
# file to sign
filename = sys.argv[len(sys.argv)-1]
print filename

setsize = len(anonset)

####### number of servers #######
n = 3
#################################

privs = range(n)
pubs = range(n)

# group parameters
p = 89884656743115795664792711940796176851119970086295094525916939279014416884510410227155912705490141517040349493104350713250894752209598792377036705329921777150659847842412101813159134527960689713473746097408990841229149478637132788373696814456297458600531763096786958922891028326530110554624621072800084070961
q = 941506596250216984203090146520333547538244481697
g = 34602665038470649139675399213351821394778342143927940407384555720280713734040263824622508144389505207857155089278564186198863137963701380287457519992520537429937507501716393531967183791615285710169926131958833245212562988126415401503359363244583486448835867790065950788495491077021769975019105890787102335681

# get the private keys
for i in range(n):
	# private keys
	response = urllib2.urlopen('http://mahan.webfactional.com/dsa/keygen/server' + str(i) + '/fbgetpriv.php?id=' + token)
	html = response.read()
	privs[i] = int(html)
	# public keys
	response = urllib2.urlopen('http://mahan.webfactional.com/dsa/keygen/server' + str(i) + '/getpub.php?id=' + id)
	html = response.read()
	pubs[i] = int(html)
	print pow(g,privs[i],p) == pubs[i]

# combine private keys
comppriv = 0
comppub = 1
for i in range(n):
	comppriv += privs[i]
	comppub *= pubs[i]
comppriv %= q
comppub %= p

print pow(g,comppriv,p) == comppub

# function to get public key parts and combine to composite key
def getpub(id):
	pubparts = range(n)
	# collect the key parts
	for i in range(n):
		# public keys
		response = urllib2.urlopen('http://mahan.webfactional.com/dsa/keygen/server' + str(i) + '/getpub.php?id=' + id)
		html = response.read()
		pubparts[i] = int(html)
	# combine them to get composite public key
	temppub = 1
	for i in range(n):
		temppub *= pubparts[i]
	temppub %= p
	return temppub

# get the public keys for all ids in anon set
pubkeys = range(setsize)
for i in range(setsize):
	key = getpub(anonset[i])
	pubkeys[i] = key
	print key

pos=0
pubs = [comppub]+pubkeys

ids = [id]+anonset	

# now shuffle keys into random order along with ids
# do this by shuffling the indices
list1_shuf = []
list2_shuf = []
index_shuf = range(len(pubs))
shuffle(index_shuf)
print index_shuf
for i in index_shuf:
    list1_shuf.append(pubs[i])
    list2_shuf.append(ids[i])
pubs = list1_shuf
ids = list2_shuf

# find the private key to use to sign
for i in range(len(pubs)):
	if(pubs[i] == comppub) :
		z = i

print ids
# print pubs
print comppub
print pubs[z]
print z

"""
# get LRS signature
# add private key to list of pub keys
pos = random.StrongRandom().randint(0,len(pubkeys))
L = pubkeys[:pos]+[comppub]+pubkeys[pos:]
anonset = anonset[:pos]+[id]+anonset[pos:]
print anonset
"""
# message to sign

f = open(filename,'rb')
m = f.read()
# get the signature
s1 = sign(m,pubs,comppriv,z)
print verify(s1,m,pubs)
print

# save the signature to file
f = open('sigs/' + filename[7:] + '.sig','w')
# save the list of facebook ids, their corresponding public keys, and the signature
pickle.dump([ids,pubs,s1],f)









