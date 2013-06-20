import os,hashlib,random,Crypto.PublicKey.RSA
from random import getrandbits

#####
# group setup
#####

# generator 
g = 2
# prime number (prime order q of group)
q = 7919
# prime p = qr + 1 (Schnorr group)
p = q * 8 + 1
print "p: ", p

# number of bits to use for DH private key
bits = 32

# the private key
a = getrandbits(bits)
b = getrandbits(bits)

# generate the public key
A = pow(g, a, q) 
B = pow(g, b, q)

# compute diffie hellman shared secret 
s1 = pow(A, b, q)
s2 = pow(B, a, q)

# test that shared secrets match
if(s1 == s2):
    print "Shared secrets match:  ", s1, s2


# public keys are A and B
# private keys are a and b
xpi = a;
# list of public keys
L = [A,B]

# STEP 1
# hash the public keys
pubhash = hashlib.sha1(str(L))
digest = pubhash.hexdigest()
h = int(digest, 16) % q

print h

ytilde = pow(h,xpi,q)
print ytilde

# STEP 2
# get random u
u = getrandbits(bits) % q
print u

# message
m = 'weak'

hash = hashlib.sha1(str(L) + str(ytilde) + m + str(pow(g,u,q)) + str(pow(h,u,q)))
digest = hash.hexdigest()
c2 = int(digest, 16) % q
print c2

# pick s2
s2 = getrandbits(bits) % q

xtmp = (pow(g,s2,q) * pow(B,c2,q)) % q
ytmp = (pow(h,s2,q) * pow(ytilde,c2,q)) % q

hash = hashlib.sha1(str(L) + str(ytilde) + m + str(xtmp) + str(ytmp))
digest = hash.hexdigest()
c1 = int(digest, 16) % q
print c1

####
# STEP 4
####
s1 = (u - (xpi * c1)) % q

sig = [c1,s1,s2,ytilde]
print sig

####################
## SIGNATURE VERIFICATION
####################

pubhash = hashlib.sha1(str(L))
digest = pubhash.hexdigest()
h = int(digest, 16) % q

z1prime = (pow(g,s1,q) * pow(A,c1,q)) % q
z1primeprime = (pow(h,s1,q) * pow(ytilde,c1,q)) % q

hash = hashlib.sha1(str(L) + str(ytilde) + m + str(z1prime) + str(z1primeprime))
digest = hash.hexdigest()
c2 = int(digest, 16) % q

z2prime = (pow(g,s2) * pow(B, c2)) % q
z2primeprime = (pow(h,s2,q) * pow(ytilde,c2,q)) % q

hash = hashlib.sha1(str(L) + str(ytilde) + m + str(z2prime) + str(z2primeprime))
digest = hash.hexdigest()
result = int(digest, 16) % q
print
print
print c1
print
print result
