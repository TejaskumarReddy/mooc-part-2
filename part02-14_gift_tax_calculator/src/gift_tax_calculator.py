# Write your solution here
value=int(input("Value of gift:"))
if 0 < value < 5000:
    print("No tax!")
elif 5000<=value<25000:
    tax=float(100 +(value - 5000)*0.08)
    print(f"Amount of tax: {tax} euros")
elif 25000<=value<55000:
    tax=float(1700 +(value - 25000)*0.1)
    print(f"Amount of tax: {tax} euros")
elif 55000<=value<200000:
    tax=float(4700 +(value - 55000)*0.12)
    print(f"Amount of tax: {tax} euros")
elif 200000<=value<1000000:
    tax=float(22100 +(value - 200000)*0.15)
    print(f"Amount of tax: {tax} euros")
elif value>=1000000:
    tax=float(142100 +(value - 1000000)*0.17)
    print(f"Amount of tax: {tax} euros")
