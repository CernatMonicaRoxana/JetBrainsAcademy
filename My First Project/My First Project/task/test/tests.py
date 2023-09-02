from hstest import StageTest, TestedProgram, CheckResult, dynamic_test


# Bubblegum: $202.0
# Toffee: $118.0
# Ice cream: $2250.0
# Milk chocolate: $1680.0
# Doughnut: $1075.0
# Pancake: $80.0
#
# Income: $5405.0
# Staff expenses: $4170
# Other expenses: $220
# Net income: $1015


class PrintFirstProject(StageTest):
    @dynamic_test()
    def test_first_project(self):
        pr = TestedProgram()
        output = pr.start().lower().strip()
        output_length = len(list(filter(None, output.splitlines())))
        if not output:
            return CheckResult.wrong("Your program didn't print any output.")
        elif '>' in output:
            return CheckResult.wrong("The greater-than symbol followed by a space (> ) represents the user input "
                                     "in examples. It's not part of the input and you shouldn’t print this sign")
        elif output_length != 9:
            return CheckResult.wrong(f'Your program should output 9 lines before taking user input:\n'
                                     f'the earned amount for each item, income, and the "Staff expenses" line.\n'
                                     f'{output_length} lines were found.')

        if 'earned' not in output.lower():
            return CheckResult.wrong("Your program didn't print the 'Earned amount' line")
        elif 'bubblegum' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Bubblegum' as an item")
        elif 'toffee' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Toffee' as an item")
        elif 'ice cream' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Ice Cream' as an item")
        elif 'milk chocolate' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Milk chocolate' as an item")
        elif 'doughnut' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Doughnut' as an item")
        elif 'pancake' not in output.lower():
            return CheckResult.wrong("Your program should print the 'Pancake' as an item")
        elif 'income' not in output.lower():
            return CheckResult.wrong("Your program should print the income on a separate line")
        elif 'staff expenses' not in output:
            return CheckResult.wrong("Your program should ask the user for input with the 'Staff expenses' line")
        elif '202' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Bubblegum.")
        elif '118' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Toffee.")
        elif '2250' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Ice Cream.")
        elif '1680' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Milk chocolate.")
        elif '1075' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Doughnut.")
        elif '80' not in output.lower():
            return CheckResult.wrong("Incorrect earned amount for Pancake.")
        elif '5405' not in output.lower():
            return CheckResult.wrong("Incorrect total income! Make sure you didn’t print the total income value from"
                                     " the examples, calculate it based on the earnings mentioned in previous stage.")
        if not pr.is_waiting_input():
            return CheckResult.wrong('Your program should ask the user to input the staff expenses')
        output1 = pr.execute('4170').lower().strip()
        if 'other expenses' not in output1:
            return CheckResult.wrong("Your program should ask the user for input with the 'Other expenses' line")
        if not pr.is_waiting_input():
            return CheckResult.wrong('Your program should ask the user to input other expenses')
        output2 = pr.execute('220').lower().strip()
        if 'net income' not in output2:
            return CheckResult.wrong("Your program should print the net income on a separate line")
        elif '1015' not in output2.lower():
            return CheckResult.wrong(
                "Incorrect net income! Make sure you didn’t print the net income value from the examples"
                ", calculate it by subtracting expenses provided in the input from the total income")
        else:
            return CheckResult.correct()


if __name__ == '__main__':
    PrintFirstProject().run_tests()
