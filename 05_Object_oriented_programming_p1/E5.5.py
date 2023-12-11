total_income = []
total_expenses = []


def get_income():
    while True:
        try:
            income = round(float(input("Enter your income: ")), 2)
            total_income.append(income)
            break
        except ValueError:
            print("Error: Invalid value for income. Please try again.")


def get_expenses():
    while True:
        try:
            expenses = round(float(input("Enter your expenses: ")), 2)
            total_expenses.append(expenses)
            break
        except ValueError:
            print("Error: Invalid value for expenses. Please try again.")
    return expenses


def get_balance():
    balance = sum(total_income) - sum(total_expenses)
    print(f"Your balance is: {balance}")
    return balance


def main():
    while True:
        user_input = int(input(
            "Įveskite veiksmą: \n1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - gauti balansą\n4 - parodyti ataskaitą\n5 - išeiti iš programos\n > "))
        if user_input == 1:
            get_income()
        elif user_input == 2:
            get_expenses()
        elif user_input == 3:
            get_balance()
        elif user_input == 4:
            print(total_income)
            print(total_expenses)
        elif user_input == 5:
            break

    # get income
    # get_expenses()
    # print("User's Income:", users_income
    # balance = users_income - users_expense
    # print()
    # print("User's Expenses:", users_expense)
    # print(f"Your balance is: {balance}")


if __name__ == "__main__":
    main()