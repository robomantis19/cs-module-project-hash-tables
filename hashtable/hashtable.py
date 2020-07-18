

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.count = 0
        self.head = None
        
    def addHash(self, node, oldValue = None):
        node = HashTableEntry(node.key, node.value)
        if self.head is None: 
            self.head = node
            return self.head
        else: 
            current = self.head

            while current.next is not None: 
                current = current.next
            current.next = node
            return current.next
        # while current != None: 
        #     next_node = self.next
        #     next_node = current
        #     self.count = self.count + 1
        #     self.head = next_node
        #     current = None
                   
        # print('length of node', self.count)
        # current = node
        # return current

    def deleteHash(self, key):
        HashToDelete = self.getHash(key)
        HashToDelete.key = None
        HashToDelete.value = None
        return HashToDelete



    def getHash(self, indexKey):
        
        current = self.head
       
        while current is not None: 
            if current.key == indexKey:
                return current
            current = current.next
        return None

    def overwrite(self, oldKey, oldValue):
        oldInput = self.getHash(oldKey) 
        oldInput.value = oldValue
        print('oldInput', oldInput)
        return oldInput
       


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable():
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        
        self.capacity = [None] * MIN_CAPACITY
        print('capacity', self.capacity)
        self.Node = HashTableEntry(None, None)
      
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        count = 0
        for i in self.capacity: 
            count += 1
        return count



    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hval = 0x811c9dc5
        prime = 0x01000193
        size = 2**32
        if not isinstance(key, bytes):
            key = key.encode("UTF-8", "ignore")
        for i in key: 
            hashv = (hval * prime) % size
            hashv = hashv ^ i
        return hashv


        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % len(self.capacity)
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # hashNumber = self.hash_index(key)
        # self.capacity[hashNumber] = value
        
        node = HashTableEntry(key, value)
        hashNumber = self.hash_index(key)
        oldValue = self.Node.getHash(key)
        self.capacity[hashNumber] = self.Node.addHash(node)
        if oldValue:
            self.capacity[hashNumber] = self.Node.overwrite(key, value)
            return self.capacity[hashNumber].value
        print(self.capacity)
        return self.capacity



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hashNumber = self.hash_index(key)
        self.capacity[hashNumber] = self.Node.deleteHash(key)
        DeletedHash = self.capacity[hashNumber]
        print('-------------Delete: ', DeletedHash)
        return DeletedHash


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # hashNumber = self.hash_index(key)
        # return self.capacity[hashNumber]
        
        hashNumber = self.hash_index(key)
        linkedListofHashes = self.capacity[hashNumber]
        print('linkedListofHashes key, value: ', linkedListofHashes)
        nodeValue = self.Node.getHash(key)
        if nodeValue != None:
            print('nodeValue: ', nodeValue.key, nodeValue.value)
            return nodeValue.value
        else: 
            print('nodeValue: None')
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        NoneCount = 0
        FullCount = 0

        for i in self.capacity: 
            if i == None: 
                NoneCount += 1
            else: 
                FullCount += 1
        bucketPercent = FullCount/len(self.capacity)
        print('+++++++bucket percentage, fullcount, noneCount, total: ', bucketPercent, FullCount, NoneCount, len(self.capacity))
        # Your code here
        if bucketPercent > .7:
            if type(new_capacity) == int: 
                self.capacity = [None] * new_capacity

            elif type(new_capacity) == list:
                self.capacity = [None] * len(new_capacity)
                print('number of slots ++++++ : ', self.get_num_slots())
                self.resize(self.capacity)
            

# node_end_list = HashTableEntry()
# print(node_end_list)

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
