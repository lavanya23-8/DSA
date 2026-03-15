class Fancy(object):

    def __init__(self):
        self.mod = 10**9+7
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val):
        inv = pow(self.mul, self.mod-2, self.mod)
        val = (val-self.add) % self.mod
        val = (val * inv) % self.mod
        self.seq.append(val)        

    def addAll(self, inc):
        self.add = (self.add + inc) % self.mod
        
    def multAll(self, m):
        self.mul = (self.mul * m) % self.mod
        self.add = (self.add * m) % self.mod
        

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod