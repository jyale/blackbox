# required for crypto
import os,hashlib,random,Crypto.PublicKey.RSA
# to get command line arguments
import sys

# ring signature implementation 
class ring:
    def __init__(self,k,l=1024):
        self.k = k
        self.l,self.n,self.q = l,len(k),1<<l-1
 
    def sign(self,m,z):
        self.permut(m)
        s,u = [None]*self.n,random.randint(0,self.q)
        c = v = self.E(u) 
        for i in range(z+1,self.n)+range(z):
            s[i] = random.randint(0,self.q)
            v = self.E(v^self.g(s[i],self.k[i].e,self.k[i].n)) 
            if (i+1)%self.n == 0: c = v
        s[z] = self.g(v^u,self.k[z].d,self.k[z].n)
        return [c,] + s
 
    def verify(self,m,X):
        self.permut(m)
        y = map(lambda i:self.g(X[i+1],self.k[i].e,self.k[i].n),range(len(X)-1))
        return reduce(lambda x,i:self.E(x^y[i]),range(self.n),X[0]) == X[0]
 
    def permut(self,m):
        self.p = int(hashlib.sha1('%s'%m).hexdigest(),16)
 
    def E(self,x): 
        return int(hashlib.sha1('%s%s'%(x,self.p)).hexdigest(),16)
 
    def g(self,x,e,n):
        q,r = x//n,x%n
        if (q+1)*n <= (1<<self.l)-1:
            return q*n + pow(r,e,n)
        else:
            return x

x = Crypto.PublicKey.RSA.generate(1024, os.urandom)
print x.publickey().exportKey()

# ring signature tests
size,msg1,msg2 = 4,'hello','world!'
r = ring(map(lambda _:Crypto.PublicKey.RSA.generate(1024, os.urandom),range(size)))
for i in range(size):
    s1,s2 = r.sign(msg1,i),r.sign(msg2,i)
    print r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2)

# creating public and private RSA keys
x = Crypto.PublicKey.RSA.generate(1024, os.urandom)
a = x.exportKey()
y = x.publickey().exportKey()
print
print "generated public key: ", y
print

# import the publick eky
z = Crypto.PublicKey.RSA.importKey(y)
print "imported public key: ", z.exportKey()
# import the private key
b = Crypto.PublicKey.RSA.importKey(a)

r = ring([b,z])
s1,s2 = r.sign(msg1,0),r.sign(msg2,0)
print r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2)

# write the keys to file
f = open('privKey', 'wb')
f.write(a)
f = open('pubKey', 'wb')
f.write(y)

# read the keys from file
f = open('privKey', 'rb')
priv = f.read()
g = open('pubKey', 'rb')
pub = g.read()

# make the key objects
priv = Crypto.PublicKey.RSA.importKey(priv)
print "imported private key: ", priv.exportKey()
# import the private key
pub = Crypto.PublicKey.RSA.importKey(pub)
print "imported public key: ", pub.exportKey()

# make ring signature
print 'ring sig from file keys'
r = ring([priv, pub])
s1,s2 = r.sign(msg1,0),r.sign(msg2,0)
print r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2)

print 'verifying using only the public keys in the ring'
r = ring([priv.publickey(), pub])
print r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2)
print priv.publickey().exportKey()

# id = str(sys.argv[1])
# f = open('id', 'w')
# f.write('this is weak to the core')
