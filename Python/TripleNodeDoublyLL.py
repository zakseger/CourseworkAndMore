class Node:
    def __init__(self, data1, data2, data3):
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.next = None
        self.prev = None

class TripleNodeDoubly:
    def __init__(self):
        self.head = None

    def append(self, data1, data2, data3):
       if self.head is None:
           triple_node = Node(data1, data2, data3)
           triple_node.prev = None
           self.head = triple_node
       else:
            triple_node = Node(data1, data2, data3)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = triple_node
            triple_node.prev = cur
            triple_node.next = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data1, cur.data2, cur.data3)
            cur = cur.next

dllist = TripleNodeDoubly()
dllist.append([0,0,0], 1, "string")
dllist.append(3,4,5)
dllist.append(6,7,8)
dllist.append(9,10,11)
dllist.append(12,13,14)

print(dllist.print_list())
