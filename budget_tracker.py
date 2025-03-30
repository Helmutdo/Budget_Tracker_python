"""Budget Tracker App"""

def add_expense(expenses, description, amount):
    """add an expense to the list of expenses
    
    expenses: list of expenses
    description: description of the expense
    amount: amount of the expense

    return: None    
    """
    for expense in expenses:
        if expense["description"] == description:
            expense["amount"] += amount
            print(f"Updated expense: {description}, new amount: ${expense['amount']}")
            return
    
    # If the description was not found, add a new expense
    expenses.append({"description": description, "amount": amount})
    print(f"Added new expense: {description}, amount: ${amount}")

def get_total_expenses(expenses):
    """get total expeneses
    
    expenses: list of expenses
    
    return: total expenses
    """
    sum = 0
    for expense in expenses:
        sum += expense["amount"]
    return sum

def get_balance(budget, expenses):
    """get the remaining budget
    
    budget: initial budget
    expenses: list of expenses

    return: remaining budget    
    """
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    """show the budget details
    budget: initial budget
    expenses: list of expenses

    return: None    
    """
    print("\n______________________________")
    print("\nTotal budget: $", budget)
    print("Expenses: ")
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']}")
    print(f"Total spend: {get_total_expenses(expenses)}")
    print(f"\nRemaining budget: ${get_balance(budget, expenses)}")
    print("______________________________")


# Main function to run the Budget Tracker
def main():
    """Main function to run the budget tracker"""
    print("""______________________________
          
Welcome to the Budget Tracker!
______________________________""")
    initial_budget = float(input("Enter your initial budget: "))
    budget = initial_budget
    expenses = []

    # loop menu
    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")

        # get user valid input
        try:
            choice = input("Enter your choice (1 - 3): ")
        except ValueError:
            print("\Invalid input. Please enter a valid number.")
            continue
        if choice == "1":
            try:
                description = input("Enter expense description: ").upper()
                if not description.isalpha():
                    print("Description must be a word. Please try again.")
                    continue

                amount = float(input("Enter expense amount: "))
                if amount <=0:
                    print("Amount must be a positive number. Please try again.")
                    continue
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
                continue
            add_expense(expenses, description, amount)
        elif choice == "2":
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("Exiting the Budget Tracker, ciao !")
            break
        else:
            print("\nInvalid choice. Please try again.")

# run main function
if __name__ == "__main__":
    main()