while True:
    get_int = int(input("Enter an integer between 1 and 8: "))
    if 1 <= get_int <= 8:
        break
    else:
        print("Number is invalid. Please try again.")

for i in range(1, get_int + 1):

    left_side = "#" * i
    right_side = "#" * i
    spaces = " " * (get_int - i)
    print(spaces + left_side + "  " + right_side)
