# First Solution
def solution(nums):
    answer, half = len(set(nums)), len(nums) // 2
    return half if answer > half else answer


# Second Solution
def solution(nums):
    return min(len(nums) // 2, len(set(nums)))