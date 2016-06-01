# Veeeery simple hash table class
# Implemented easy linear chaining
class HashTable(object):
    def __init__(self, size):
        self.list = []
        for x in xrange(size):
            self.list.append([])
        self.size = size

    def insert(self, val):
        self.list[ val % self.size ].append(val)
        
    def inside(self, val):
        if val in self.list[ val % self.size ]:
            return True
        else:
            return False



hashBrowns = HashTable(100)

for x in xrange(10):
    hashBrowns.insert(x)

for x in xrange(10):
    if hashBrowns.inside(x) == True:
        print x, " is in our breakfast!"
    else:
        print "We don't have any ", x, "!"

for x in xrange(100, 110):
    if hashBrowns.inside(x) == True:
        print x, " is in our breakfast!"
    else:
        print hashBrowns.list[x % 100]
    
