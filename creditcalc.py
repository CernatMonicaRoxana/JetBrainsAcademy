import math
import argparse


def annuity_count_of_months(credit_prin, monthly_payments, interest):
    n = annuity_count_of_periods(interest, monthly_payments, credit_prin)
    no = ''
    if n % 12 == 0:
        no_years = n // 12
        if no_years > 1:
            no =  "It will take {} years to repay this loan!".format(no_years)
        elif no_years == 1:
            no =  "It will take 1 year to repay this loan!"

    else:
        no_years = n // 12
        no_months = n % 12
        if no_months > 1 and no_years > 1:
            no = "It will take {} years and {} months to repay this loan!".format(no_years, no_months)
        elif no_years == 0 and no_months == 1:
            no = "It will take 1 month to repay this loan!"
        elif no_years == 0 and no_months > 1:
            no = "It will take {} months to repay ths loan!".format(no_months)

    return no, n


def annuity_payment(credit_prin, interest, count_periods):
    annuity_pay = credit_prin * (interest * pow(1 + interest, count_periods) / (pow(1 + interest, count_periods) - 1))
    return math.ceil(annuity_pay)


def annuity_count_of_periods(interest, annuity_pay, credit_prin):
    base = 1 + interest
    num = annuity_pay / (annuity_pay - (interest * credit_prin))
    n = math.ceil(math.log(num, base))
    return n


def annuity_cred_prin(annuity_pay, count_periods, interest):
    cred = annuity_pay / (interest * pow(1 + interest, count_periods) / (pow(1 + interest, count_periods) - 1))
    return math.floor(cred)


def interest_rate(num):
    interest = (num / 100) / (12 * (100 / 100))
    return interest


def diff_payment(credit_prin, periods, interest):
    dif_payment = 0
    for month in range(1, periods + 1):
        payment = (credit_prin / periods) + (interest * (credit_prin - (credit_prin * (month - 1) / periods)))
        dif_payment += math.ceil(payment)
        print("Month {}: paid out {}".format(month, math.ceil(payment)))
    return dif_payment


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Credit calculator")
    parser.add_argument('--type')
    parser.add_argument('--principal', type=int)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=int)
    args = parser.parse_args()

    if args.type is None:
        print("Incorrect parameters")
        exit()

    if args.type == 'diff':
        present_args = [args.principal, args.periods, args.interest, args.payment].count(None)
        if present_args != 1:
            print("Incorrect parameters")
            exit()

        if args.payment is not None:
            print("Incorrect parameters")
            exit()

        credit_prin = args.principal
        periods = args.periods
        interest = interest_rate(args.interest)

        if credit_prin < 0 or periods < 0 or interest < 0:
            print("Incorrect parameters")
            exit()

        dif_payment = diff_payment(credit_prin, periods, interest)
        overpayments = dif_payment - credit_prin
        print("Overpayment = {}".format(math.ceil(overpayments)))

    elif args.type == 'annuity':
        present_args = [args.principal, args.periods, args.interest, args.payment].count(None)
        if present_args != 1:
            print("Incorrect parameters")
            exit()

        credit_prin = args.principal
        periods = args.periods
        interest = interest_rate(args.interest)
        monthly_payment = args.payment

        if args.periods is None:
            if credit_prin < 0 or monthly_payment < 0 or interest < 0:
                print("Incorrect parameters")
                exit()
            annuity, x = annuity_count_of_months(credit_prin, monthly_payment, interest)
            overpayment = (x * monthly_payment) - credit_prin
            print(annuity)
            print("Overpayment = {}".format(math.ceil(overpayment)))

        elif args.principal is None:
            if monthly_payment < 0 or periods < 0 or interest < 0:
                print("Incorrect parameters")
                exit()
            annuity = annuity_cred_prin(monthly_payment, periods, interest)
            print("Your loan principal = {}". format(annuity))
            overpayment = (periods * monthly_payment) - annuity
            print("Overpayment = {}".format(math.ceil(overpayment)))

        elif args.payment is None:
            if credit_prin < 0 or interest < 0 or periods < 0:
                print("Incorrect parameters")
                exit()
            annuity = annuity_payment(credit_prin, interest, periods)
            print("Your annuity payment = {}!". format(annuity))
            overpayment = (annuity * periods) - credit_prin
            print("Overpayment = {}".format(math.ceil(overpayment)))
