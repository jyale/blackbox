from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

class LRS:
	# takes a list of public keys, one private key, and the 
	# index of the private key's corresponding public key in 
	# the list of public keys
	# all public keys must have the same p, q, g values
	def __init__(self, publicKeys, privateKey, index):
		self.L = publicKeys
		self.xpi = privateKey.x
		self.pi = index
		# get group parameters
		self.p = self.L[0].p
		self.q = self.L[0].q
		self.g = self.L[0].g
		
	# define the hash functions
	def H1(self, message):
		# hash the message
		digest = SHA.new(message).hexdigest()
		# convert to integer
		x = int(digest, 16)
		# take it mod q
		return x % self.q
	def H2(self, message):
		# hash the message
		digest = SHA.new(message).hexdigest()
		# convert to integer
		x = int(digest, 16)
		# take it mod p
		return x % self.p

	# sign a message
	def sign(self,m):
		# compute h (hash the public keys)
		keystring = ''
		for i in range(len(self.L)):
			keystring += str(self.L[i])
		h = self.H2(keystring)
		# compute linkage tag
		tag = pow(h,self.xpi,self.p)
		# get a random u (in Zq)
		u = random.StrongRandom().randint(1,self.q-1)
		
		# compute first c value
		c2 = self.H1(str(self.L[0].y) + str(self.L[1].y) + str(tag) + m + str(pow(self.g,u,self.p)) + str(pow(h,u,self.p)))
		
		# step 3
		s2 = random.StrongRandom().randint(1,self.q-1)
		c1 = self.H1(str(self.L[0].y) + str(self.L[1].y) + str(tag) + m + str((pow(self.g,s2,self.p) * pow(self.L[1].y,c2,self.p))%self.p) + str((pow(h,s2,self.p) * pow(tag,c2,self.p))%self.p))

		# step 4
		s1 = (u - (x1 * c1)) % self.q
		sig = [c1,s1,s2,tag]
		return sig
	
	def verify(self,m,sig):
		# get parameters from signature
		c1 = sig[0]
		print c1
		s1 = sig[1]
		print s1
		s2 = sig[2]
		print s2
		tag = sig[3]
		print tag
		# compute h
		keystring = ''
		for i in range(len(self.L)):
			keystring += str(self.L[i])
		h = self.H2(keystring)
	
		z1p = (pow(self.g,s1,self.p) * pow(y1,c1,self.p)) % self.p
		z1pp = (pow(h,s1,self.p) * pow(tag,c1,self.p)) % self.p

		c2 = self.H1(str(y1)+str(y2) + str(tag) + m + str(z1p) + str(z1pp))

		z2p = (pow(self.g,s2,self.p) * pow(y2,c2,self.p)) % self.p
		z2pp = (pow(h,s2,self.p) * pow(tag,c2,self.p)) % self.p

		print
		print c1
		print 
		result = self.H1(str(y1)+str(y2)+str(tag)+m+ str(z2p) + str(z2pp))
		print result
		print
		print (c1 == result)

# generate group parameters
key = DSA.generate(1024)
a = key.p
b = key.q
c = key.g

# generate private keys
x1 = random.StrongRandom().randint(1,b-1)
x2 = random.StrongRandom().randint(1,b-1)

# get public keys
y1 = pow(c,x1,a)
y2 = pow(c,x2,a)

tuple1 = (y1,c,a,b,x1)
tuple2 = (y2,c,a,b,x2)

# get the 2 DSA keys

key1 = DSA.construct(tuple1)
key2 = DSA.construct(tuple2)

lrs = LRS([key1,key2],key1,0)
mess = 'weak'
sig = lrs.sign(mess)
		
print lrs.verify(mess,sig)	

print
print a
print
print b
print
print c
		
		
		
		
		
		
		

