from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 1. can we make a word strating from i?
        # 2. if so, when does the word end? Let's say it ends on index j.
        # 3. search again starting from index j+1
        ans = []
        def backtrack(i, sentence):
            if i == len(s):
                ans.append(sentence)
                return

            for word in wordDict:
                if word == s[i:i+len(word)]:
                    if sentence == "":
                        backtrack(i+len(word), word)
                    else:
                        backtrack(i+len(word), sentence + " " + word)
        
        backtrack(0, "")
        return ans