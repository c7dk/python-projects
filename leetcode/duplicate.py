# nums = [1,2,3,1] #True
# nums = [1,1,1,3,3,4,3,2,4,2] #True
nums = [1,2,3,4] #False

# nums.sort()
# print(nums)

# def duplicate(nums):
#     for i in range(len(nums)-1):
#         # print(i)
#         # print(nums[i])
#         if nums[i] == nums[i+1]:
#             # print(i)
#             return True
#     return False

# print(duplicate(nums))

# -----------------------------
#dictionary

def duplicate(nums):
    dict = {nums[0]:1}

    for i in range (1, len(nums)):
        if nums[i] in dict:
            return True
        else:
            dict[nums[i]] = 1

    return False

print(duplicate(nums))