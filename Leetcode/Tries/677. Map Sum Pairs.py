class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.book = {}
    
    def add(self, w: str, val: int) -> None:
        node = self.root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            
            if w in self.book:
                node.val += val - self.book[w]
            else:
                node.val += val
        
        self.book[w] = val
        node.end = True

    def sum(self, prefix: str) -> int:
        res = 0
        node = self.root
        i = 0
        while i < len(prefix) and prefix[i] in node.children:
            node = node.children[prefix[i]]
            res = node.val
            i += 1
        if i < len(prefix):
            return 0
        return res

class MapSum:
    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)