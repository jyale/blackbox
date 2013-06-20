import os,hashlib,random,Crypto.PublicKey.RSA
 
class ring:
# initial ring signature setup
    def __init__(self,k,l=1024):
        self.k = k
        self.l,self.n,self.q = l,len(k),1<<l-1
# method to sign a message
    def sign(self,m,z):
        self.permut(m)
        s,u = [None]*self.n,random.randint(0,self.q)
        c = v = self.E(u) 
	
	# for all other members (ie not the one using their private key)
        for i in range(z+1,self.n)+range(z):
            s[i] = random.randint(0,self.q)
            v = self.E(v^self.g(s[i],self.k[i].e,self.k[i].n)) 
            if (i+1)%self.n == 0: c = v

	# use the private key of member z
        s[z] = self.g(v^u,self.k[z].d,self.k[z].n)
        return [c,] + s

# method to verify a signature (X is a list of public keys, m is signature)
    def verify(self,m,X):
        self.permut(m)
        y = map(lambda i:self.g(X[i+1],self.k[i].e,self.k[i].n),range(len(X)-1))
        return reduce(lambda x,i:self.E(x^y[i]),range(self.n),X[0]) == X[0]
 
# helper functions as defined in ring sig paper
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

# number of participants in ring signature
size = 4
# two messages to sign
msg1,msg2 = 'hello','world!'

# ring signature object
r = ring(map(lambda _:Crypto.PublicKey.RSA.generate(1024, os.urandom),range(size)))
# test every combination of signing and verifying
for i in range(size):
    s1,s2 = r.sign(msg1,i),r.sign(msg2,i)
    print (r.verify(msg1,s1) and r.verify(msg2,s2) and not r.verify(msg1,s2))
