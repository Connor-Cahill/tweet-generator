class Bucket:

  def __init__(self):
    """ creates new instance of hash table node """
    self.data = None  #  create data and set to nones

  def is_empty(self):
    """ returns true if node is empty """
    return self.data is None  #  returns true if data is empty

  def delete(self):
    """Removes data from node """
    self.data = None
  
  def __repr__(self):
    """ prints string representation of node """
    return ' [ {} ] '.format(self.data)

  def __str__(self):
    return ' [ {} ] '.format(self.data)




class Hash_Table:
  """
  Hash Table implemented with linear probing. Currently this hash table is
  restricted to the amount of buckets (init_size)
  """
  def __init__(self, init_size=8):
    """ creates new instance of hash table """
    self.buckets = [Bucket() for _ in range(init_size)]
    self.size = 0

  def __str__(self):
    """Return a formatted string representation of this hash table."""
    ret = ['{} : {}'.format(item.data[0], item.data[1]) for item in self.buckets if item.data is not None]
    return '{' + ', '.join(ret) + '}'


  def __repr__(self):
      """Return a string representation of this hash table."""
      return 'Hash Table: {}'.format(item.data for item in self.buckets)

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
      """Insert or update the given key with its associated value. """     
      index = self._bucket_index(key) #   find bucket index for key
      self.size += 1  #  increment size counter
      bucket = self.buckets[index]  #  grab starting bucket
      if bucket.is_empty():  #  check if bucket is empty
        bucket.data = (key, value)  #  if it is add the data
        return  #  break the function 
      #  loop until bucket key equal inputted key or bucket is empty
      while bucket.is_empty() == False or bucket.data[0] != key:
        index += 1  #  increment index 
        if index >= len(self.buckets):  # if index greater than num buckets
          bucket = self.buckets[index % len(self.buckets)]  #  mod the index
        else:
          bucket = self.buckets[index]  #  assign incremented index
        if bucket.is_empty():
          break
      bucket.data = (key, value)  #  assign new data to bucket
        
        
      
  def get(self, key):
    """ returns value of given key """
    index = self._bucket_index(key)  #  grab index of starting bucket
    bucket = self.buckets[index]  #  grab starting bucket
    for _ in range(len(self.buckets)):  #  loop for len of buckets (self.buckets)
      if index >= len(self.buckets):  # if index is greater than len(buckets)
        bucket = self.buckets[index % len(self.buckets)] #  mod the index
      else:
        bucket = self.buckets[index]  #  assign new index
      if bucket.data[0] == key:  #  if key in bucket equal inputted key
        return bucket.data[1]  #  return the value
      index += 1  #  increment the index
    raise KeyError('KEY: {} not in hashtable')  #  every node has been touch, no key, raise error

  def delete(self, key):
    """Delete the given key from hashtable or Raise Error """
    index = self._bucket_index(key)  #  grab starting index
    bucket = self.buckets[index]  #  grab starting bucket
    for _ in range(len(self.buckets)):  #  loop for number of buckets
      if index >= len(self.buckets):  #  if index greater than num buckets 
        bucket = self.buckets[index % len(self.buckets)]  #  mod index
      else:
        bucket = self.buckets[index]  #  assign new index
      if bucket.data[0] == key:  #  if key in bucket equal inputted key 
        bucket.delete() # delete the data from the bucket
        self.size -= 1  #  decrement the size of hashtable
        return  # break the function
      index += 1  #  increment index 
    raise KeyError("KEY: {} was not found in hashtable.")  #  key not found, throw error
    


def test_ht():
  """ runs some test methods on hash table """
  ht = Hash_Table()
  ht.set("my_key", 5)
  ht.set("duder", 69)
  ht.set("lady", 122)
  ht.set("something", 14)
  ht.set("hello", 10)
  print(ht)
  ht.delete('hello')
  print(ht)

if __name__ == "__main__":
  test_ht()