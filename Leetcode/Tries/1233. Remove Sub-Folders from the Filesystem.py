from collections import defaultdict

# Trie solution
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(str)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, path: str) -> bool:
        curr = self.root
        path = path.split('/')
        for p in path:
            if p == '':
                continue
            if curr.end:
                return False
            else:
                if p in curr.nodes:
                    curr = curr.nodes[p]
                else:
                    curr.nodes[p] = TrieNode()
                    curr = curr.nodes[p]
        curr.end = True
        return True

class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        trie = Trie()
        folder.sort()
        res = []
        for path in folder:
            if trie.add(path):
                res.append(path)
        return res

# String solution
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = []
        for p in folder:
            if not res or not p.startswith(res[-1] + '/'):
                res.append(p)
        return res