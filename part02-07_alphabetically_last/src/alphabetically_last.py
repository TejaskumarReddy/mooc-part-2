# Write your solution here
word1=input("Please type in first word:")
word2=input("Please type in second word")
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")