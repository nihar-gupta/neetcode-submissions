class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False 
    
    def contains(self, ch):
        return self.links[ord(ch)-ord('a')] != None
    
    def put(self, ch, node):
        self.links[ord(ch)-ord('a')] = node
    
    def nextPointer(self, ch):
        return self.links[ord(ch)-ord('a')]
    
    def turnFlag(self):
        self.flag = True
    
    def getFlag(self):
        return self.flag

class PrefixTree:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        node = self.root 
        for wd in word:
            if not node.contains(wd):
                node.put(wd, Node())
            node = node.nextPointer(wd)
        
        node.turnFlag()



    def search(self, word: str) -> bool:
        node = self.root
        for wd in word:
            if not node.contains(wd):
                return False 
            node = node.nextPointer(wd)

        return node.getFlag()
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for wd in prefix:
            if not node.contains(wd):
                return False 
            node = node.nextPointer(wd)
        return True
        
        