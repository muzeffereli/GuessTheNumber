from random import randint

start=1
end=1000
value=randint(start,end)

print(value)

print("The computer chose a number between",start,"and",end)

guess=None

while guess!=value:
  guess=int(input("Guess the number:"))

  if guess < value:
    print("The number is higher")
  elif guess > value:
    print("The number is Lower")
print("Congratulations!!! You guess the number.You won.")