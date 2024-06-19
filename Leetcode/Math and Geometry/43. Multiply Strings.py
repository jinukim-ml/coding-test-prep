class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for i in range(len(num1)):
            n1 += (ord(num1[len(num1)-i-1]) - 48) * 10**i

        n2 = 0
        for i in range(len(num2)):
            n2 += (ord(num2[len(num2)-i-1]) - 48) * 10**i
        
        return str(n1 * n2)