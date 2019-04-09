"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  # Output_list used to test methods with terminal

  def output_list(self):
    current_node = self.head

    while current_node is not None:
      print(current_node.value)
      current_node = current_node.next

    return

  def add_to_head(self, value):
    new_node = ListNode(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    if self.head is None:
      return None
    old_node = self.head
    self.head.delete()
    self.head = old_node.next

  def add_to_tail(self, value):
    new_node = ListNode(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      
  def remove_from_tail(self):
    if self.tail is not None:
      old_tail = self.tail
      old_tail.delete()
      self.tail = old_tail.prev

  def move_to_front(self, node):
    #error, how to access value of node
    self.head.insert_before(node)
    self.head = self.head.prev
    if node is self.tail:
      self.tail = self.tail.prev
    node.delete()

  def move_to_end(self, node):
    pass

  def delete(self, node):
    node.delete()
    
  def get_max(self):
    pass


node1 = ListNode('Hello')
node2 = ListNode(4)
node3 = ListNode('testing')

hell = DoublyLinkedList()

hell.add_to_tail('second to last')
hell.add_to_tail('tail')
hell.add_to_head('adding')
hell.add_to_head('new head')
# hell.remove_from_head()
hell.remove_from_tail()
hell.output_list()