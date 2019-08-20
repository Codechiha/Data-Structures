class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value == self.value:
      return
    elif self.value > value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)
    elif self.value < value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    #True, if tree contains this number
    if target == self.value:
      return True
    #True, if 
    if target > self.value:
      if self.right:
        if self.right.contains(target):
          return True
    else:
      if self.left:
        if self.left.contains(target):
          return True
    return False

  def get_max(self):
    if not self:
      return None
    if not self.right:
      return self.value
    return self.right.get_max()

  def for_each(self, cb):
    # for each node perform a callback function
    if self.left:
      self.left.for_each(cb)
    cb(self.value)
    if self.right:
      self.right.for_each(cb)
    cb(self.value)

  
