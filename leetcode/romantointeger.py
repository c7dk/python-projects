roman_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000

}
# print(roman_numbers['X'])

example1 = "III"
example2 = "MXII"
example3 = "LVIII"
example4 = "MDCLXVI"
# Output: 3
# Explanation: III = 3.



def romanToInt(input_string):
    ret = 0
    for s in input_string:
        # print(roman_numbers[s])
        cint = roman_numbers[s]
        print(cint)
        ret = cint + ret
        print(ret)
        print('----------------')
    return ret
        
a = romanToInt(example4)
print(a)