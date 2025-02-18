class Solution:
    def smallestNumber(self, pattern: str) -> str:
        target_len = len(pattern) + 1
        seen = set()
        arr = []
        def backtrack(i: int) -> bool:
            if len(arr) == target_len:
                return True
            
            if pattern[i-1] == 'I':
                for n in range(arr[i-1]+1, 10):
                    if n not in seen:
                        arr.append(n)
                        seen.add(n)
                        if backtrack(i+1):
                            return True
                        arr.pop()
                        seen.remove(n)
            else:
                for n in range(1, arr[i-1]):
                    if n not in seen:
                        arr.append(n)
                        seen.add(n)
                        if backtrack(i+1):
                            return True
                        arr.pop()
                        seen.remove(n)
            return False
        for n in range(1, 10):
            arr.append(n)
            seen.add(n)
            if backtrack(1):
                break
            arr.pop()
            seen.remove(n)
        
        res = ''
        for n in arr:
            res += str(n)
        return res