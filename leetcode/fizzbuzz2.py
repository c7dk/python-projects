number = input("Please type a number for FizzBuzz: ")
nums2 = int(number)


for num in range(1, nums2 + 1):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
    else:
        print(num)

        