hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
normal_pay = 40 * r

if h > 40:
    Total_hrs = h - 40
    gross_pay = Total_hrs * (1.5 * r)
    total_pay = gross_pay + normal_pay
    print(total_pay)
else :
    gross_pay = h * r
    print(gross_pay)