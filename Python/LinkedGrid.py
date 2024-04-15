class Node:
    def __init__(self, data):
        self.data = data
        self.east = None
        self.west = None
        self.south = None
        self.north = None
        self.southeast = None
        self.southwest = None
        self.northeast = None
        self.northwest = None

class LinkedGrid:
    def __init__(self):
        self.head = None

    def link_from_top(self, data):
        cur = self.head
        cur2 = data.head
        cur3 = data.head.east
        
        n = 0
        a = 0
        z = 0

        cur.south = cur2
        
        while cur.east:
            a += 1
            n = 0
            cur = cur.east
            cur2 = data.head

            while cur2.east:
                cur2 = cur2.east
                south = cur2
                n += 1
                if n is a:                                      
                    cur.south = south

    def link_se_from_top(self, data):
        cur = self.head
        cur2 = data.head
        
        n = 0
        a = 0
        z = 0

        cur.southeast = cur2.east

        while cur.east:
            a += 1
            n = 0
            cur = cur.east
            cur2 = data.head

            while cur2.east:
                cur2 = cur2.east
                southeast = cur2.east
                n += 1
                if n is a:                                      
                    cur.southeast = southeast

    def link_sw_from_top(self, data):
        cur = self.head
        cur2 = data.head
        
        n = 0
        a = 0
        z = 0

        cur.southwest = cur2.west

        while cur.east:
            a += 1
            n = 0
            cur = cur.east
            cur2 = data.head

            while cur2.east:
                cur2 = cur2.east
                southwest = cur2.west
                n += 1
                if n is a:                                      
                    cur.southwest = southwest

    def link_ne_from_top(self, data):
        cur = self.head
        cur2 = data.head
        
        n = 0
        a = 0
        z = 0

        cur.northeast = cur2.east

        while cur.east:
            a += 1
            n = 0
            cur = cur.east
            cur2 = data.head

            while cur2.east:
                cur2 = cur2.east
                northeast = cur2.east
                n += 1
                if n is a:                                      
                    cur.northeast = northeast

    def link_nw_from_top(self, data):
        cur = self.head
        cur2 = data.head
        
        n = 0
        a = 0
        z = 0

        cur.northwest = cur2.west

        while cur.east:
            a += 1
            n = 0
            cur = cur.east
            cur2 = data.head

            while cur2.east:
                cur2 = cur2.east
                northwest = cur2.west
                n += 1
                if n is a:                                      
                    cur.northwest = northwest
            
    def append(self, data):
       if self.head is None:
           new_node = Node(data)
           new_node.west = None
           new_node.south = None
           new_node.north = None
           self.head = new_node
       else:
            new_node = Node(data)
            cur = self.head
            while cur.east:
                cur = cur.east
            cur.east = new_node
            new_node.west = cur
            new_node.east = None
            new_node.south = None
            new_node.north = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.west = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.west = new_node
            new_node.east = self.head
            self.head = new_node
            new_node.west = None

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.east is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.east
                cur.east = new_node
                new_node.east = nxt
                new_node.west = cur
                nxt.west = new_node
            cur = cur.east
            
    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.west is None and cur.data == key:
                self.prepend(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.west
                prev.east = new_node
                cur.west = new_node
                new_node.east = cur
                new_node.west = prev
            cur = cur.east                                
    
    def print_list(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node location: ', cur)
            cur = cur.east

    def print_list_south(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node southern link: ',cur.south)
            cur = cur.east

    def print_list_southeast(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node southeastern link: ',cur.southeast)
            cur = cur.east

    def print_list_southwest(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node southwestern link: ',cur.southwest)
            cur = cur.east

    def print_list_northeast(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node northeastern link: ',cur.northeast)
            cur = cur.east

    def print_list_northwest(self):
        cur = self.head
        while cur:
            print('node data: ', cur.data)
            print('node northwestern link: ',cur.northwest)
            cur = cur.east
            
dllist = LinkedGrid()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

dllist2 = LinkedGrid()

dllist2.append(6)
dllist2.append(7)
dllist2.append(8)
dllist2.append(9)
dllist2.append(10)

dllist3 = LinkedGrid()

dllist3.append(11)
dllist3.append(12)
dllist3.append(13)
dllist3.append(14)
dllist3.append(15)

dllist4 = LinkedGrid()

dllist4.append(16)
dllist4.append(17)
dllist4.append(18)
dllist4.append(19)
dllist4.append(20)

dllist5 = LinkedGrid()

dllist5.append(21)
dllist5.append(22)
dllist5.append(23)
dllist5.append(24)
dllist5.append(25)


dllist.link_from_top(dllist2)
dllist2.link_from_top(dllist3)
dllist3.link_from_top(dllist4)
dllist4.link_from_top(dllist5)

dllist.link_se_from_top(dllist2)
dllist.link_sw_from_top(dllist2)
dllist2.link_ne_from_top(dllist)
dllist2.link_nw_from_top(dllist)

dllist2.link_se_from_top(dllist3)
dllist2.link_sw_from_top(dllist3)
dllist3.link_ne_from_top(dllist2)
dllist3.link_nw_from_top(dllist2)

dllist3.link_se_from_top(dllist4)
dllist3.link_sw_from_top(dllist4)
dllist4.link_ne_from_top(dllist3)
dllist4.link_nw_from_top(dllist3)

dllist4.link_se_from_top(dllist5)
dllist4.link_sw_from_top(dllist5)
dllist5.link_ne_from_top(dllist4)
dllist5.link_nw_from_top(dllist4)

dllist2.print_list()
print('\n')
dllist.print_list_south()
print('\n')
dllist.print_list_southeast()
print('\n')
dllist.print_list_southwest()
print('\n')
dllist2.print_list_northeast()
print('\n')
dllist2.print_list_northwest()
print('\n')
dllist.print_list()


