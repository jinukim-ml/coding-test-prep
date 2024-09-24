class TrieNode:
    def __init__(self):
        self.children = [None] * 10
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        idx = 0
        node = self.root
        while idx < len(word) and node.children[int(word[idx])]:
            node = node.children[int(word[idx])]
            idx += 1
        
        while idx < len(word):
            pos = int(word[idx])
            node.children[pos] = TrieNode()
            node = node.children[pos]
            idx += 1
        node.end = True

    def search(self, word: str) -> int:
        idx = 0
        node = self.root

        res = 0
        while idx < len(word) and node.children[int(word[idx])]:
            node = node.children[int(word[idx])]
            idx += 1
            res += 1
        return res

class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        trie = Trie()
        for w in arr1:
            trie.insert(str(w))
        
        ans = 0
        for w in arr2:
            length = trie.search(str(w))
            ans = max(ans, length)
        return ans
    
    def get_prefix(self, n1: int, n2: int) -> str:
        n1, n2 = str(n1), str(n2)

        res = ''
        for i in range(min(len(n1), len(n2))):
            if n1[i] != n2[i]:
                break
            else:
                res += n1[i]
        return res