#  collect the distributed key parts and combine them into composite key

import sys,os,hashlib,random,Crypto.PublicKey.RSA, urllib2, pickle
from lrs import sign, verify
from Crypto.Random import random
# facebook id / email / cellphone number etc
id = 'weakcode'

# list of other ids for anonymity set
anonset = ['you','are','weak']
setsize = len(anonset)

# number of servers
n = 3
privs = range(n)
pubs = range(n)

# group parameters
p = 89884656743115795664792711940796176851119970086295094525916939279014416884510410227155912705490141517040349493104350713250894752209598792377036705329921777150659847842412101813159134527960689713473746097408990841229149478637132788373696814456297458600531763096786958922891028326530110554624621072800084070961
q = 941506596250216984203090146520333547538244481697
g = 34602665038470649139675399213351821394778342143927940407384555720280713734040263824622508144389505207857155089278564186198863137963701380287457519992520537429937507501716393531967183791615285710169926131958833245212562988126415401503359363244583486448835867790065950788495491077021769975019105890787102335681

# get the private and public keys
for i in range(n):
	# private keys
	response = urllib2.urlopen('http://mahan.webfactional.com/dsa/keygen/server' + str(i) + '/getpriv.php?id=' + id)
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

	
# get LRS signature
# add private key to list of pub keys
pos = random.StrongRandom().randint(0,len(pubkeys))
L = pubkeys[:pos]+[comppub]+pubkeys[pos:]
# message to sign

f = open('ogst.pdf','rb')
msg1 = f.read()
m = msg1
print verify(sign(m,L,comppriv,pos),m)
print










