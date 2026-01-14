print("---SIMPLE BUDGET TRACKER---")
salary =  float(input("What is your monthly salary? "))
wage = float(input("What is your weekly wage? "))

monthly_wage = wage * 4
monthly_income = salary + monthly_wage

print(f"Your total monthly income is {monthly_income}")

housing = float(input("How much do you pay for rent or mortgage? "))
food = float(input("How much do you pay for food? "))
transport = float(input("How much do you pay for transport? "))
utilities = float(input("How much do you pay for utilities? "))

monthly_expenses = housing + food + transport + utilities

print(f"Your total monthly expenses is {monthly_expenses}")

balance = monthly_income - monthly_expenses

print(f'The remaining balance is {balance}')
