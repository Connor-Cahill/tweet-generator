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
  
  def __init__(self, num_buckets=8):
    """ creates new instance of hash table """
    self.buckets = [Bucket() for _ in range(num_buckets)]
    self.num_buckets = num_buckets
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
      for b in self.buckets:  #  iterate through all buckets
        if not b.is_empty():
          all_keys.append(b.data[0])  #  append keys
      return all_keys
  
  def contains(self, key):
    """ returns bool on whether key exists in hashtable """
    index = self._bucket_index(key)
    for _ in range(len(self.buckets)):
      if index >= len(self.buckets):
        bucket = self.buckets[index % len(self.buckets)]
      else:
        bucket = self.buckets[index]
      if not bucket.is_empty():
        if bucket.data[0] == key:
          return True
      index += 1
    return False

  def values(self):
      """Return a list of all values in this hash table.
      TODO: Running time: O(?) Why and under what conditions?"""
      all_vals = []
      for b in self.buckets:  #  Iterate through all buckets
        if not b.is_empty():
          all_vals.append(b.data[1])  #  append values
      return all_vals

  def items(self):
      """Return a list of all items (key-value pairs) in this hash table.
      TODO: Running time: O(???) Why and under what conditions?"""
      # Collect all pairs of key-value entries in each bucket
      all_items = []  
      for bucket in self.buckets:
          if not bucket.is_empty(): #  make sure bucket is not empty
            all_items.append((bucket.data[0], bucket.data[1]))  #  appending key, value tuple 
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
    while not bucket.is_empty() or self.contains(key):
      index += 1  #  increment index 
      if index >= len(self.buckets):  # if index greater than num buckets
        bucket = self.buckets[index % len(self.buckets)]  #  mod the index
      else:
        bucket = self.buckets[index]  #  assign incremented index
      if not bucket.is_empty():
        if bucket.data[0] == key: #  if bucket's key is the inputted key
          self.size -= 1  #  key already in hash table decrement counter
          break
    bucket.data = (key, value)  #  assign new data to bucket
    if self.buckets_full():
      print('Buckets are full!')
      self.more_buckets()
      
        
        
      
  def get(self, key):
    """ returns value of given key """
    index = self._bucket_index(key)  #  grab index of starting bucket
    bucket = self.buckets[index]  #  grab starting bucket
    for _ in range(len(self.buckets)):  #  loop for len of buckets (self.buckets)
      if index >= len(self.buckets):  # if index is greater than len(buckets)
        bucket = self.buckets[index % len(self.buckets)] #  mod the index
      else:
        bucket = self.buckets[index]  #  assign new index
      if not bucket.is_empty():
        if bucket.data[0] == key:  #  if key in bucket equal inputted key
          return bucket.data[1]  #  return the value
      index += 1  #  increment the index
    raise KeyError('KEY: {} not in hashtable'.format(key))  #  every node has been touch, no key, raise error

  def delete(self, key):
    """Delete the given key from hashtable or Raise Error """
    index = self._bucket_index(key)  #  grab starting index
    bucket = self.buckets[index]  #  grab starting bucket
    for _ in range(len(self.buckets)):  #  loop for number of buckets
      if index >= len(self.buckets):  #  if index greater than num buckets 
        bucket = self.buckets[index % len(self.buckets)]  #  mod index
      else:
        bucket = self.buckets[index]  #  assign new index
      if not bucket.is_empty(): # make sure bucket is NOT empty 
        if bucket.data[0] == key:  #  if key in bucket equal inputted key 
          bucket.delete() # delete the data from the bucket
          self.size -= 1  #  decrement the size of hashtable
          return  # break the function
      index += 1  #  increment index 
    raise KeyError("KEY: {} was not found in hashtable.")  #  key not found, throw error
  
  def buckets_full(self):
    """ if hash table is 2/3ish full returns true """
    
    if self.size / len(self.buckets) >= 2 / 3:
      return True
    else: 
      return False


  #* Note key and value are for missed item appended
  def more_buckets(self):
    """ copies all items in current hash table then makes new HT with more buckets """
    items  = self.items()
    new_size = len(self.buckets) * 2
    print(new_size)
    # self = Hash_Table(new_size)
    self.__init__(new_size)
    # print(self)
    for item in items:
      self.set(item[0], item[1])
    return self
    
  
    
    
    


def test_ht():
  """ runs some test methods on hash table """
  ht = Hash_Table()
  ht.set("my_key", 5)
  ht.set("duder", 69)
  ht.set("lady", 122)
  ht.set("something", 14)
  ht.set("hello", 10)
  # print(ht)
  ht.delete('hello')
  print(ht)
  ht.set("pink", 110)
  ht.set("black", 132)
  ht.set("other", 41)
  print('Far')
  ht.set("lemur", 123123)
  ht.set("dogg", 1233)
  ht.set("dogecoin", 123144)
  ht.set("leee", 235)
  ht.set("okey", 5423)
  ht.set("ikey", 1231)
  # print('not broken yet')
  ht.set("jakse", 9090)
  ht.set("cat", 913)
  ht.set("brown", 816)
  ht.set("nanny", 8888)
  # print(ht)
  # # print(ht.size)
  ht.set('brown', 12)
  ht.set("nanny", 11)
  # print('**FINISHED**')
  print(ht)
  # print(ht.get('brown'))

if __name__ == "__main__":
  test_ht()
  # ht = Hash_Table(4)
  # print(ht.num_buckets)
  # ht.set('green', 8)
  # ht.set('yellow', 4)
  # ht.set('blue', 1)
  # ht.set('nevy', 12)
  # ht.set('doge', 13)
  # ht.set('something', 14)
  # ht.set('nevy', 15)
  # ht.set('cat', 16)
  # ht.set('nephew', 17)
  # print(ht)
  # print(ht.num_buckets)
  # print('OVER WITH')