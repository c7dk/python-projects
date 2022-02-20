def maxChars(inp):
    charmap = {}

    # make chamap

    for e in inp:
        # print(e)

        if e in charmap:
            charmap[e] += 1
        else:
            charmap[e] = 1
        # print(charmap)

    # find max count and max char

    maxCnt = 0
    maxChar = ''
    for key, val in charmap.items():
        if val > maxCnt:
            maxCnt = val
            maxChar = key

    return maxChar

ret = maxChars('abcccccd')
print(ret) 

ret = maxChars('apple 123111111')
print(ret)
