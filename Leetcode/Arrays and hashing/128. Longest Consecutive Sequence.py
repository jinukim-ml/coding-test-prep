def solution(nums):
    if len(nums) == 0:
        return 0
    
    nums = sorted(set(nums))
    streak = 1
    longest_streak = 0
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            streak += 1
        else:
            longest_streak = streak if longest_streak <= streak else longest_streak
            streak = 1
    longest_streak = streak if longest_streak <= streak else longest_streak
    return longest_streak