def get_number(input_message, condition, error_message):
    """Gets the appropriate number given the condition"""
    while True:  # theoretically possible to have an infinite loop if the user's entry is never valid, but not worried about that here
        try:
            val = float(input(input_message))
        except:
            print("Enter an appropriate value.")
            continue
        if not condition(val):
            print(error_message)
            continue
        return val
    
def calculate_months(annual_salary, portion_saved, total_cost, r=0.04, portion_down_payment=0.25, current_savings=0.0):
    """Returns months to reach down payment"""
    down_payment = portion_down_payment * total_cost

    # if the money is already there, no need to save further
    if current_savings >= down_payment:
        return 0
    
    monthly_salary = annual_salary / 12
    monthly_contribution = monthly_salary * portion_saved

    # in the case where it's impossible; prevents infinite loop
    if current_savings == 0 and monthly_contribution == 0:
        raise ValueError
    
    monthly_rate = r / 12
    months = 0

    # standard case; could take many many months if low contribution and high down payment, but not worried about overflow here
    while current_savings < down_payment: 
        # adding interest before the contribution was the only way to get the test cases to work
        current_savings += current_savings * monthly_rate
        current_savings += monthly_contribution
        months += 1

    return months
    
if __name__ == "__main__":
    # conditions to determine valid input
    is_nonnegative = lambda x: x >= 0
    is_decimal = lambda x: 0 <= x <= 1
    
    annual_salary = get_number(input_message="Enter starting salary: $", 
                               condition=is_nonnegative, 
                               error_message="Must be $0 or more.")
    
    portion_saved = get_number(input_message="Enter the percent of your salary to save, as a decimal: ",
                               condition=is_decimal, 
                               error_message="Must be a decimal between [0,1].")
    
    total_cost = get_number(input_message="Enter cost of your dream home: $", 
                            condition=is_nonnegative, 
                            error_message="Must be $0 or more.")
    
    try:
        total_months = calculate_months(annual_salary, portion_saved, total_cost)
        print(f"Number of months: {total_months}")
    except:
        print("Not possible to save with no savings or no contribution.")
