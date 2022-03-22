# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3, 3]
target = 6

def twoSum(nums, target):
    ret = []
    for i, num in enumerate(nums):
        print(f"i = {i}, nums = {num}")
        for j, num2 in enumerate(nums):
            if i == j:
                continue

            added = num + num2
            print(f"j = {j}, j={j} num={num} num2={num2} added = {added}")
            if added == target:
                ret.append(i)
                print(ret)
            
        print('------------------')

    return ret

ret = twoSum(nums, target)
print(ret)

