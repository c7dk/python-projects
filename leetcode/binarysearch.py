# nums = [-1, 0, 3, 5, 9, 12]
# target = 9
nums = [-1, 0, 3, 5, 9, 12]
target = 2

def search(nums, target):
    left = 0
    right = len(nums) - 1

    if (target > nums[-1]) or (target < nums[0]): return -1

    while left <= right:
        pivot = (left + right) // 2

        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            left = pivot + 1
        elif nums[pivot] > target:
            right = pivot - 1
    
    return -1

print(search(nums, target))