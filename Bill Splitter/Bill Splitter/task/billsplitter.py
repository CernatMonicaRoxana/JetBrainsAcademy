# write your code here
import math
import random


def main():
    print("Enter the number of friends joining (including you):")

    friends = int(input())

    if friends <= 0:
        print("No one is joining for the party")

    else:
        diction = {}

        print("Enter the name of every friend (including you), each on a new line:")
        for i in range(0, friends):
            friend = input()
            diction[friend] = 0

        print("Enter  the total bill value:")
        bill = int(input())

        split_bill = bill / friends
        split_bill = math.ceil(split_bill) if split_bill % 10 == 0 else round(split_bill, 2)

        for j in diction:
            diction[j] = split_bill

        print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
        lucky = input()
        if lucky == "No":
            print("No one is going to be lucky")
        elif lucky == "Yes":
            ind = random.randint(0, friends - 1)
            lucky_one = list(diction.keys())[ind]
            print(f"{lucky_one} id the lucky one!")

            split_bill = round(bill / (friends - 1), 2)
            for j in diction:
                if j == lucky_one:
                    diction[j] = 0
                else:
                    diction[j] = split_bill

        print(diction)


if __name__ == '__main__':
    main()
