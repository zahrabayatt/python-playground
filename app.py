high_income = True
good_credit = True
student = True

# Short-circuit Evaluation:
# In python, logical operators are short circuit.

if high_income and good_credit and not student:
    print("Eligible")

if high_income or good_credit and not student:
    print("Eligible")
