hand1 = input("Please ender your hand: ")

hand2 = int(hand1)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

targetnum = 21

offnum = targetnum - hand2

count = 0

for card in cards:
    if card <= offnum:
        count += 1

probability = count/len(cards) * 100
print(probability)

if probability == 100:
    print('Completly safe')
elif probability >= 75:
    print('Safe')
elif probability >= 50:
    print('Somewhat risky')
elif probability >= 25:
    print('Risky')
elif probability >= 1:
    print('Very risky')
elif probability == 0:
    print('No chance')