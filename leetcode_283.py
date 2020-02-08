# 283. Move Zeroes

def moveZeroes(nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    index = 0
    count = 0
    while True:
        if index >= len(nums):
            break
        if nums[index] == 0:
            count += 1
            nums.pop(index)
        else:
            index += 1
    for i in range(0, count):
        nums.append(0)
