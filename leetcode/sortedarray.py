# nums = [-4,-1,0,3,10]
nums = [-7,-3,2,3,11]

def sortedSquares(nums):
    # two pointers
    l = 0
    r = len(nums) - 1

    ret = [0] * len(nums) 
    k = len(ret) - 1

    while l<=r:
        if abs(nums[l]) < abs(nums[r]):
            ret[k] = nums[r] * nums[r]
            r -= 1

        else: 
            ret[k] = nums[l] * nums[l]
            l += 1

        k -= 1
    
    return ret

print(sortedSquares(nums))