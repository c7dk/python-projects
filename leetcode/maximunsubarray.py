# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
nums = [5,4,-1,7,8]

def maxSubArray(nums):
    maxSum = currSum = nums[0]

    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum +nums[i])
        maxSum = max(maxSum, currSum)

    return maxSum

print(maxSubArray(nums))