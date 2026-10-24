class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 0

class FreqStack:

    def __init__(self):
        
        self.freq_dict = dict()
        self.nodes_dict = dict()
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        if val not in self.nodes_dict:

            newnode = Node(val)
            newnode.freq = 1

            if 1 not in self.freq_dict:
                self.create_key_in_freq_dict(1)
            
            self.insert_node_in_freq_dict(1, newnode)
            self.nodes_dict[val] = [newnode]
            self.max_freq = max(self.max_freq, 1)
        else:
            
            previous_node = self.nodes_dict[val][-1]
            previous_freq = previous_node.freq

            newnode = Node(val)
            newnode.freq = previous_freq + 1

            if previous_freq+1 not in self.freq_dict:
                self.create_key_in_freq_dict(previous_freq+1)
            
            self.insert_node_in_freq_dict(previous_freq+1, newnode)
            self.nodes_dict[val].append(newnode)
            self.max_freq = max(self.max_freq, previous_freq+1)

            

    def pop(self) -> int:
        curr_max_freq = self.max_freq
        rt_node = self.get_recent_node_with_freq(curr_max_freq)
        rt_val = rt_node.val
        self.nodes_dict[rt_val].pop()
        if len(self.nodes_dict[rt_val]) == 0:
            self.nodes_dict.pop(rt_val)
        return rt_val


    


    def get_recent_node_with_freq(self, freq):
        tail = self.freq_dict[freq][1]
        
        targetnode = tail.prev

        prevnode = targetnode.prev
        prevnode.next = tail
        tail.prev = prevnode

        head = self.freq_dict[freq][0]
        tail = self.freq_dict[freq][1]
        if head.next == tail:
            if self.max_freq == freq:
                self.max_freq -= 1
        


        return targetnode





    def create_key_in_freq_dict(self, key):
        head = Node(0)
        tail = Node(0)
        head.next = tail
        tail.prev = head 
        self.freq_dict[key] = [head, tail]
    
    def insert_node_in_freq_dict(self, key, node):
        tail = self.freq_dict[key][1]
        
        tailprev = tail.prev
        tailprev.next = node 
        node.prev = tailprev
        node.next = tail
        tail.prev = node


        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()