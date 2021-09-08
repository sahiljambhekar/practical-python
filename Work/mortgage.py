# mortgage.py
#
# Exercise 1.7
PRINCIPAL = 5e5
MONTHLY_PAYMENT = 2684.11
INTEREST_RATE = 0.05 

def calculate_total(remaining):
  total_paid = 0.0
  while(remaining >= 0):
    remaining = remaining * (1 + INTEREST_RATE/12) - MONTHLY_PAYMENT
    total_paid = total_paid + MONTHLY_PAYMENT
  print("Total Paid {:.2f}".format(total_paid))

calculate_total(PRINCIPAL)

DOWNPAYMENT = 2e5
calculate_total(PRINCIPAL-DOWNPAYMENT)

