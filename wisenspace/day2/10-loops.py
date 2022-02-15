# 1. for loop
"""
k = list(range(1, 4))
print(k)
"""

"""
for counter in range(1, 11):
    # print('hello')
    print(f'hello {counter}')
"""
# --------------------------
# 2. while loop

"""
sharks = 0
answer = 'y'

while answer == 'y':
    sharks = sharks + 1
    print(f'{sharks} balancing sharks')
    answer = input('Add another shark? (y/n)')
"""

# ------------------------------
# 3. infinite loops

"""
while True:
    print('This is an infinite loop!')
    answer = input('Are you bored yet? (y/n)')
    if answer =='y':
        print('How rude!')
        break
"""

# -------------------------------
#4. loop inside loop

for horray_count in range(1, 4):
    for hip_count in range(1, 3):
        print(f'Hip {hip_count}')
    print(f'Horray! {horray_count}')
