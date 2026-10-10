class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_values(self,values):
        for val in values:
            self.insert_at_end(val)


    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node


    def print_list(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print()


    def reverse(self):
        prev=None
        current=self.head

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

values=list(map(int,input().split()))
ll=LinkedList()

ll.insert_values(values)

ll.print_list()

ll.reverse()

ll.print_list()