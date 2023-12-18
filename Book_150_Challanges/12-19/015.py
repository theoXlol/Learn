#Ask the user to enter their favourite colour.
# If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [colour], I prefer red”.

color = input("What colour do you like?: ")

if color == "RED" or color == "red" or color == "Red":
    print("I like red too!")
else:
    print("I dont like the colour", color, "I prefer Red")