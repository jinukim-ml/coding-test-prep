class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # every character in t is included in the window
        # minimum window substring
        if len(s) < len(t):
            return ""
        
        minlen = float('inf')

        tab_s, tab_t = {}, {}
        for i in range(len(t)):
            tab_t[t[i]] = tab_t.get(t[i], 0) + 1
        need = len(tab_t)

        l, have = 0, 0
        indices = [-1, -1]
        for r in range(len(s)):
            tab_s[s[r]] = tab_s.get(s[r], 0) + 1
            if s[r] in tab_t and tab_s[s[r]] == tab_t[s[r]]:    
                have += 1

            while have == need:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    indices = [l, r]

                tab_s[s[l]] -= 1
                if s[l] in tab_t and tab_s[s[l]] < tab_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = indices
        if minlen == float('inf'):
            return ""
        else:
            return s[l:r+1]