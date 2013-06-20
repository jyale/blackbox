from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

message = "Hello"
# make DSA keypair
key = DSA.generate(1024)

# hash the message
h = SHA.new(message).digest()
# random int (required for signing the message)
k = random.StrongRandom().randint(1,key.q-1)
# sign message HASH (h) using key and random int k in range 1 to (q-1)
sig = key.sign(h,k)

if key.verify(h,sig):
    print "OK"
else:
    print "Incorrect signature"

x = key.publickey()

if x.verify(h,sig):
    print "OK"
else:
    print "Incorrect signature"

print key.keydata
print x.keydata
print key.has_private()
print x.has_private()

y = key.__getattr__('y')
p = key.__getattr__('p')
q = key.__getattr__('q')
g = key.__getattr__('g')
x = key.__getattr__('x')

print key.x

# get 2 private keys
x1 = random.StrongRandom().randint(1,key.q-1)
x2 = random.StrongRandom().randint(1,key.q-1)

#composite key
x = (x1 + x2) % q
y = pow(g,x,p)

tuple = (y,g,p,q,x)

key = DSA.construct(tuple)

h = SHA.new('weak').digest()
k = random.StrongRandom().randint(1,key.q-1)
sig = key.sign(h,k)

if key.verify(h,sig):
    print "OK"
else:
    print "Incorrect signature"

print (x1 + x2 + x2)
print (x1 + x2 + x2) % q

x = (x1 + x2 + x2) % q
y = pow(g,x,p)

print 'computed y: ', y
print 'y1 * y2 * y2: ', (pow(g,x1,p) * pow(g,x2,p) * pow(g,x2,p)) % p


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
def H1(m):
	# hash the message
	digest = SHA.new(message).hexdigest()
	# convert to integer
	x = int(digest, 16)
	# take it mod q
	return x % q
def H2(m):
	# hash the message
	digest = SHA.new(message).hexdigest()
	# convert to integer
	x = int(digest, 16)
	# take it mod p
	return x % p

print

m = 'hello'

y1 = key1.y
y2 = key2.y
x1 = key1.x
x2 = key2.x

L = [y1,y2]
h = H2(str(y1) + str(y2))

tag = pow(h,x1,p)
# get a random u
u = random.StrongRandom().randint(1,q-1)
c2 = H1(str(y1) + str(y2) + str(tag) + m + str(pow(g,u,p)) + str(pow(h,u,p)))

# step 3
s2 = random.StrongRandom().randint(1,q-1)
c1 = H1(str(y1) + str(y2) + str(tag) + m + str((pow(g,s2,p) * pow(y2,c2,p))%p) + str((pow(h,s2,p) * pow(tag,c2,p))%p))

# step 4
s1 = (u - (x1 * c1)) % q

sig = [c1,s1,s2,tag]

#########################################
# SIGNATURE VERIFICATION
#########################################

z1p = (pow(g,s1,p) * pow(y,c1,p)) % p
z1pp = (pow(h,s1,p) * pow(tag,c1,p)) % p

c2 = H1(str(y1)+str(y2) + str(tag) + m + str(z1p) + str(z1pp))

z2p = (pow(g,s2,p) * pow(y,c2,p)) % p
z2pp = (pow(h,s2,p) * pow(tag,c2,p)) % p

print
print c1
print 
result = H1(str(y1)+str(y2)+str(tag)+m+ str(z2p) + str(z2pp))

print (c1 == result)
