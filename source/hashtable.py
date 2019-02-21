from linkedList import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(log n) we have to loop through every bucket and then every item"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(?) Why and under what conditions?"""
        all_vals = []
        for b in self.buckets:  #   iterate through every bucket
            for k, v in b.iterate(): #   in each bucket iterate through items
                all_vals.append(v)  #   for each item append value
        return all_vals #   return all values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(1) we are storing a size counter in the class"""
        return self.size #  returns the size of hashtable

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1) Hashtables have a constant lookup time"""
        try:
            self.get(key)   #  try hashtables get method
            return True #  if it returns an item return true
        except:
            return False  #  if get method throws error return false

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) hashtables have a constant lookup time"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        index = self._bucket_index(key)
        for item in self.buckets[index].iterate():
            if item[0] == key:
                return item[1]
        raise KeyError('Key not found: {}'.format(key)) #   raise error if not

    #*NOTE: this set method uses CHAINING
    # def set(self, key, value):
    #     """Insert or update the given key with its associated value.
    #     TODO: Running time: O(1) constant time to add to a hashtable"""
    #     # TODO: Find bucket where given key belongs
    #     # TODO: Check if key-value entry exists in bucket
    #     # TODO: If found, update value associated with given key
    #     # TODO: Otherwise, insert given key-value entry into bucket
    #     index = self._bucket_index(key) #   find bucket index for key
    #     self.size += 1  #  increment size counter
    #     for item in self.buckets[index].iterate():    # iterate over items in bucket
    #         if item[0] == key:  #   if item in bucket
    #             self.size -= 1  #  item already in list, decrement counter
    #             self.buckets[index].delete(item) #   DELETE item
    #     self.buckets[index].append((key, value)) #  append new item to bucket
    
    #*NOTE: this set method uses LINEAR PROBING
    def set(self, key, value):
        """ Inserts or updates given key with its associated value """
        index = self._bucket_index(key)
        self.size += 1
        bucket = self.buckets[index]
        if bucket.is_empty():
            bucket.append((key, value))
            return
        elif bucket.is_empty() == False and bucket.head.data[0] == key:
            bucket.head = None
            bucket.tail = None
            self.size -= 1
            bucket.append((key, value))
            return 
        else:
            while bucket.is_empty() == False:
                if bucket.head.data[0] == key:
                    bucket.head = None
                    bucket.tail = None
                    self.size -= 1
                    bucket.append((key, value))
                    return
                if index + 1 < len(self.buckets):
                    bucket = self.buckets[index + 1]
                else:
                    index = 0
                    bucket = self.buckets[index]
            bucket.append((key, value))

        

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        b = self.buckets[self._bucket_index(key)]  #  grab bucket key would be in 
        for item in b.iterate(): #  iterate over items in bucket
            if item[0] == key:  #  if item exists 
                b.delete(item)  #  use linkedlist delete method to remove from bucket
                self.size -= 1  #  decrement our size counter
                return  #  end function!
        raise KeyError('KEY: {} was not found in hashtable.'.format(key))  #  key not in bucket, throw error
        
        


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    # test_hash_table()
    ht = HashTable(9)
    ht.set("hello", 4)
    ht.set("olleh", 6)
    ht.set("something", 9)
    ht.set("else", 10)
    ht.set("connor", 19)
    # ht.set("bobby", 100)
    # ht.set("louis", 9)
    # ht.set("blue", 91)
    # ht.set("black", 999)

    print(ht)
    print(ht.buckets)
