class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        size = len(s)//k
        s_map = {}
        t_map = {}
        s_key = ''
        t_key = ''
        for curr in range(len(s)):
            s_key += s[curr]
            t_key += t[curr]
            if len(s_key) == size:
                s_map[s_key] = s_map.get(s_key, 0) + 1
                t_map[t_key] = t_map.get(t_key, 0) + 1
                s_key = ''
                t_key = ''

        for key, val in s_map.items():
            if key not in t_map:
                return False
            elif val != t_map[key]:
                return False
        return True