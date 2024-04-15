class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.last = None
        self.gluon = None

class LinkedList: 
    def __init__(self):
        self.head = None
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            
    
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, data):
        
        if not prev_node:
            print("Pevious node is not in the list")
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        ##Not Working##
        
        if key_1 == key_2:
            return

        prev_1 = None
        curr_n = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_1.next = curr_1
        else:
            self.head = curr_1

        curr_n = curr_1.next
        curr_1.next = curr_2.next
        curr_2.next = curr_n.next            

llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
##llist.insert_after_node(llist.head.next.next, 'E')
print(llist.len_recursive(llist.head))
##print(llist.head.next.data, "\n")
llist.print_list()
print("\n")
llist.swap_nodes('B', 'C')
print(llist.len_recursive(llist.head))
llist.print_list()

