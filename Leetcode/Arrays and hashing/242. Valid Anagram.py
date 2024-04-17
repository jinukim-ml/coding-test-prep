class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        
        s_keys = sorted(s_hash.keys())
        t_keys = sorted(t_hash.keys())

        for key in s_keys:
            if key not in t_hash:
                return False
            else:
                if s_hash[key] != t_hash[key]:
                    return False
        return True
