# Employee Payroll Calculator

emp_name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

# Allowances
hra = 0.20 * basic_salary   # House Rent Allowance
da = 0.10 * basic_salary    # Dearness Allowance

# Deductions
pf = 0.12 * basic_salary    # Provident Fund
tax = 0.05 * basic_salary   # Tax

gross_salary = basic_salary + hra + da
net_salary = gross_salary - (pf + tax)

print("\n----- Employee Payroll -----")
print("Employee Name:", emp_name)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)
print("PF Deduction:", pf)
print("Tax Deduction:", tax)
print("Net Salary:", net_salary)
