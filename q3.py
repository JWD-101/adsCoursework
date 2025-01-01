class HashTable():
    """Implements a simple hash table of size k, with all 
    empty entries denoted as '-' at initialisation.

    You must not modify this code.

    Set up your hashtable as follows, with some sensible integer value for k:
        h = HashTable(k)
    
    For a HashTable h:
        h.lookup(pos) returns the data in position pos.
        h.add(pos, data) adds data in position pos. 
        h.check(table) checks that the current entries are equal to 
            table, which is represented as a list. This is only used for 
            testing that the hash table contains what we expect.
        h.print_table prints h.
    """
    def __init__(self, k):
        self.__table = ["-"] * k  
    def lookup(self, pos):
        return self.__table[pos]
    def add(self, pos, data):
        self.__table[pos] = data
    def check(self, table_of_data):
        return self.__table == table_of_data
    def print_table(self):
        print(self.__table)

def hash_quadratic(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Use quadratic probing (see question for details) to resolve 
    collisions.
    """
    h = HashTable(17)
    for key in d:
        hash = (3*key+5)%17
        collisionResolved = False
        j=0
        while collisionResolved==False:
            if h.lookup((hash+j*j)%17)=="-":
                h.add((hash+j*j)%17,key)
                collisionResolved=True
            else:
                j+=1
    return h

def hash_double(d):
    """Inserts keys from the list d into a hash table and
    returns the HashTable which contains the state of the 
    hash table after these insertions.

    Use just one HashTable instance inside this function.
    
    Use double hashing (see question for details) to resolve
    collisions.
    """
    h = HashTable(17)
    for key in d:
        hash = (3*key+5)%17
        secondHash = 13-(key%13)

        collisionResolved = False
        j=0
        while collisionResolved==False:
            if h.lookup((hash+j*secondHash)%17)=="-":
                h.add((hash+j*secondHash)%17,key)
                collisionResolved=True
            else:
                j+=1
    return h

# simple tests
assert(hash_quadratic([1, 2, 3, 4]).check([4, '-', '-', '-', '-', '-', '-', '-', 1, '-', '-', 2, '-', '-', 3, '-', '-']))
assert(hash_quadratic([5]).check(['-', '-', '-', 5, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert(hash_quadratic([22]).check(['-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert(hash_quadratic([5, 22, 39]).check(['-', '-', '-', 5, 22, '-', '-', 39, '-', '-', '-', '-', '-', '-', '-', '-', '-']))

assert(hash_double([1, 2, 3, 4]).check([4, '-', '-', '-', '-', '-', '-', '-', 1, '-', '-', 2, '-', '-', 3, '-', '-']))
assert(hash_double([5]).check(['-', '-', '-', 5, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert(hash_double([22]).check(['-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']))
assert(hash_double([5, 22, 39]).check(['-', '-', '-', 5, '-', '-', '-', 22, '-', '-', '-', '-', '-', '-', '-', '-', 39]))

