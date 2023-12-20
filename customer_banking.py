# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

def check_user_input_float(user_input):
    """
    function that validates the users input is actually a float, 
    if valid returns the float and False
    otherwise it returns None and True
    """
    if user_input.isdigit():
        return float(user_input), True

    print("The inputed value was not a number, you must input a number")
    return None, False

def check_user_input_int(user_input):
    """
    function that validates the users input is actually an int, 
    if valid returns the float and False
    otherwise it returns None and True
    """
    if user_input.isdigit():
        return int(user_input), True

    print("The inputed value was not a number, you must input a number")
    return None, False

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance_is_digit = False
    savings_interest_is_digit = False
    savings_maturity_is_digit = False

    while not savings_balance_is_digit:
        savings_balance, savings_balance_is_digit = check_user_input_float(input("What is the starting balance for the savings account? "))

    while not savings_interest_is_digit:
        savings_interest, savings_interest_is_digit = check_user_input_float(input("What is the interest rate for the saving account? "))

    while not savings_maturity_is_digit:
        savings_maturity, savings_maturity_is_digit = check_user_input_int(input("What is the maturity(number of months) of the savings account? "))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated saving balance: ${updated_savings_balance:,.2f}")
    print(f"Interest earned: ${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance_is_digit = False
    cd_interst_is_digit = False
    cd_maturity_is_digit = False

    while not cd_balance_is_digit:
        cd_balance, cd_balance_is_digit = check_user_input_float(input("What is the starting balance for the cd account? "))

    while not cd_interst_is_digit:
        cd_interest, cd_interst_is_digit = check_user_input_float(input("What is the interest rate for the cd account? "))

    while not cd_maturity_is_digit:
        cd_maturity, cd_maturity_is_digit = check_user_input_int(input("What is the maturity(number of months) of the cd account? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated cd balance: ${updated_cd_balance:,.2f}")
    print(f"Interest earned: ${interest_earned:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
