# Write your solution here
points=int(input("How many points[0-100]:"))
if points < 0 or points > 100:
    print("Grade: impossible!")
elif 0 < points and 50 > points:
    print("Grade: fail")
elif 49 < points and 60 > points:
    print("Grade: 1")
elif 59 < points and 70 > points:
    print("Grade: 2")
elif 69 < points and 80 > points:
    print("Grade: 3")
elif 79 < points and 90 > points:
    print("Grade: 4")
else:
    print("Grade: 5")


