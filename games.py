import random


def randomly_generate():
    """
    Randomly generates a 4-digit number (with unique digits).
    hello
    """
    k = random.randrange(1023, 9999)
    k = set(str(k))
    while len(k) < 4:
        k = random.randrange(1023, 9999)
        k = set(str(k))
    else:
        k = "".join(k)
        return k
    # list_1 = []
    # for i in range(1000, 9999):
    #     list_1.append(i)
    #     k = 0
    #     for j in str(i):
    #         if str(i).count(j) > 1:
    #             k += 1
    #             if k == 1:
    #                 list_1.remove(i)
    # return str(random.choice(list_1))


def user_num(user: str) -> bool:
    """
    check there are duplicate digits in the given number
    """
    for i in user:
        while user.count(i) > 1:
            return False
    return True


def cows_and_bulls(user, rend_num):
    """
    For every digit that the user guessed correctly in the correct place,
    they have a “cow”.
    For every digit the user guessed correctly in the wrong place is a “bull.”
    Every time the user makes a guess,
    tell them how many “cows” and “bulls” they have.
    Once the user guesses the correct number, the game is over.
    """
    guesses = 0
    while user != rend_num:
        print(rend_num)
        cow = 0
        bull = 0
        for i in user:
            if i in rend_num:
                for k in rend_num:
                    if (i == k) and (user.index(i) == rend_num.index(k)):
                        cow += 1
                        guesses += 1
                    elif (i == k) and (user.index(i) != rend_num.index(k)):
                        bull += 1
                        guesses += 1
                    else:
                        continue
            else:
                continue
        user = input(f"cow-{cow}--bull-{bull}----{user} guess a 4-digit number **** -")
        if user_num(user) and len(user) == 4:
            continue
        else:
            print("There are duplicate digits in the number")
    else:
        print("congratulations you guessed the number ", rend_num, "guesses made by the user-", guesses)


rend_num_1 = randomly_generate()
user_1 = input("number\n")
cows_and_bulls(user_1, rend_num_1)
