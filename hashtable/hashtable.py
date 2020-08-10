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
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.entries = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.hash_table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Day 2
        return self.entries / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        hash = 5381  # Magic constant
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Day 1
        # index = self.hash_index(key)
        # new_entry = HashTableEntry(key, value)
        # self.hash_table[index] = new_entry.value

        # Day 2

        index = self.hash_index(key)
        new_entry = HashTableEntry(key, value)
        current = self.hash_table[index]

        if current is None:
            self.hash_table[index] = new_entry
            self.entries += 1
    
        else:
            while current is not None:
                # Overwrites if key currently exists
                if current.key is key:
                    current.value = value
                    return
                prev = current  # keeps a reference to the previous current entry
                current = current.next # will end up becoming None eventually
            prev.next = new_entry
            self.entries += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        # Day 1
        # if not self.hash_table[hash_key]:
        #     print("NAHHHHHHHHH")
        # self.hash_table[hash_key] = None

        # Day 2
        current = self.hash_table[index]

        if current is None:
            return print("nothing here to delete")
        elif current.key is key:
            current.value = None
            current = None
        else:
            while current.next:
                current = current.next
                if current.key is key:
                    current.value = None
                    current.next = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Day 1
        # index = self.hash_index(key)
        # if not self.hash_table[index]:
        #     return None
        # return self.hash_table[index]

        # Day 2
        index = self.hash_index(key)
        if self.hash_table[index] is None:
            return None
        if self.hash_table[index].key is key:
            return self.hash_table[index].value

        else:
            current = self.hash_table[index]
            while current.next is not None:
                current = current.next
                if current.key is key:
                    return current.value

            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_table = HashTable(
            new_capacity)  # creates a new hashtable of new capacity length
        for entry in self.hash_table:
            if entry:  # handles initial "head" entry
                new_table.put(entry.key, entry.value)
            if entry.next:
                current = entry
                while current.next:
                    current = current.next
                    new_table.put(current.key, current.value)
        self.hash_table = new_table.hash_table
        self.capacity = new_table.capacity


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

    for entry in ht.hash_table:
        print(entry.value)

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
