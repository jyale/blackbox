from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

# group parameters
p = 89884656743115795664792711940796176851119970086295094525916939279014416884510410227155912705490141517040349493104350713250894752209598792377036705329921777150659847842412101813159134527960689713473746097408990841229149478637132788373696814456297458600531763096786958922891028326530110554624621072800084070961
q = 941506596250216984203090146520333547538244481697
g = 34602665038470649139675399213351821394778342143927940407384555720280713734040263824622508144389505207857155089278564186198863137963701380287457519992520537429937507501716393531967183791615285710169926131958833245212562988126415401503359363244583486448835867790065950788495491077021769975019105890787102335681


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

def verify(sig, m, L):
	# print 'verifying...'	
	# get variables from signature
	# L = sig[3]
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
'''	
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
'''









