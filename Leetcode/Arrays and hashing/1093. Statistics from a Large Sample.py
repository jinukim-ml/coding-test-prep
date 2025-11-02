class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        num_samples = sum(count)
        def get_median_odd() -> int:
            freq = 0
            for i in range(256):
                freq += count[i]
                if freq >= num_samples//2+1:
                    return i
        def get_median_even() -> int:
            prev, freq = -1, 0
            half = num_samples//2
            for i in range(256):
                freq += count[i]
                if freq < half:
                    continue
                elif freq == half:
                    if count[i]:
                        prev = i
                else:
                    if prev == -1:
                        return i
                    else:
                        return (prev+i)/2
        if num_samples%2:
            median = get_median_odd()
        else:
            median = get_median_even()
        
        minimum = 256
        for i in range(256):
            if count[i]:
                minimum = i
                break
        
        maximum = 0
        for i in reversed(range(256)):
            if count[i]:
                maximum = i
                break
        
        mean, mode = 0, 256
        freq = 0
        for i in range(256):
            mean += i * count[i]
            if count[i] > freq:
                freq = count[i]
                mode = i
        mean /= num_samples
        return [minimum, maximum, mean, median, mode]