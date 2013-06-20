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
