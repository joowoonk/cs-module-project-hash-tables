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
        if capacity >= MIN_CAPACITY:
            self.capacity = capacity
        else:
            self.capacity = MIN_CAPACITY
        
        self.hashtable = [HashTableEntry(None, None)] *self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity        

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return len(self.hashtable) / len(self.capacity)

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
        current = self.hashtable[i]
        checking = True

        while checking:
            if current.key:
                if current.key != key:
                    if current.next:
                        current = current.next
                    else:
                        current.next = HashTableEntry(key, value)
                else:
                    current.value = value
                    checking = False
            else:
                current.key = key
                current.value = value
                checking = False


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        # warning message, if there is no key.. 

        Implement this.
        """
        # Your code here
        ind = self.hash_index(key)

        current = self.hashtable[ind]
        found = current.key
        checking = True
        while checking == True:
            if current.key:
                if current.key != key:
                    if current.next:
                        current = current.next
                    else:
                        return None
                else:
                    found = current.key
                    current.value = None
                    return found
            else:
                return None



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        ind = self.hash_index(key)

        current = self.hashtable[ind]

        checking = True

        while checking:
            if current.key:
                if current.key != key:
                    if current.next:
                        current = current.next
                    else:
                        return None

                else:
                    return current.value
            else:
                return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity

        old_hashtable = self.hashtable

        self.hashtable = [HashTableEntry(None, None)] * self.capacity

        checking = False

        for i in old_hashtable:
            self.put(i.key, i.value)

            if i.next:
                checking = True
                current = i.next
                while checking:
                    self.put(current.key, current.value)
                    if not current.next:
                        checking = False
                    else:
                        current = current.next


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
