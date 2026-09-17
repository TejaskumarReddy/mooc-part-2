# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
summ=0
positive_numbers=0
negative_numbers=0
while True:
    number=int(input("Number:"))
    if number ==0:
        break
    numbers += 1
    summ += number
    mean =float(summ/numbers)
    previous_number=number
    if number > 0:
        positive_numbers +=1
    elif number < 0:
        negative_numbers += 1
print("... the program asks for numbers")
print(f"Numbers typed in {numbers}")
print(f"The sum of the numbers is {summ}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
