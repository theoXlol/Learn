'''
Challenge:
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”.
'''

question1 = input("Is it raining?: ")
question2 = input("Is it windy?: ")

question1 = question1.lower()
question2 = question2.lower()

if question1 == "no":
    print("Enjoy your day!")


if question1 == "yes" and question2 == "no":
    print("You need a umbrella")
elif question1 == "yes" and question2 == "yes":
    print("It is to windy for a umbrella, stay at home")