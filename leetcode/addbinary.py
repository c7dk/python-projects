# a = "11"
# b = "1"
a = "1010"
b = "1011"

def addBinary(a, b):
    i = len(a) -1
    j = len(b) -1
    carry = 0
    ret = ''

    while i >=0 or j >=0 or carry > 0:
        carry += int(a[i]) if i >= 0 else 0
        carry += int(b[j]) if j >= 0 else 0

        ret = str(carry % 2) + ret
        carry = carry // 2
        i -= 1
        j -= 1

    return ret

print(addBinary(a, b))