class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        idx = 0
        start = self.root
        while idx < len(word) and start.children[ord(word[idx])-97]:
            start = start.children[ord(word[idx])-97]
            idx += 1

        while idx < len(word):
            node = TrieNode()
            start.children[ord(word[idx])-97] = node
            # if start.end:
            #     start.end = False
            start = start.children[ord(word[idx])-97]
            idx += 1
        start.end = True

    def search(self, word: str) -> bool:
        idx = 0
        head = self.root
        while idx < len(word) and head.children[ord(word[idx])-97]:
            head = head.children[ord(word[idx])-97]
            idx += 1
        if len(word) == idx and head.end == True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        idx = 0
        head = self.root

        while idx < len(prefix) and head.children[ord(prefix[idx])-97]:
            head = head.children[ord(prefix[idx])-97]
            idx += 1
        
        if len(prefix) == idx:
            return True
        else:
            return False