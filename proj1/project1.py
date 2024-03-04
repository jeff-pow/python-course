import rate_dict
import table_header as th

'''
Mortgage calculator for Project 1
CSC295
Jeff Powell
9/18/23
'''

# Following four magic numbers are the valid mortgage terms
TEN_YEAR_TERM = 10
FIFTEEN_YEAR_TERM = 15
TWENTY_YEAR_TERM = 20
THIRTY_YEAR_TERM = 30
# Payments are made monthly
PAYMENTS_PER_YEAR = 12


# Main method handles receiving user input and calling methods to preform the
# necessary calculations
def main():
    valid_loan_terms = [TEN_YEAR_TERM, FIFTEEN_YEAR_TERM, TWENTY_YEAR_TERM,
                        THIRTY_YEAR_TERM]
    while True:
        purchase_price = float(input("Enter purchase price of home in USD: "))
        if purchase_price >= 0:
            break
        print("Invalid amount. Please input an amount above zero.")
    while True:
        loan_term = int(input("Enter loan term in years: "))
        if valid_loan_terms.__contains__(loan_term):
            break
        print("Invalid term length. Must be 10, 15, 20, or 30 years.")
    while True:
        down_payment_percentage = float(
            input("Enter down payment percentage: "))
        if 0 <= down_payment_percentage < 100:
            break
        print("Invalid down payment percentage. \
              Please input a valid percentage")

    down_payment_percentage /= 100
    ltv = 1 - down_payment_percentage
    key = get_key(loan_term, ltv)
    rate = rate_dict.rates[key]
    rate /= 100
    payment_remaining = purchase_price - (purchase_price *
                                          down_payment_percentage)
    payment_remaining = payment_remaining

    monthly_payment = calc_monthly_payment(loan_term, payment_remaining, rate)

    print()
    print(f"Loan amount: ${payment_remaining:,.2f}")
    output_loan_info(key)
    # TODO: This may need a comma in the future if Dr. Titus changes formatting
    print(f"Monthly Payment = ${monthly_payment:.2f}")

    math_loop(down_payment_percentage,
              payment_remaining, monthly_payment, rate, purchase_price)


# Calculates the payments that must be made to complete a given mortgage given
# a variety of information about the mortgage
def math_loop(down_payment_percentage, payment_remaining, monthly_payment,
              rate, total_loan_amount):
    purchase_price = payment_remaining
    pmi = get_PMI(purchase_price, down_payment_percentage)
    interest_payments = []
    principal_payments = []
    principal_balances = []
    pmi_payments = []
    while True:
        interest = (rate / PAYMENTS_PER_YEAR * payment_remaining)
        principal = monthly_payment - interest
        interest_payments.append(interest)
        principal_payments.append(principal)
        payment_remaining -= principal
        principal_balances.append(payment_remaining)
        if payment_remaining + principal > total_loan_amount * .8:
            pmi_payments.append(pmi)
        else:
            pmi_payments.append(0)
        if payment_remaining - principal < 0:
            break

    print_summary(interest_payments, principal_payments,
                  pmi_payments, principal_balances, purchase_price)


# Prints a summary of all the information calculated by the program,
# and formats it
def print_summary(interest_payments, principal_payments, pmi_payments,
                  principal_balances, purchase_price):
    th.make_table_header()
    # print(f"{'0':^8} {'':^18} {'':^20} {purchase_price:^20.2f} {'':^9}")
    print(f"{'0':^8}{purchase_price:>54,.2f}")
    for idx in range(len(principal_balances)):
        print(f'{idx + 1:>4} {interest_payments[idx]:>16,.2f} {principal_payments[idx]:>19,.2f} {principal_balances[idx]:>20,.2f} {pmi_payments[idx]:>15,.2f}')

    print("==============================================================================")
    print()
    print("Mortgage Summary")

    interest_sum = 0
    for i in interest_payments:
        interest_sum += i
    print(f"Total interest paid: ${interest_sum:>56,.2f}")

    principal_sum = 0
    for p in principal_payments:
        principal_sum += p
    print(f"Total payment to principal: ${principal_sum:>49,.2f}")

    pmi_sum = 0
    for p in pmi_payments:
        pmi_sum += p
    print(f"Total PMI paid: ${pmi_sum:>61,.2f}")

    total_sum = pmi_sum + principal_sum + interest_sum
    print(f"Total payments: ${total_sum:>61,.2f}")


def calc_monthly_payment(loan_term, payment_remaining, rate):
    monthly_rate = rate / PAYMENTS_PER_YEAR
    total_payments = PAYMENTS_PER_YEAR * loan_term
    return payment_remaining * \
        (monthly_rate * (1 + monthly_rate) ** total_payments) / \
        ((1 + monthly_rate) ** total_payments - 1)


EIGHTY_PERCENT = .8
NINTY_PERCENT = .9


# Returns the string key for a loan to look up the rate for the loan
def get_key(loan_term, ltv):
    key = str(loan_term) + "-Year Fixed, "
    if loan_term == TEN_YEAR_TERM:
        if ltv <= EIGHTY_PERCENT:
            return key + "80% or less LTV"
        elif ltv <= NINTY_PERCENT:
            return key + "80.1-90% LTV"
        else:
            return key + "90.1-100% LTV"
    else:
        if ltv <= NINTY_PERCENT:
            return key + "90% or less LTV"
        else:
            return key + "90.1-100% LTV"


# Takes in the key used to get loan rates, and formats it to output loan info
def output_loan_info(info):
    rate = rate_dict.rates[info]
    print(f"Loan type: {info} at {rate:,.3f}% APR")


# Returns the PMI if there currently is one
def get_PMI(purchase_price, down_payment_percentage):
    ltv = 1 - down_payment_percentage
    if ltv <= .80:
        rate = 0
    elif .80 < ltv <= .85:
        rate = .00375 / PAYMENTS_PER_YEAR
    elif .85 < ltv <= .90:
        rate = .00675 / PAYMENTS_PER_YEAR
    elif .90 < ltv <= .95:
        rate = .00875 / PAYMENTS_PER_YEAR
    else:
        rate = .0103 / PAYMENTS_PER_YEAR

    return purchase_price * rate


if __name__ == "__main__":
    main()
