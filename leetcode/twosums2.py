# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

example1_input = [3, 3]
example1_target = 6

def twoSums(nums, target):
    ret = []
    for i, num in enumerate(nums):
        print(f"i = {i}, nums = {num}")
        for j, num2 in enumerate(nums):
            if i == j:

                added = num + num2
                print(f'j = {j}, nums = {num2}, added = {added}')
                if added == target:
                    ret.append(j)
                    print(ret)

        print('--------------------')


a = twoSums(example1_input, example1_target)
print(a)
