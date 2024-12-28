
food_expenses = 0.0
transport_expenses = 0.0
entertainment_expenses = 0.0
other_expenses = 0.0
total_expenses = 0.0


def display_summary():
    global total_expenses
    if total_expenses == 0:
        print("No expenses recorded.")
        return
    
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Food: ${food_expenses:.2f} ({(food_expenses / total_expenses) * 100:.2f}%)")
    print(f"Transport: ${transport_expenses:.2f} ({(transport_expenses / total_expenses) * 100:.2f}%)")
    print(f"Entertainment: ${entertainment_expenses:.2f} ({(entertainment_expenses / total_expenses) * 100:.2f}%)")
    print(f"Other: ${other_expenses:.2f} ({(other_expenses / total_expenses) * 100:.2f}%)")
    print("-----------------------")

while True:
    print("\n--- Daily Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == '1':
        category = input("Enter the category (Food, Transport, Entertainment, Other): ").strip().lower()
        amount = float(input("Enter the expense amount: "))
        
        # here we update the category 
        if category == 'food':
            food_expenses += amount
        elif category == 'transport':
            transport_expenses += amount
        elif category == 'entertainment':
            entertainment_expenses += amount
        elif category == 'other':
            other_expenses += amount
        else:
            print("Invalid category. Please try again.")
            continue
        
        # here we update the expense
        total_expenses += amount
        print(f"Added ${amount:.2f} to {category.capitalize()} expenses.")
    
    elif choice == '2':
        display_summary()
    
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid option. Please choose again.")
