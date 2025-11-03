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

def calculate_savings(annual_salary, portion_saved, months, semi_annual_raise=0.07, current_savings=0.0, r=0.04):
    """Calculates the savings in n-months given annual salary and portion saved"""
    cur_month = 0

    monthly_salary = annual_salary / 12
    monthly_contribution = monthly_salary * portion_saved

    monthly_rate = r / 12

    while cur_month < months:
        current_savings += current_savings * monthly_rate
        current_savings += monthly_contribution
        cur_month += 1

        if cur_month % 6 == 0:  # need to update the monthly figures based on the new annual salary
            annual_salary *= (1.0 + semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_contribution = monthly_salary * portion_saved
    
    return current_savings

def bisection_search(annual_salary, n_months=36, scale=10_000, total_cost=1_000_000, portion_down_payment=0.25):
    """Find the lowest savings rate to reach down payment in n months"""
    down_payment = portion_down_payment * total_cost

    # check the impossibility case
    max_savings = calculate_savings(annual_salary, portion_saved=1.0, months=n_months)
    if max_savings < down_payment - 100.0:
        raise ValueError
    
    target_min = down_payment - 100.0
    low, high = 0, scale            
    steps = 0

    # high is guaranteed sufficient
    while low < high:
        mid = (low + high) // 2
        portion_saved = mid / scale
        current_savings = calculate_savings(annual_salary, portion_saved, n_months)

        if current_savings < target_min:  # move up one if not enough savings yet
            low = mid + 1                 # guaranteed minimum
        else:
            high = mid                    # if too much savings, move the high down; we're looking for minimum

        steps += 1        

    return round(low / scale, 4), steps
      
if __name__ == "__main__":
    # conditions to determine valid input
    is_nonnegative = lambda x: x >= 0
    
    annual_salary = get_number("Enter the starting annual salary: $", 
                               "Must be $0 or more.", condition=is_nonnegative)
    
    try:
        portion_saved, steps = bisection_search(annual_salary)
        print(f"Best savings rate: {portion_saved:.4f}")
        print(f"Steps in bisection search: {steps}")
    except:
        print("It is not possible to pay the down payment in three years.")
        