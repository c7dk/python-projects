import random
import string

def pick_random_adjective():
    adjectives = [
        'sleepy', 'slow', 'smelly', 'wet', 'fat', 'red',
        'orange', 'yellow', 'green',
        'blue', 'purple', 'fluffy',
        'white', 'proud', 'brave']
    ret = random.choice(adjectives)
    return ret

def pick_random_noun():
    nouns = [
        'apple', 'dinosaur', 'ball',
        'toaster', 'goat', 'dragon',
        'hammer', 'duck', 'panda']
    ret = random.choice(nouns)
    return ret

def pick_random_number():
    return random.randint(0, 100)

def pick_random_punctuation():
    ret = random.choice(string.punctuation)
    return ret

def combine(adj, noun, number, punc):
    return adj + noun + str(number) + punc

def make_password():
    adj = pick_random_adjective()
    noun = pick_random_noun()
    number = pick_random_number()
    punc = pick_random_punctuation()

    password = combine(adj, noun, number, punc)
    print(f'created password: {password}')

def main():
    while True:
        make_password()
        cont = input("Want another password? ")
        if(cont != "yes" and cont != 'y'):
            break

if __name__ == "__main__":
    # execute only if run as a script
    main()
