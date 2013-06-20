import os,hashlib,random,Crypto.PublicKey.RSA
from ring import ring

print('weak')

# number of participants in ring signature
size = 4
# two messages to sign
msg1,msg2 = 'hello','world!'

# ring signature object
r = ring(map(lambda _:Crypto.PublicKey.RSA.generate(1024, os.urandom),range(size)))
# test every combination of signing and verifying
for i in range(size):
    s1,s2 = r.sign(msg1,i),r.sign(msg2,i)
    x = (r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2))
    print(x)

print()

# signing test
# make 2 RSA keys
key1 = Crypto.PublicKey.RSA.generate(1024, os.urandom)
key2 = Crypto.PublicKey.RSA.generate(1024, os.urandom)
# make a ring signature
r = ring([key1, key2])

# write private key to file
x = key1.exportKey()
print (x)
