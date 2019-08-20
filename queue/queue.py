# class Queue:
#   def __init__(self):
#     self.size = 0
#     # what data structure should we
#     # use to store queue elements?
#     self.storage = []

#   def enqueue(self, item):
#      self.storage.append(item)
#      # self.storage.insert(0, item) also works
#      self.size += 1
  
#   def dequeue(self):
#     if self.size == 0:
#       return None
#     else:
#       self.size -= 1
#       return self.storage.pop(0)

#   def len(self):
#     return self.size
import sys
sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = DoublyLinkedList()

  def enqueue(self, item):
     self.storage.add_to_tail(item)
     # self.storage.insert(0, item) also works
     self.size += 1
  
  def dequeue(self):
    if self.size == 0:
      return None
    else:
      self.size -= 1
      return self.storage.remove_from_head()

  def len(self):
    return self.size