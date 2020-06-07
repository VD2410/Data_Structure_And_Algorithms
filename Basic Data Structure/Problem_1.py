from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        self.cache = OrderedDict()
        if capacity <=0:
        	print("ERROR:- Capacity should be positive")
        	exit(0)

        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:

        	value = self.cache[key]
        	self.cache.move_to_end(key)

        	return value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity < (len(self.cache) + 1):

        	self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(value)

        

our_cache = LRU_Cache(5)
# print(our_cache)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print("-----------------------------Test 1-------------------------------------")

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)


print("-----------------------------Test 2-------------------------------------")

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print("-----------------------------Test 3-------------------------------------")

print(our_cache.get()) 