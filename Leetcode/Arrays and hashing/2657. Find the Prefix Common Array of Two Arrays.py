class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        C = [0] * len(A)
        seen_A = set()
        seen_B = set()
        for i in range(len(A)):
            C[i] = C[i-1]
            if A[i] == B[i]:
                C[i] += 1
            else:
                if A[i] in seen_B:
                    C[i] += 1
                if B[i] in seen_A:
                    C[i] += 1
            seen_A.add(A[i])
            seen_B.add(B[i])
        return C