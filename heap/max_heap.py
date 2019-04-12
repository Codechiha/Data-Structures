class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    deleted = self.storage[0]
    del self.storage[0]
    self._sift_down(0)
    return deleted

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    #Parent Node = (Index - 1) // 2
    #While Parent Node is 0 or greater
    while (index - 1) // 2 >= 0:
      parent = (index - 1) // 2
      # if Current (Index) Node value > Parent Node value
      if self.storage[index] > self.storage[parent]:
          # Swap 
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
      # Update the Indices of the swapped values 
      index = parent

  def _sift_down(self, index):
    pass