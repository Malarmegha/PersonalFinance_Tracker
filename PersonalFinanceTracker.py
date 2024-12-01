class PersonalFinanceTracker:
    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self):
        self.budget = float(input("Enter your budget: "))
        print(f"Budget set to ${self.budget:.2f}")

    def add_expense(self):
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        self.expenses.append({'name': name, 'amount': amount})
        print(f"Expense '{name}' of ${amount:.2f} added.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense['name']}: ${expense['amount']:.2f}")
        
        total_expenses = sum(exp['amount'] for exp in self.expenses)
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Remaining Budget: ${self.budget - total_expenses:.2f}")

    def main(self):
        while True:
            print("\nPersonal Finance Tracker")
            print("1. Set Budget")
            print("2. Add Expense")
            print("3. View Expenses")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.set_budget()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.view_expenses()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = PersonalFinanceTracker()
    tracker.main()
