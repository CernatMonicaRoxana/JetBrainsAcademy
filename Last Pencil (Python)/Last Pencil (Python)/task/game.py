import string
import random


def validate_no_pencils():
    while True:
        try:
            pencils_no = int(input())
            if pencils_no <= 0:
                print("The number of pencils should be positive")
            else:
                return pencils_no
        except ValueError:
            print("The number of pencils should be numeric")


def validate_name():
    while True:
        name = input()
        if (name != "Jack") and (name != "John"):
            print("Choose between 'John' and 'Jack'")

        else:
            flag = True if name == 'Jack' else False
            return f"{name}'s turn!", flag


def valid_option(no, pencils_no):
    if (no not in string.digits) or (int(no) < 1 or int(no) > 3):
        print("Possible values: '1', '2' or '3'")
        return False

    if int(no) > pencils_no:
        print("Too many pencils were taken")
        return False

    return True


def bot_moves(pencils_no):
    if pencils_no % 4 == 1:
        return random.randint(1, min(3, pencils_no))
    elif pencils_no % 4 == 0:
        return 3
    elif pencils_no % 4 == 3:
        return 2
    elif pencils_no % 4 == 2:
        return 1


def game(flag, pencils_no):
    while True:
        print(pencils_no * '|')
        if flag:
            print('Jack\'s turn!')
            option = bot_moves(pencils_no)
            print(option)
            flag = False
        else:
            print('John\'s turn!')
            option = input()

            while not valid_option(option, pencils_no):
                option = input()

            flag = True

        pencils_no -= int(option)
        if pencils_no == 0:
            return "Jack won!" if flag else "John won!"


def main():
    print("How many pencils would you like to use:")

    pencils_no = validate_no_pencils()

    print("Who will be the first (John, Jack):")
    stmt, flag = validate_name()

    print(game(flag, pencils_no))


if __name__ == '__main__':
    # main()


