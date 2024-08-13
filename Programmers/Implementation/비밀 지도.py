def solution(n, arr1, arr2):
    ans = []
    
    for i in range(n):
        b1 = bin(arr1[i])[2:]
        b2 = bin(arr2[i])[2:]
        
        b1 = '0' * (n - len(b1)) + b1
        b2 = '0' * (n - len(b2)) + b2
        s = ''
        for j in range(n):
            if b1[j]  == '1' or b2[j] == '1':
                s += '#'
            elif b1[j] == '0' and b2[j] == '0':
                s += ' '
        ans.append(s)
    return ans