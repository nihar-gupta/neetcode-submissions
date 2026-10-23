# class LFUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.next = None 
        self.prev = None 
        self.freq = 1

class LFUCache:
    def __init__(self, capacity):

        # max capacity
        self.capacity = capacity

        # current no of nodes 
        self.current = 0

        # to hold all the nodes with same frequence
        self.freq_dict = dict()

        # to hold the keys with its nodes
        self.nodes = dict()

        # current least frequency available
        self.curr_freq = 1
        
    
    def get(self, key):
        if key in self.nodes:
            curr_node = self.nodes[key]
            val = curr_node.val
            self.update_frequence(curr_node)
            return val 
        else:
            return -1

    def create_entry_in_freq_dict(self, key):

        # example 
        # 2 : [head -> node1 -> node2 -> tail]

        # this tells that node1 and node2 are with frequency 2 
        # this head and tail are dummy 
        # this is doubly linked list 

        head = Node(0,0)
        tail = Node(0,0)
        head.next = tail 
        tail.prev = head
        self.freq_dict[key] = [head , tail]

    
    def remove_node_from_current_list(self, node):
        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node
        next_node.prev = prev_node
        

    
    def update_frequence(self, node):
        curr_freq = node.freq

        if curr_freq + 1 not in self.freq_dict:
            self.create_entry_in_freq_dict(curr_freq+1)

        
        self.remove_node_from_current_list(node)


        head = self.freq_dict[curr_freq+1][0]
        headNext = head.next 
        head.next = node 
        node.prev = head 
        node.next = headNext 
        headNext.prev = node 

        node.freq += 1

        if self.freq_dict[curr_freq][0].next == self.freq_dict[curr_freq][1]:
            # head.next == tail  (meaning there are no elements left with curr_freq)
            # no elements present in that freq 

            # but we need to check if this is the least freq we hold as of now or not 
            if self.curr_freq == curr_freq:

                # as we dont have any elements with current freq we need to update this even by 1 
                self.curr_freq += 1

    
    def remove_least_freq_used(self):
        tail = self.freq_dict[self.curr_freq][1]
        targetnode = tail.prev 

        prev_node = targetnode.prev 
        next_node = targetnode.next 

        prev_node.next = next_node
        next_node.prev = prev_node

        self.nodes.pop(targetnode.key)


    def put(self, key, value):

        if key not in self.nodes:
            # node not yet present - need to insert a new node  

            if self.current == self.capacity:
                # need to remove a node with less frequence 
                # if multiple nodes with same less frequence, then select the one with less recently used 

                self.remove_least_freq_used()
                self.current -= 1


            # now insert node 

            node = Node(key, value)
            node.freq = 1
            self.nodes[key] = node 

            if 1 not in self.freq_dict:

                self.create_entry_in_freq_dict(1)

            
            head = self.freq_dict[1][0]
            
            headNext = head.next 
            head.next = node 
            node.prev = head 
            node.next = headNext
            headNext.prev = node 
            self.curr_freq = 1

            self.current += 1
        
        else:
            # key is present 

            curr_node = self.nodes[key]
            curr_node.val = value
            self.update_frequence(curr_node)

