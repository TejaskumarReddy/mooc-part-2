# Write your solution here
attempts=0
pin=4321
while True:
    attempts +=1
    code=int(input("Password:"))
    if code == pin:
        break
    else:
        print("Wrong")
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
