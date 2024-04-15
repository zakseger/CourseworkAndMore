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

    def split(self): 
        return list(self)

    def convert(self): 
        new = "" 
   
        for x in self: 
            new += x  
    
        return new 

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

    def build_layer(self, dllist):
        if self.head is None:
            return
        else:
            cur = self.head

            while cur is not None:
                if cur.next is not None:
                    cut = cur.data1

                    wList = []

                    for char in cut:
                        wList.append(char)

                    last = len(wList) - 1

                    if last > 1:
                        wList.pop(last)             ## Delete \n
                        wList.pop(last - 1)         ## Delete Last Character
                        
                        new = ""    
                        for x in wList: 
                            new += x
                            
                        new_word = new
                        
                        dllist.append(new_word, None)
                        
                    cur = cur.next
                else:
                    cur = self.head

                    while cur is not None:
                        cut = cur.data1

                        wList = []

                        for char in cut:
                            wList.append(char)

                        last = len(wList) - 1

                        if last > 1:
                            wList.pop(last)             ## Delete Last Character
                            
                            new = ""    
                            for x in wList: 
                                new += x
                                
                            new_word = new
                            
                            dllist.append(new_word, None)
                            
                        cur = cur.next
                    

    def build_layer_n(self, dllist):
        if self.head is None:
            return
        else:
            cur = self.head

            while cur is not None:
                cut = cur.data1

                wList = []

                for char in cut:
                    wList.append(char)

                last = len(wList) - 1

                if last > 1:
                    wList.pop(last)             ## Delete Last Character
                    
                    new = ""    
                    for x in wList: 
                        new += x
                        
                    new_word = new
                    
                    dllist.append(new_word, None)
                    
                cur = cur.next

                                    
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

       

print("Linked List Started...")

new_time = time.time()
full_time = time.time()

print("for loop beginning now...")

dllist1 = DoubleNodeDoubly()
    
dllist1.append('a',None)
dllist1.append('b',None)
dllist1.append('c',None)
dllist1.append('d',None)
dllist1.append('e',None)
dllist1.append('f',None)
dllist1.append('g',None)
dllist1.append('h',None)
dllist1.append('h',None)
dllist1.append('j',None)
dllist1.append('k',None)
dllist1.append('l',None)
dllist1.append('m',None)
dllist1.append('n',None)
dllist1.append('o',None)
dllist1.append('p',None)
dllist1.append('q',None)
dllist1.append('r',None)
dllist1.append('s',None)
dllist1.append('t',None)
dllist1.append('u',None)
dllist1.append('v',None)
dllist1.append('w',None)
dllist1.append('x',None)
dllist1.append('y',None)
dllist1.append('z',None)

dllist2 = DoubleNodeDoubly()

file = open("dictWords.txt", "r")
lines = file.readlines()

x = 0

for line in lines:
    x += 1
    dllist2.append(line, None)
    print(x," --- %s seconds ---" % (time.time() - new_time),line)

print("for loop complete")
    
print("Dictionary Words List Built in:")
print("--- %s seconds ---" % (time.time() - new_time), "\n")

dllist3 = DoubleNodeDoubly()
dllist4 = DoubleNodeDoubly()
dllist5 = DoubleNodeDoubly()
dllist6 = DoubleNodeDoubly()
dllist7 = DoubleNodeDoubly()
dllist8 = DoubleNodeDoubly()
dllist9 = DoubleNodeDoubly()
dllist10 = DoubleNodeDoubly()
dllist11 = DoubleNodeDoubly()
dllist12 = DoubleNodeDoubly()
dllist13 = DoubleNodeDoubly()
dllist14 = DoubleNodeDoubly()
dllist15 = DoubleNodeDoubly()
dllist16 = DoubleNodeDoubly()
dllist17 = DoubleNodeDoubly()
dllist18 = DoubleNodeDoubly()
dllist19 = DoubleNodeDoubly()
dllist20 = DoubleNodeDoubly()

new_time = time.time()

dllist2.build_layer(dllist3)
dllist3.build_layer_n(dllist4)
dllist4.build_layer_n(dllist5)
dllist5.build_layer_n(dllist6)
dllist6.build_layer_n(dllist7)
dllist7.build_layer_n(dllist8)
dllist8.build_layer_n(dllist9)
dllist9.build_layer_n(dllist10)
dllist10.build_layer_n(dllist11)
dllist11.build_layer_n(dllist12)
dllist12.build_layer_n(dllist13)
dllist13.build_layer_n(dllist14)
dllist14.build_layer_n(dllist15)
dllist15.build_layer_n(dllist16)
dllist16.build_layer_n(dllist17)
dllist17.build_layer_n(dllist18)
dllist18.build_layer_n(dllist19)

print("Layers Completed in: --- %s seconds ---" % (time.time() - new_time))

print(dllist16.print_list(), "\n")
print(dllist17.print_list(), "\n")
print(dllist18.print_list(), "\n")

print(dllist2.head)
print(dllist3.head)

print("Program Completed in: --- %s seconds ---" % (time.time() - full_time))
