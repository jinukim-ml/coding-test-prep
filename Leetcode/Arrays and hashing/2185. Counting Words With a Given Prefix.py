class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0
        for w in words:
            i = 0
            while i < min(len(pref), len(w)) and pref[i] == w[i]:
                i += 1
            if i == len(pref):
                res += 1
        return res

# Trie solution
from collections import defaultdict

class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.cnt = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
                node.cnt += 1
            else:
                newnode = TrieNode()
                node.children[ch] = newnode
                node = node.children[ch]
                node.cnt += 1
    
    def count(self, word: str) -> int:
        node = self.root
        for ch in word:
            node = node.children[ch]
        return node.cnt
    
class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        return trie.count(pref)