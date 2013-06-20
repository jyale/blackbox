class LRSPublicKey:
	# takes a list of public keys, one private key, and the 
	# index of the private key's corresponding public key in 
	# the list of public keys
	# all public keys must have the same p, q, g values
	def __init__(self, publicKeys, privateKey, index, p, q, g):
		self.L = publicKeys
		self.xpi = privateKey
		self.pi = index
		# get group parameters
		self.p = p
		self.q = q
		self.g = g
		
	# define the hash functions
	def H1(m):
		# hash the message
		digest = SHA.new(message).hexdigest()
		# convert to integer
		x = int(digest, 16)
		# take it mod q
		return x % self.q
	def H2(m):
		# hash the message
		digest = SHA.new(message).hexdigest()
		# convert to integer
		x = int(digest, 16)
		# take it mod p
		return x % self.p

test = LRSPublicKey([1,2,3],2,2,4,5,6)
print test.p
