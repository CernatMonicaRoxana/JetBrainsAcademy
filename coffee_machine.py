class CoffeeMachine:

    def __init__(self):
        self.water_av = 400
        self.milk_av = 540
        self.coffee_av = 120
        self.cups_av = 9
        self.money = 550
        self.state = "choosing an action"

    def user(self, input_str):
        if self.state == "choosing an action":
            if input_str == "remaining":
                self.remaining()

            elif input_str == "buy":
                self.state = "choosing a type of coffee"

            elif input_str == "fill":
                self.state = "fill water"

            elif input_str == "take":
                self.take()

            elif input_str == "exit":
                exit()

        elif self.state == "choosing a type of coffee":
            if input_str == "1":
                self.buy_espresso()
                self.state = "choosing an action"

            elif input_str == "2":
                self.buy_latte()
                self.state = "choosing an action"

            elif input_str == "3":
                self.buy_cappuccino()
                self.state = "choosing an action"

            elif input_str == "back":
                self.state = "choosing an action"

        elif self.state == "fill water":
            self.fill_water(input_str)
            self.state = "fill milk"
        elif self.state == "fill milk":
            self.fill_milk(input_str)
            self.state = "fill coffee"
        elif self.state == "fill coffee":
            self.fill_coffee(input_str)
            self.state = "fill cups"
        elif self.state == "fill cups":
            self.fill_cups(input_str)
            self.state = "choosing an action"

    def remaining(self):
        print("The coffee machine has:")
        print(str(self.water_av) + " of water")
        print(str(self.milk_av) + " of milk")
        print(str(self.coffee_av) + " of coffee beans")
        print(str(self.cups_av) + " of disposable cups")
        print("$" + str(self.money) + " of money")

    def buy_espresso(self):
        if self.water_av >= 250 and self.milk_av >= 16 and self.coffee_av >= 16 and self.cups_av >= 1:
            print("I have enough resources, making you a coffee!\n")
            self.water_av -= 250
            self.coffee_av -= 16
            self.cups_av -= 1
            self.money += 4
        elif self.water_av < 250:
            print("Sorry, not enough water!\n")
        elif self.milk_av < 16:
            print("Sorry, not enough milk!\n")
        elif self.coffee_av < 16:
            print("Sorry, not enough coffee beans!\n")
        elif self.cups_av < 1:
            print("Sorry, not enough disposable cups!\n")

    def buy_latte(self):
        if self.water_av >= 350 and self.milk_av >= 75 and self.coffee_av >= 20 and self.cups_av >= 1:
            print("I have enough resources, making you a coffee!\n")
            self.water_av -= 350
            self.milk_av -= 75
            self.coffee_av -= 20
            self.cups_av -= 1
            self.money += 7
        elif self.water_av < 350:
            print("Sorry, not enough water!\n")
        elif self.milk_av < 75:
            print("Sorry, not enough milk!\n")
        elif self.coffee_av < 20:
            print("Sorry, not enough coffee beans!\n")
        elif self.cups_av < 1:
            print("Sorry, not enough disposable cups!\n")

    def buy_cappuccino(self):
        if self.water_av >= 200 and self.milk_av >= 100 and self.coffee_av >= 12 and self.cups_av >= 1:
            print("I have enough resources, making you a coffee!\n")
            self.water_av -= 200
            self.milk_av -= 100
            self.coffee_av -= 12
            self.cups_av -= 1
            self.money += 6
        elif self.water_av < 200:
            print("Sorry, not enough water!\n")
        elif self.milk_av < 100:
            print("Sorry, not enough milk!\n")
        elif self.coffee_av < 12:
            print("Sorry, not enough coffee beans!\n")
        elif self.cups_av < 1:
            print("Sorry, not enough disposable cups!\n")

    def fill_water(self, water_in):
        self.water_av += int(water_in)

    def fill_milk(self, milk_in):
        self.milk_av += int(milk_in)

    def fill_coffee(self, coffee_in):
        self.coffee_av += int(coffee_in)

    def fill_cups(self, cups_in):
        self.cups_av += int(cups_in)

    def take(self):
        print("I gave you $" + str(self.money) + "\n")
        self.money = 0


coffee = CoffeeMachine()
while True:
    coffee.user(input())
