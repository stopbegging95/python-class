def message():
    print("Tax Calculator")
    user_input()

def user_input():
    user_name = input("Enter your name: ")
    dependents = int(input("Enter your dependent: "))
    gross_income = float(input("Enter Gross Income: "))
    cal_tax(user_name, dependents, gross_income)

def cal_tax(user_name, dependents, gross_income):
    tax_rate_dec = .20
    std_deduction = 10000
    dep_deduction = dependents * 200
    total_deduction = std_deduction + dep_deduction
    taxable_income = gross_income - total_deduction
    income_tax = taxable_income * tax_rate_dec
    print(f"Hello, {user_name}")
    print(f"You have entered {dependents} dependents")
    print(f"You have entered the gross income of: {gross_income:,.2f} ")
    print(f"{user_name}, your taxable income is: ${taxable_income:,.2f}")
    print(f"And your income tax is: {income_tax:,.2f}")

if __name__=="__main__":
    message()


