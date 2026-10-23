# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        
class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity
        self.dictionary = dict()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dictionary:
            presentNode = self.dictionary[key]
            returnValue = presentNode.value
            self.change_to_recently_used(presentNode)
            return returnValue
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # case 1: if key already present
        if key in self.dictionary:
            presentNode = self.dictionary[key]
            presentNode.value = value
            self.change_to_recently_used(presentNode)
        else:
            # case 2: if it is not full of capacity
            if len(self.dictionary) < self.capacity:
                self.add_new_node(key, value)
            else:
                # delete least used node
                self.delete_least_used_node()
                self.add_new_node(key, value)

    def change_to_recently_used(self, presentNode):
        previousNode = presentNode.prev
        nextNode = presentNode.next

        # remove from its postition
        previousNode.next = nextNode
        nextNode.prev = previousNode

        # add next to head
        headNext = self.head.next
        self.head.next = presentNode
        presentNode.prev = self.head
        presentNode.next = headNext
        headNext.prev = presentNode

    def add_new_node(self, key, value):
        newNode = Node(key, value)

        headNext = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = headNext
        headNext.prev = newNode

        # update the dictionary
        self.dictionary[key] = newNode

    def delete_least_used_node(self):
        targetNode = self.tail.prev

        prevNode = targetNode.prev
        nextNode = targetNode.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        # remove reference from dictionary
        self.dictionary.pop(targetNode.key)
