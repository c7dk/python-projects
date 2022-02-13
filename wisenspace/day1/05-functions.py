# how to use fuctions

# 1. function with one argument
print('Hello, World!')

# 2. function with 3 argument and 1 return value
val = min(12, 24, 1000)
print(val)

val = max(2, 3, 5, 9)
print(val)

# 3. function is called from a string and returned new value
hw = 'Hello, World!'.upper()
print(hw)

# -------------

# how to make functions

# 1. making function with no argument and no return value
def print_seconds_per_day():
    hours = 24
    minutes = hours * 60
    seconds = minutes * 60
    print(seconds)

print_seconds_per_day()

# 2. making function with one argument and returen 1 value
def upper(str):
    return str.upper()
    
ret = upper('unicorn')
print(ret)

# 3. function with 2 arguments and no return value
def add(number1, number2):
    print(number1 + number2)
add(2, 3)

# 4. functin with 2 arguments and 1 return value
def add2(number1, number2):
    return number1 + number2

val = add2(2, 3)
print(val)