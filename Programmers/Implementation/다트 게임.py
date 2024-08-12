def solution(dartResult):
    l = 0
    options = set(['#', '*'])
    ans = []
    while l < len(dartResult):
        score = int(dartResult[l])
        if dartResult[l+1] == '0':
            score *= 10
            l += 1
        l += 1
        
        if dartResult[l] == 'D':
            score **= 2
        elif dartResult[l] == 'T':
            score **= 3
        l += 1
        
        if l < len(dartResult) and dartResult[l] in options:
            if dartResult[l] == '*':
                if ans:
                    ans[-1] *= 2
                score *= 2
            else:
                score *= -1
            l += 1
        ans.append(score)
                
    return sum(ans)