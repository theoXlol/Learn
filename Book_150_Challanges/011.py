'ask the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.'

larger = int(input('Enter a number over a 100 :'))
smaller = int(input('Enter a number under 100'))
answer = larger//smaller
print(smaller,'goes into',larger,answer,'times')