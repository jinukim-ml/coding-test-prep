from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_cnt = [0]*26
        strs_num = []
        for i in range(len(strs)):
            word_cnt = [0] * 26
            for character in strs[i]:
                word_cnt[ord(character)-97] += 1
            strs_num.append(word_cnt)

        answer = []
        used_idx = []
        for i in range(len(strs_num)):
            pivot = strs_num[i]
            
            if i in used_idx:
                continue
            else:
                group = [strs[i]]

            for j in range(i+1, len(strs_num)):
                if pivot == strs_num[j]:
                    group.append(strs[j])
                    used_idx.append(j)
            if group:
                answer.append(group)
        return answer