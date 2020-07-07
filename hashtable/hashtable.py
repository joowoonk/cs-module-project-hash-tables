class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hashtable = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.hashtable)
        

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return len(self.hashtable) - self.hashtable.count(None)

    # def fnv1(self, key):
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """
    #     pass
    #     # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
    
        return hash & 0xFFFFFFFF
        # Your code here
        

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)

        self.hashtable[i] = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        self.hashtable[i] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)

        return self.hashtable[i]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")


# data = [None] * 16  # Size should be a power of 2
# ​
# def my_hash(s):
# 	"""Beej's naive hashing function"""
# ​
# 	sb = s.encode()
# ​
# 	total = 0
# ​
# 	for b in sb:
# 		total += b
# 		total &= 0xffffffff  # add this for a 32-bit hashing function
# 		#total &= 0xffffffffffffffff  # add this for a 64-bit hashing function
# ​
# 	return total
# ​
# def get_index(s):
# 	h = my_hash(s)
# ​
# 	i = h % len(data)
# ​
# 	return i
# ​
# def put(k, v):
# 	# Get the index into "data" to store "v"
# 	i = get_index(k)
# ​
# 	# Store v there
# 	data[i] = v
# ​
# def get(k):
# 	i = get_index(k)
# ​
# 	return data[i]
# ​
# def delete(k):
# 	i = get_index(k)
# ​
# 	data[i] = None
# ​
# ​
# if __name__ == "__main__":
# ​
# 	put("beej", 3490)
# 	put("goats", 999)
# 	put("beej", "hello")
# ​
# 	print(data)
# ​
# 	print(get("beej"))
# ​
# 	#print(my_hash("beej"))
# 	#print(my_hash("goats"))
# ​
# 	#print(get_index("beej"))
# 	#print(get_index("goats"))
# 	#print(get_index("foo"))
# 	#print(get_index("bar"))
# 	#print(get_index("baz"))
# 	#print(get_index("qux"))
# ​
# ​
