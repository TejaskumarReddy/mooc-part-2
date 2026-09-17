# Write your solution here
person1=input("Person 1:")
age1=int(input(f"Age of {person1}?"))
person2=input("Person 2:")
age2=int(input(f"Age of {person2}?"))
if age1>age2:
    print(f"The elder is {person1}")
elif age2>age1:
    print(f"The elder is {person2}")
elif age1==age2:
    print(f"{person1} and {person2} are the same age")
