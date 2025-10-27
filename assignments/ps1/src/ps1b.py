def get_number(input_message, error_message, condition):
    """Gets the appropriate number given the condition."""
    while True:  # theoretically possible to have infinite loop, not concerned about that here
        try:
            val = float(input(input_message))
        except ValueError:
            print("Enter an appropriate numeric value.")
            continue
        if not condition(val):
            print(error_message)
            continue
        return val
    
def calculate_months(annual_salary, portion_saved, total_cost,
                     semi_annual_raise, r=0.04, portion_down_payment=0.25, current_savings=0.0):
    """Returns months to reach down payment with regular raise"""
    down_payment = portion_down_payment * total_cost

    # case: already have enough
    if current_savings >= down_payment:
        return 0
    
    monthly_salary = annual_salary / 12
    monthly_contribution = monthly_salary * portion_saved

    # case: impossible; no contribution and no interest
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

        if months % 6 == 0:  # need to update the monthly figures based on the new annual salary
            annual_salary *= (1.0 + semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_contribution = monthly_salary * portion_saved

    return months
    
if __name__ == "__main__":
    # conditions to determine valid input
    is_nonnegative = lambda x: x >= 0
    is_decimal = lambda x: 0 <= x <= 1
    
    annual_salary = get_number("Enter your starting annual salary: $", 
                               "Must be $0 or more.", condition=is_nonnegative)
    
    portion_saved = get_number("Enter the percent of your salary to save, as a decimal: ", 
                               "Must be a decimal between [0,1].", condition=is_decimal)
    
    total_cost = get_number("Enter the cost of your dream home: $", 
                            "Must be $0 or more.", condition=is_nonnegative)
    
    semi_annual_raise = get_number("Enter the semi-annual raise, as a decimal: ", 
                                   "Must be a decimal between [0,1].", condition=is_decimal)  # makes the assumption the raise cannot be more than doubled
    try:
        total_months = calculate_months(annual_salary, portion_saved, total_cost, semi_annual_raise)
        print(f"Number of months: {total_months}")
    except ValueError as e:
        print(e)
