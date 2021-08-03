sum = 0

while True:
    userInput = input("Enter the item price: \n")
    if userInput != 'q':

        sum = sum + int(userInput)

        print(f"Total order so far: {sum}")

    else:
        print(f"Total bill so far: {sum}")
        print("Thanks for shopping with us")

        break




