from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

################################
# LINKABLE RING SIGNATURE CODE
################################

key = DSA.generate(1024)
p = key.p
q = key.q
g = key.g

# generate private keys
x1 = random.StrongRandom().randint(1,q-1)
x2 = random.StrongRandom().randint(1,q-1)

# get public keys
y1 = pow(g,x1,p)
y2 = pow(g,x2,p)

tuple1 = (y1,g,p,q,x1)
tuple2 = (y2,g,p,q,x2)

# get the 2 DSA keys
key1 = DSA.construct(tuple1)
key2 = DSA.construct(tuple2)

# define the hash functions
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
print



y1 = key1.y
y2 = key2.y
x1 = key1.x
x2 = key2.x

L = [y1,y2]
h = H2(str(y1) + str(y2))
h = g

######################################
# SIGNATURE GENERATION
######################################

m = 'hello'
tag = pow(h,x1,p)
# get a random u
u = random.StrongRandom().randint(1,q-1)
c2 = H1(str(y1) + str(y2) + str(tag) + m + str(pow(g,u,p)) + str(pow(h,u,p)))

# step 3
s2 = random.StrongRandom().randint(1,q-1)
c1 = H1(str(y1) + str(y2) + str(tag) + m + str((pow(g,s2,p) * pow(y2,c2,p))%p) + str((pow(h,s2,p) * pow(tag,c2,p))%p))

# step 4
s1 = (u - (x1 * c1)) % q

sig = [c1,[s1,s2],tag]
firstsig = sig
thirdsig = sig

##########################################
# x2 = x2 + 1

L = [y1,y2]
n = len(L)
m = 'weak'
x = x2
c = range(n)
# index of private key in list of public keys
# pi = 1
# get a string of all the public keys
keystring = ''
for i in range(n):
	keystring += str(L[i])
tag = pow(h,x,p)
keytagm = keystring + str(tag) + m

# get a random u
u = random.StrongRandom().randint(1,q-1)
c[0] = H1(keytagm + str(pow(g,u,p)) + str(pow(h,u,p)))

# step 3
s1 = random.StrongRandom().randint(1,q-1)
c[1] = H1(keytagm + str((pow(g,s1,p) * pow(L[0],c[0],p))%p) + str((pow(h,s1,p) * pow(tag,c[0],p))%p))

# step 4
s2 = (u - (x * c[1])) % q

sig = [c[0],[s1,s2],tag]
secondsig = sig

#########################################
# SIGNATURE VERIFICATION FUNCTION
#########################################

def verify(sig, L, m):
	# get variables from signature
	n = len(L)
	c = range(n + 1)
	c[0] = sig[0]
	s = sig[1]
	tag = sig[2]
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
	print c[0]
	print result
	print (c[0] == c[n])
	print
	
	
m = 'hello'
x = x1
tag = pow(h,x,p)
# get a random u
u = random.StrongRandom().randint(1,q-1)
c2 = H1(str(y1) + str(y2) + str(tag) + m + str(pow(g,u,p)) + str(pow(h,u,p)))

# step 3
s2 = random.StrongRandom().randint(1,q-1)
c1 = H1(str(y1) + str(y2) + str(tag) + m + str((pow(g,s2,p) * pow(y2,c2,p))%p) + str((pow(h,s2,p) * pow(tag,c2,p))%p))

# step 4
s1 = (u - (x * c1)) % q

sig = [c1,[s1,s2],tag]
thirdsig = sig

####################################
# TEST SIG GEN FUNCTION
####################################

m = 'hello'
x = x1
L = [y1,y2]
n = len(L)
c = range(n)
s = range(n)
keystring = str(y1) + str(y2) + str(tag) + m;
tag = pow(h,x,p)
# get a random u
u = random.StrongRandom().randint(1,q-1)
c[1] = H1(keystring + str(pow(g,u,p)) + str(pow(h,u,p)))

# step 3
s[1] = random.StrongRandom().randint(1,q-1)
c[0] = H1(keystring + str((pow(g,s[1],p) * pow(L[1],c[1],p))%p) + str((pow(h,s[1],p) * pow(tag,c[1],p))%p))

# step 4
s[0] = (u - (x * c[0])) % q

sig = [c[0],[s[0],s[1]],tag]
thirdsig = sig

####################################
# END SIG GEN FUNCTION
####################################
# m = 'hello'
# L = [y1,y2]
# x = x1
# pi = 0
def sign(m,L,x,pi):
	tag = pow(h,x,p)
	# get a random u
	keystring = str(L[0]) + str(L[1]) + str(tag) + m;
	u = random.StrongRandom().randint(1,q-1)
	c[(pi+1)%n] = H1(keystring + str(pow(g,u,p)) + str(pow(h,u,p)))

	i = (pi+1)%n
	# step 3
	s[i] = random.StrongRandom().randint(1,q-1)
	c[(i+1)%n] = H1(keystring + str((pow(g,s[i],p) * pow(L[i],c[i],p))%p) + str((pow(h,s[i],p) * pow(tag,c[i],p))%p))

	# step 4
	s[pi] = (u - (x * c[pi])) % q

	sig = [c[0],[s[0],s[1]],tag]
	thirdsig = sig
	return sig
	

m = 'hello'
	
print 'verify funtion.....'
print	
L = [y2,y1]
verify(firstsig,L,'hello')
verify(secondsig,L,'weak')
L = [y1,y2]
verify(firstsig,L,'hello')
verify(secondsig,L,'weak')
print 'third sig'
verify(thirdsig,L,m)
print
print 'weak'
verify(sign(m,L,x2,1),L,m)
