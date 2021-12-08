'''
______
PART 3
______
Write a program that asks the user to input one integer. The program will then print two strings, one stating if it's positive, negative, or zero, and another that states whether or not is is divisible by 3. (Hint: to check divisibility by 3, you will find using the modulus(%) operation very helpful.)

3 examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a number:  -2
negative
not divisible by 3

Enter a number:  0
zero
divisible by 3

Enter a number:  5
positive
not divisible by 3
'''

#write your code below
num = int(input("Enter a number: "))

if num < 0 :
  print("Negative")
elif num > 0 :
  print("Positive")
elif num == 0 :
  print("Zero")

num2 = num % 3

if num2 == 0 :
  print("Divisible by 3")
else :
  print("Not divisible by 3")