import time

class Node:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None
        self.prev = None
        self.arm = None
        
class DoubleNodeDoubly:
    def __init__(self):
        self.head = None

    def append(self, data1, data2):
       if self.head is None:
           double_node = Node(data1, data2)
           double_node.prev = None
           self.head = double_node
       else:
            double_node = Node(data1, data2)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = double_node
            double_node.prev = cur
            double_node.next = None

    def link_lists(self, L2):
        first_node2 = L2.head
        
        if self.head is None:       
            return
        else:
            cur = self.head
            while cur.next:
                cur.arm = first_node2
                cur = cur.next                
            cur.arm = first_node2
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data1, cur.data2)
            cur = cur.next

    def print_list_arms(self):
        cur = self.head
        while cur:
            print(cur.data1, cur.data2, cur.arm)
            cur = cur.next

dllist1 = DoubleNodeDoubly()

print("Linked List Started...")

file = open("mil.txt", "r")
lines = file.readlines()

main_time = time.time()
new_time = time.time()

print("for loop beginning now...")

x = 0
    
for line in lines:
    x += 1

    dllist1.append(line, None)
    print(x, " --- %s seconds ---" % (time.time() - new_time))


print("URL List Built in:")
print("--- %s seconds ---" % (time.time() - start_time))

print(dllist1.print_list())

dllist2 = DoubleNodeDoubly()

dllist2.append('a',None)
dllist2.append('c',None)
dllist2.append('e',None)
dllist2.append('g',None)
dllist2.append('i',None)

print(dllist2.print_list())

dllist3 = DoubleNodeDoubly()

dllist3.append(0,None)
dllist3.append(2,None)
dllist3.append(3,None)
dllist3.append(5,None)
dllist3.append(6,None)

print(dllist3.print_list())

dllist1.link_lists(dllist2)

dllist2.link_lists(dllist3)
            
print(dllist1.print_list_arms())
print(dllist2.print_list_arms())

print(dllist2.head)
print(dllist3.head)

print(x, " --- %s seconds ---" % (time.time() - new_time))

##dllist1.append('a',None)
##dllist1.append('b',None)
##dllist1.append('c',None)
##dllist1.append('d',None)
##dllist1.append('e',None)
##dllist1.append('f',None)
##dllist1.append('g',None)
##dllist1.append('h',None)
##dllist1.append('h',None)
##dllist1.append('j',None)
##dllist1.append('k',None)
##dllist1.append('l',None)
##dllist1.append('m',None)
##dllist1.append('n',None)
##dllist1.append('o',None)
##dllist1.append('p',None)
##dllist1.append('q',None)
##dllist1.append('r',None)
##dllist1.append('s',None)
##dllist1.append('t',None)
##dllist1.append('u',None)
##dllist1.append('v',None)
##dllist1.append('w',None)
##dllist1.append('x',None)
##dllist1.append('y',None)
##dllist1.append('z',None)
