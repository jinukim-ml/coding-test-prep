from collections import defaultdict

class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        balls = defaultdict(int)
        color_freq = defaultdict(int)
        unique_colors = set()
        res = []
        for b, c in queries:
            prev_color = balls[b]
            if prev_color != 0:
                color_freq[prev_color] -= 1
                if color_freq[prev_color] == 0:
                    unique_colors.discard(prev_color)
            balls[b] = c
            color_freq[c] += 1
            if color_freq[c] == 1:
                unique_colors.add(c)
            res.append(len(unique_colors))
        return res