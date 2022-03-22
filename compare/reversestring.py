s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]
# Output: ["o","l","l","e","h"]

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """

# s1.reverse()
# s2.reverse()

# print('Reversed List: ', s2)

# two pointers
l = 0
r = len(s1) - 1

while l<r:
    s1[l], s1[r] = s1[r], s1[l]
    l += 1
    r -= 1
    # print(s1)

print(s1)