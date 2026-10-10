# # Complete Linked List Implementation with Important Operations

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # ---------------------------
#     # Print Linked List
#     # ---------------------------
#     def print_list(self):
#         curr = self.head

#         if curr is None:
#             print("Linked List is empty")
#             return

#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next

#         print("None")

#     # ---------------------------
#     # Insert at Beginning
#     # ---------------------------
#     def insert_beginning(self, data):
#         new_node = Node(data)

#         new_node.next = self.head
#         self.head = new_node

#     # ---------------------------
#     # Insert at End
#     # ---------------------------
#     def insert_end(self, data):
#         new_node = Node(data)

#         # Empty List
#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head

#         while curr.next:
#             curr = curr.next

#         curr.next = new_node

#     # ---------------------------
#     # Delete First Node
#     # ---------------------------
#     def delete_first(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         self.head = self.head.next

#     # ---------------------------
#     # Delete Last Node
#     # ---------------------------
#     def delete_last(self):
#         if self.head is None:
#             print("List is empty")
#             return

#         # Only one node
#         if self.head.next is None:
#             self.head = None
#             return

#         curr = self.head

#         while curr.next.next:
#             curr = curr.next

#         curr.next = None

#     # ---------------------------
#     # Search Element
#     # ---------------------------
#     def search(self, key):
#         curr = self.head
#         position = 1

#         while curr:
#             if curr.data == key:
#                 return f"{key} found at position {position}"

#             curr = curr.next
#             position += 1

#         return f"{key} not found"

#     # ---------------------------
#     # Reverse Linked List
#     # ---------------------------
#     def reverse(self):
#         prev = None
#         curr = self.head

#         while curr:
#             next_node = curr.next

#             curr.next = prev

#             prev = curr
#             curr = next_node

#         self.head = prev

#     # ---------------------------
#     # Find Middle Node
#     # ---------------------------
#     def find_middle(self):
#         if self.head is None:
#             return None

#         slow = self.head
#         fast = self.head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         return slow.data
#     # ---------------------------
#     # Detect Cycle
#     # ---------------------------
#     def detect_cycle(self):
#         slow = self.head
#         fast = self.head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True

#         return False

#     # ---------------------------
#     # Create Cycle (For Testing)
#     # Connect Last Node to Position
#     # ---------------------------
#     def create_cycle(self, pos):
#         if pos == 0:
#             return

#         cycle_node = None
#         curr = self.head
#         count = 1

#         while curr.next:
#             if count == pos:
#                 cycle_node = curr

#             curr = curr.next
#             count += 1

#         curr.next = cycle_node

#     # ---------------------------
#     # Merge Two Sorted Lists
#     # ---------------------------
#     @staticmethod
#     def merge_sorted(l1, l2):
#         dummy = Node(-1)
#         tail = dummy

#         p1 = l1.head
#         p2 = l2.head

#         while p1 and p2:

#             if p1.data <= p2.data:
#                 tail.next = p1
#                 p1 = p1.next
#             else:
#                 tail.next = p2
#                 p2 = p2.next

#             tail = tail.next

#         if p1:
#             tail.next = p1

#         if p2:
#             tail.next = p2

#         merged = LinkedList()
#         merged.head = dummy.next

#         return merged


# # ====================================================
# # DRIVER CODE
# # ====================================================

# ll = LinkedList()

# print("Insert at End:")
# ll.insert_end(10)
# ll.insert_end(20)
# ll.insert_end(30)
# ll.print_list()

# print("\nInsert at Beginning:")
# ll.insert_beginning(5)
# ll.print_list()

# print("\nDelete First Node:")
# ll.delete_first()
# ll.print_list()

# print("\nDelete Last Node:")
# ll.delete_last()
# ll.print_list()

# print("\nSearch:")
# print(ll.search(20))
# print(ll.search(100))

# print("\nReverse:")
# ll.reverse()
# ll.print_list()

# print("\nMiddle Node:")
# print(ll.find_middle())

# print("\nDetect Cycle:")
# print(ll.detect_cycle())

# # Uncomment to test cycle detection
# # ll.create_cycle(2)
# # print(ll.detect_cycle())


# print("\nMerge Two Sorted Lists:")

# list1 = LinkedList()
# list1.insert_end(1)
# list1.insert_end(3)
# list1.insert_end(5)

# list2 = LinkedList()
# list2.insert_end(2)
# list2.insert_end(4)
# list2.insert_end(6)

# merged = LinkedList.merge_sorted(list1, list2)

# print("List 1:")
# list1.print_list()

# print("List 2:")
# list2.print_list()

# print("Merged:")
# merged.print_list()


# def f(x=[]):
#     x.append(1)
#     return x
#
# print(f(),f())
# # print(f())
# # print(f())
#



# print(0.1+0.2==0.3)
# => False


# print(bool(0))

# print(isinstance(True, int))
# =>True 


# print(isinstance(True, bool))
# print(isinstance(True, float))
# print(isinstance(True, str))
# print(isinstance([True], list))
# print(isinstance('abc', str))


# print(list(zip([1,2,3],[4,5,6],['a','b','c'])))

# # l=[1,2,3]
# d={x:x**2 for x in range(5)}
# print(d)

# l=[1,9,6,2]
# # l.sort()
# print(sorted(l))


# a=[[1,2]]
# b=a*3
# print(b)
# b[0][0]=99
# print(b)

# print(bool([[]]))
# # True
# print(bool(((()))))
# # False


# d={}
# print(type(d))
# d=set(d)
# print(type(d))



def scoreOfString(s):
    score=0
    for ch in range(1,len(s)):
        score+=abs(ord(s[ch])-ord(s[ch-1]))
    
    return score

print(scoreOfString("hello"))