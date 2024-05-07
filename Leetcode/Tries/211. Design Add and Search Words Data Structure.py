class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        idx = 0
        head = self.root
        while idx < len(word) and head.children[ord(word[idx])-97]:
            head = head.children[ord(word[idx])-97]
            idx += 1

        while idx < len(word):
            newnode = TrieNode()
            head.children[ord(word[idx])-97] = newnode
            head = head.children[ord(word[idx])-97]
            idx += 1
        head.end = True
    def search(self, word: str) -> bool:
        idx = 0
        head = self.root
        if '.' in word:
            return self.wildcard(head, word, 0)
        else:
            while idx < len(word) and head.children[ord(word[idx])-97]:
                    head = head.children[ord(word[idx])-97]
                    idx += 1
            
            if idx == len(word):
                return head.end
            else:
                return False
    
    def wildcard(self, root: TrieNode, word: str, idx: int) -> bool:
        if idx == len(word):
                return root.end
        
        if word[idx] == '.':
            for direction in range(26):
                    if root.children[direction] and self.wildcard(root.children[direction], word, idx+1):
                        return True
            return False
        else:
            while idx < len(word):
                if word[idx] == '.':
                    for direction in range(26):
                        if root.children[direction] and self.wildcard(root.children[direction], word, idx+1):
                            return True
                    return False
                
                else:
                    if root.children[ord(word[idx])-97]:
                        root = root.children[ord(word[idx]) - 97]
                        idx += 1
                    else:
                        return False

            if idx == len(word):
                return root.end
            else:
                return False