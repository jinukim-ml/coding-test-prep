class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, path: str) -> bool:
        node = self.root
        path = path.split('/')
        i = 0
        while i < len(path) and path[i] in node.children:
            node = node.children[path[i]]
            i += 1
        if node.end:
            return True
        else:
            while i < len(path):
                newnode = TrieNode()
                node.children[path[i]] = newnode
                node = newnode
                i += 1
            node.end = True
            return False

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        trie = Trie()
        ans = []
        for path in folder:
            if trie.insert(path):
                continue
            else:
                ans.append(path)
        return ans