import math

# Take user choice

user_choice = input("""investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
Enter either 'investment' or 'bond' from the menu above to proceed: """)

# Take the required inputs from user for investment

if user_choice.lower() == "investment":
    amount = int(input("Please enter the deposit amount "))
    interest_rate = int(input("Please enter interest rate "))
    years = int(input("Please enter the number of years that the money is being invested. "))
    interest = input("Please enter the interest type whether 'simple' or 'compound' ")
    # Calculate simple or compound interest
    if interest.lower() == "simple":
        Total_amount = amount * (1 + (interest_rate / 100) * years)
        print(f"Total Amount you will get after {years} years for simple interest is {Total_amount} ")
    elif interest.lower() == "compound":
        Total_amount = amount * math.pow((1 + (interest_rate/100)), years)
        print(f"Total Amount you will get after {years} years for compound interest is {Total_amount} ")
    else:
        print("Please enter the valid interest type 'Simple/Compound' ")

elif user_choice.lower() == "bond":
    house_value = int(input("Please enter the present value of the house "))
    interest_rate = int(input("Please enter the interest rate "))
    months = int(input("Please enter the number of months you are plan to take to repay the bond "))
    Total_amount = (((interest_rate/100)/12) * house_value) / (1 - (1 + interest_rate) ** (-months))
    print(f"The amount that you will have to be repaid on a home loan each month is {Total_amount} ")
else:
    print("Please enter valid choice")
