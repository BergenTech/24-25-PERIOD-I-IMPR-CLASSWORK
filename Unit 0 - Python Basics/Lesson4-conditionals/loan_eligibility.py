age = int(input("Enter your age: "))
income = float(input("Enter your annual income in dollars: "))
credit_score = int(input("Enter your credit score: "))

if age >= 18:
    if income >= 25000:
        if credit_score >= 650:
            if age>=30 and income >= 50000 and credit_score >=700:
                risk = "Low Risk"
            elif age>=25 and income >=35000 and credit_score >=650:
                risk = "Medium Risk"
            else:
                risk = "High Risk"
            eligibility = "Eligible"
        else:
            eligibility = "Not Eligible!"
            risk = 'N/A'
    else:
        eligibility = "Not Eligible!"
        risk = 'N/A'
else:
    eligibility = "Not Eligible!"
    risk = "N/A"

print(f"Loan Eligibility:{eligibility}")
if eligibility == "Eligible":
    print(f"Risk Category: {risk}")