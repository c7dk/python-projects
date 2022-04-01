# num1 = "11"
# num2 = "123"
# num1 = "456"
# num2 = "77"
num1 = "0"
num2 = "0"

def addStrings(num1, num2):
    i = len(num1) -1
    j = len(num2) -1
    carry = 0
    ret = ''

    while i >=0 or j >=0 or carry > 0:
        carry += int(num1[i]) if i >= 0 else 0
        carry += int(num2[j]) if j >= 0 else 0

        ret = str(carry % 10) + ret
        carry = carry // 10
        i -= 1
        j -= 1

    return ret

print(addStrings(num1, num2))