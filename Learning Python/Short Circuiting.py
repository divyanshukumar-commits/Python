high_income = True
high_credit = True
student = True

# Here if first statement is false whole false entire statement is false
if high_income and high_credit and not student:
    print("Eligible")
else:
    print("Not eligible")


# Similarly if one is true then the whole statement is true
if high_income or high_credit or not student:
    print("Eligible")
else:
    print("Not Eligible")
