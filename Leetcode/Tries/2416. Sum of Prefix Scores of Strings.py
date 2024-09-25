class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, w: str) -> None:
        node = self.root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = [TrieNode(), 1]
            else:
                node.children[ch][1] += 1
            node = node.children[ch][0]
    
    def search(self, w: str) -> int:
        node = self.root
        res = 0
        for ch in w:
            if ch in node.children:
                res += node.children[ch][1]
                node = node.children[ch][0]
            else:
                break
        return res

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()

        for w in words:
            trie.add(w)
        
        ans = []
        for w in words:
            ans.append(trie.search(w))
        return ans