import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
  # Need to store key/value pairs - so dict
  # something to store the cache
  # Size of the cache and max capacity
  def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.storage = dict()
    self.order = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Make sure we handle a situation when the key is not present
    if key in self.storage:
      # Move the retrieved item to the head
      node = self.storage[key]
      self.order.move_to_front(node)
      # Return value associated with a given key
      return node.value[1]

    else:
      return None
  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # if the key is already in the cache, update the value and move to head
    if key in self.storage:
      node = self.storage[key]
      node.value = (key, value)
      self.order.move_to_front(node)
      return

    # if the key is at limit, then the oldest entry will be removed
    if self.size == self.limit:
      del self.storage[self.order.tail.value[0]]
      self.order.remove_from_tail()
      self.size -= 1

    # 3 Tasks
    # 1. Add the key value pair to head of LL
    self.order.add_to_head((key, value))
    # 2. Add to the Dict
    self.storage[key] = self.order.head
    # 3. Increase size
    self.size += 1