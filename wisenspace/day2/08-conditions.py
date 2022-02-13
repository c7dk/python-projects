# 1. Boolean values
answer_one = True
answer_two = False

10 == 10 # True
10 == 11 # False
10 != 10 # False
10 != 11 # True

'Hello' == 'Hello' # True
'Hello' == 'Good bye' # False
'Good bye' != 'Hello' # True
42 == '42' # False

# -------------------

# 2. equal signs
age = 10

if age == 10:
    print('You are currently 10 years old')

# -------------------

#3. Logical Operators

age = input('Please enter how old you are: ')
age = int(age)

if age != 10:
    print('You are not currently 10 years old')

if age > 10:
    print('You are currently older than 10 years old')

if age < 10:
    print('You are currently younger than 10 years old')

