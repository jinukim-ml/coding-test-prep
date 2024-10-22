# 뉴스 클러스터링 https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import Counter

def solution(str1:str, str2:str) -> int:
    str1 = str1.lower()
    str2 = str2.lower()
    a, b = [], []
    
    for r in range(1, len(str1)):
        s:str = str1[r-1:r+1]
        if s.isalpha() and len(s) == 2:
            a.append(s)
    
    for r in range(1, len(str2)):
        s:str = str2[r-1:r+1]
        if s.isalpha() and len(s) == 2:
            b.append(s)
    cnt_a, cnt_b = Counter(a), Counter(b)
    intersection, union = 0, 0
    
    for k, v in cnt_a.items():
        if k in cnt_b:
            intersection += min(v, cnt_b[k])
            union += max(v, cnt_b[k])
            cnt_b.pop(k)
        else:
            union += v
    for k, v in cnt_b.items():
        union += v
        
    if intersection == 0 and union == 0:
        jaccard = 1
    else:
        jaccard = intersection / union
    return int(jaccard * 65536)