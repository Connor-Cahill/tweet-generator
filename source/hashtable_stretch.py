class Ht_Node:

  def __init__(self, data):
    """ creates new instance of hash table node """
    self.data = data

  def is_empty(self):
    return self.data is None  #  returns true if data is empty
  
  def __repr__(self):
    """ prints string representation of node """
    return 'Node -->  [[ {} ]]'.format(self.data)


class Hash_Table:
  
  def __init__(self, init_size=8):
    """ creates new instance of hash table """
    self.buckets = [Ht_Node() for _ in range(init_size)]
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
    
    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) constant time to add to a hashtable"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key) #   find bucket index for key
        self.size += 1  #  increment size counter
        for item in self.buckets[index].iterate():    # iterate over items in bucket
            if item[0] == key:  #   if item in bucket
                self.size -= 1  #  item already in list, decrement counter
                self.buckets[index].delete(item) #   DELETE item
        self.buckets[index].append((key, value)) #  append new item to bucket
      
    def get(self, key):
      """ returns value of given key """
      pass

    def delete(self, key):
        """Delete the given key from hashtable or Raise Error """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        while bucket.head.data[0] != key:
            if index + 1 < len(self.buckets):
                index += 1
                bucket = self.buckets[index]
            else:
                index = 0
                bucket = self.buckets[index]
        if bucket.head.data[0] == key:
            bucket.delete(key)
            return
        else: 
            raise KeyError("KEY: {} was not found in hashtable.")