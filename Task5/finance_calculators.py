# This Program will allow the user to calculate their interest on an investment;
# or alternatively calculate the amount that should be repaid on a home loan each month

import math

# We want user to be able to choose which calculator they want to use, investment or loan repayment
print("\ninvestment \t- to calculate the amount of interest you will earn on your investment \nbond \t\t- to calculate the amount you will have to pay on a home loan\n")
print("Enter either 'investment' or 'bond' from the menu above to proceed: \n")


while True:

    user_selection = input("Please enter the name of preffered calculator: ") # requesting user's input
    
    calculator_type = user_selection.lower() # changing all letters to a lower case, as we don't know how user will type it in
    calculator_type = calculator_type.strip() # removing any spaces at the beginning, so the calculator works if user puts a space by mistake


    if (calculator_type == "investment"):  # INVESTMENT CALCULATOR #
        print("\n***Investment Calculator selected***\n") 

        try:
            # gathering data required for investment calcualtions
            deposit = int(input("Enter the amount of money you are depositing: \t")) # deposit
            interest_rate = float(input("Enter the intrest rate: \t\t\t")) # intrest rate
            interest_rate = interest_rate/100 # since we are asking for an interest %, we have to divide it by 100, otherwise math will not work
            num_years = int(input("Enter number of years you plan to invest: \t")) # years invested

        except ValueError:
            print("Invalid input, please enter a valid numerical value.")
            continue

        # asking user to choose type of investment calculator
        print('''\nYou can choose between 'simple' or 'compund' intrest. 
            \n\tSIMPLE - continually calculated on the initial amount invested and is only calculated once per year.
            \n\tCOMPOUND - the intrest is calculated on the current total know as the accumulated amount \n''')
        
        type_of_interest = str(input("Please enter an intrest type you would like to use:\t"))
        type_of_interest = type_of_interest.lower()

        # simple formula A = P * (1 + r * t)    <<A-total amount once intrest is applied, P-deposit, r-intrest rate, t-number of years>>
        if type_of_interest == "simple":
            simple = deposit * (1 + interest_rate * num_years)
            print(f"\nThe total amount of money you would accumulate after {num_years} years is: £ {simple}\n")
            break


        # compund formula A = P * math.pow((1 + r), t))    <<A-total amount once intrest is applied, P-deposit, r-intrest rate, t-number of years>>
        elif type_of_interest == "compound":
            compound = deposit * math.pow(((1 + interest_rate)), num_years)
            print(f"\nThe total amount of money you would accumulate after {num_years} years is: £ {compound}\n")
            break
        
    
    elif (calculator_type == "bond"): # HOME LOAN REPAYMENT CALCULATOR #
        print("\n***Home Loan Repayment Calculator selected***\n")
        house_value = int(input("Please enter your house value: \t\t\t\t\t\t"))
        monthly_interest_rate = float(input("Please enter your monthly intrest rate: \t\t\t\t"))
        monthly_interest_rate = monthly_interest_rate/100
        num_months_repaid = int(input("Please enter in how many months you would like to repay your loan: \t"))

        # formula:  Repayment = (i * P) / (1 - ( 1 + i) ** (-n))   << P-house value, i-monthly intrest rate, n-number of months the loan will be repaid>>
        repayment = (monthly_interest_rate * house_value) / (1 -(1 + monthly_interest_rate) ** (-num_months_repaid))
        print(f"\nYou will have to repay £ {repayment} every month.\n\n")
        break

    else:
        print("Invalid input, please make sure your spelling is correct\n")



