# and or not

high_income = False
high_credit = True
student = True

if high_income and high_credit:
    print("Eligible")
else:
    print("Not Eligible")

if high_income or high_credit:
    print("Eligible")
else:
    print("Not Eligible")

if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or high_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
