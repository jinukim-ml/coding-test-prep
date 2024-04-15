'''
Solution for https://school.programmers.co.kr/learn/courses/30/lessons/84512
Type: Exhaustive search
'''
def solution(word):
    chrs = ['A', 'E', 'I', 'O', 'U']
    s = ['A']
    nums = [0, -1, -1, -1, -1]
    last_idx = 0
    answer = 1

    # Last character is U -> pop
    while ''.join(s) != word:
        if len(s) < 5:
            s.append('A')
            last_idx += 1 # Last character pointer
            nums[last_idx] += 1 # numerical last character
        elif s[last_idx] == 'U':
            while s[last_idx] == 'U':
                s.pop()
                nums[last_idx] = -1 # Reset last character
                last_idx -= 1
            nums[last_idx] += 1
            s[-1] = chrs[nums[last_idx]]
        else:
            nums[last_idx] += 1
            s[-1] = chrs[nums[last_idx]]
        answer += 1
    return answer