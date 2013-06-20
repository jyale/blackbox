from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

# set group parameters
key = DSA.generate(1024)
p = key.p
q = key.q
g = key.g

# hash functions
def H1(message):
	# hash the message
	digest = SHA.new(message).hexdigest()
	# convert to integer
	x = int(digest, 16)
	# take it mod q
	return x % q
def H2(message):
	# hash the message
	digest = SHA.new(message).hexdigest()
	# convert to integer
	x = int(digest, 16)
	# take it mod p
	return x % p

def verify(sig, L, m):
	# print 'verifying...'	
	# get variables from signature
	n = len(L)
	c = range(n + 1)
	c[0] = sig[0]
	s = sig[1]
	tag = sig[2]
	h=g
	# lists to store calculation results in (z' and z'' in LRS paper)
	zp = range(n)
	zpp = range(n)	
	# get a string of all the public keys
	keystring = ''
	for i in range(n):
		keystring += str(L[i])
	for i in range(n):
		zp[i] = (pow(g,s[i],p) * pow(L[i],c[i],p)) % p
		zpp[i] = (pow(h,s[i],p) * pow(tag,c[i],p)) % p
		c[i+1] = H1(keystring + str(tag) + m + str(zp[i]) + str(zpp[i]))
	result = c[n]
	return (c[0] == c[n])

def sign(m,L,x,pi):
	# print 'signing...'
	h = g
	tag = pow(h,x,p)
	n = len(L)
	c = range(n)
	s = range(n)
	# get a random u
	keystring = ''
	for i in range(n):
		keystring += str(L[i])
	keystring += str(tag) + m;
	u = random.StrongRandom().randint(1,q-1)
	c[(pi+1)%n] = H1(keystring + str(pow(g,u,p)) + str(pow(h,u,p)))
	# step 3
	i = (pi+1)%n
	for i in range(pi+1,n)+range(pi):
		# print range(6,5)
		s[i] = random.StrongRandom().randint(1,q-1)
		c[(i+1)%n] = H1(keystring + str((pow(g,s[i],p) * pow(L[i],c[i],p))%p) + str((pow(h,s[i],p) * pow(tag,c[i],p))%p))
	# step 4
	s[pi] = (u - (x * c[pi])) % q
	# the signature
	sig = [c[0],s,tag]
	return sig
	
# generate private and public keys
X = range(10)
L = range(10)
for i in range(len(X)):
	X[i] = random.StrongRandom().randint(1,q-1)
	L[i] = pow(g,X[i],p)

# test signing and verifying message with different private keys
m = 'hello'	
for i in range(len(X)):
	for j in range(len(X)):
		print str(i) + ',' + str(j) + ' ' + str((i == j) == verify(sign(m,L,X[i],j),L,m))

# print verify(sign(m,L,X[50],50),L,m)









