# ----------------------------------------------------------------------------------------------------------------------------------
# Pseudocode
# 
# Get user input - The user chooses from two options
    # investment or bond choices are displayed, user input is requested
    # users input should be manipulated so that it is in all caps
    # if input == BOND run bond line
    # if input == INVESTING run investing line
    # if no input display error

# if investment is selected
#  get user input = amount of money + the interest rate as a number (.strip(%)) + number of years to invest
# and get simple or compound as an input
# if simple is typed then calculate simple interest A = P * (1 + r*t) and print
# if compound is type then calculate compound interest A = P * math.pow((1+r),t) and print

# if user selects bond
#  get user input = P= present value of house + i = the interest rate as a number (strip(%))+ n =  number of months repay the bond
# caluclate repayment as = (i * P)/(1 - (1 + i)**(-n))
# print
# -----------------------------------------------------------------------------------------------------------------------------------


# Note = This is a financial calculator. The user can access either an investment calculator (simple or compound) or a home loan repayment calculator
import math
print("-"*80)
print("Welcome to Tom's Financial Calculators")
print("*"*80)
print("Investment - Choose this calculator to calculate the amount of interest you'll earn on your investment")
print("Bond       - Choose this calculator to calculate the amount you'll have to pay on a home loan")
print("-"*80)
calculation_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculation_choice_upper = calculation_choice.upper()
print(calculation_choice_upper)
# Did consider using something like this = calculation_choice_stripped = calculation_choice.strip("'") 

if calculation_choice_upper == "INVESTMENT":
    amount_of_money = float(input("Please enter the amount of money invested (omit any currency symbols): "))
    interest_rate_investment = float(input("Please enter the interest rate (eg enter 8 for 8%): "))
    number_of_years = float(input("Please enter the number of years you will be investing for: "))
    type_of_interest = input("Please enter the type of interest, either enter 'simple' or 'compound': ")
    type_of_interest_upper = type_of_interest.upper()
    if type_of_interest_upper == "SIMPLE":
        simple_interest = amount_of_money * (1 + (interest_rate_investment/100)*number_of_years)
        print(f"The amount of interest when investing £{amount_of_money} over {number_of_years} years at {interest_rate_investment}% you will gain with simple interest is: £", round(simple_interest, 2))
    if type_of_interest_upper == "COMPOUND":
        compound_interest = amount_of_money * math.pow((1 + (interest_rate_investment/100)), number_of_years)
        print(f"The amount of interest when investing £{amount_of_money} over {number_of_years} years at {interest_rate_investment}% you will gain with compound interest is: £", round(compound_interest, 2))

if calculation_choice_upper == "BOND":
    value_of_loan = float(input("Please enter the present value of the loan (omit any currency symbols): "))
    interest_rate_bond = float(input("Please enter the interest rate (eg enter 8 for 8%): "))
    monthly_interest_rate = (interest_rate_bond/100)/12
    number_of_months = float(input("Please enter the number of months to repay the bond: "))
    repayment = (monthly_interest_rate * value_of_loan) / (1 - (1 + monthly_interest_rate)**(-abs(number_of_months)))
    print(f"The total amount of interest you will be repaying on your loan of {number_of_months} months at {interest_rate_bond}% is: £", round(repayment, 2))
          
# I tested this code many times on my 70+ year old mother which pulled up many issues I hadn't foreseen! I can understand the importance of iterating through the testing process now to find bugs!!!