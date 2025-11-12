from collections import defaultdict

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        info = defaultdict(lambda: '?')
        for k, v in knowledge:
            info[f'({k})'] = v
        res, subarr = [], []
        for ch in s:
            entry = ''
            if ch == '(':
                subarr.append(ch)
            elif subarr:
                subarr.append(ch)
                if subarr[-1] == ')':
                    key = ''.join(subarr)
                    entry = info[key]
                    subarr = []
            else:
                entry = ch
            res.append(entry)
        return ''.join(res)