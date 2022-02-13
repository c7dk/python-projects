# 4. if ~ elif ~ else

weather = 'rain'

if weather == 'rain':
    print('Remember to bring your umbrella!')
elif weather == 'snow':
    print('Remeber to stay warm when its snowy!')
else:
    print('Remember to bring your sunglasses on this sunny day!')

# -----------------

# 5. reverse condition
# not True => False

#------------------
# 6. combining conditions

age = input('Please enter your age: ')
height = input('Please enter how tall you currently are (please use a whole number): ')

age = int(age)
height = int(height)

if (age > 10) and (height > 45):
    print( 'You can ride this rollercoaster')
else:
    print('I am very sorry to inform you that you are not currently allowed to ride this rollercoaster')

#------------------
# 7.

weather = 'rainy'
number_of_hw = 10

if weather == 'nice' and number_of_hw < 3:
    print('Go outside and play for a long time')
elif weather == 'nice' and number_of_hw < 7:
    print('Go outside and play for a little while')
elif weather == 'rainy' and number_of_hw < 9:
    print('Stay inside and go work on your homework')
else:
    print('Rest at home')
