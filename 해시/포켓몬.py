def solution(nums):
    answer, half = len(set(nums)), len(nums) // 2
    return half if answer > half else answer