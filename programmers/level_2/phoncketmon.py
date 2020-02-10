def solution(nums):
    choice = len(nums)//2
    return min(choice, len((set(nums))))