class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) > 12:
            return []
        res = []
        def is_valid(ip: str) -> bool:
            for i, digits in enumerate(ip.split('.')):
                if len(digits) > 1 and digits[0] == '0':
                    return False
                if int(digits) > 255:
                    return False
            return True
            
        def backtrack(i: int, dots: int, ip: str) -> None:
            print(i, ip)
            if dots == 4:
                return
            if i == len(s):
                print(f'sending ip: {ip}')
                if dots == 3 and is_valid(ip):
                    res.append(ip)
                return
            if not 4-dots <= len(s)-i <= (4-dots)*3:
                return
            backtrack(i+1, dots+1, ip + s[i] + '.')
            backtrack(i+1, dots, ip + s[i])

        backtrack(0, 0, '')
        return res