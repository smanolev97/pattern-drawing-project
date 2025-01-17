# 🖼️ Python Pattern Drawing Project

while True:
    # Step 1: Display a menu to the user
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Exit")

    # Step 2: Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    if choice == 9:
        print("Thank you for using the Python Pattern Drawing Program. Goodbye!")
        break
    # Step 3: Get dimensions based on choice
    if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))

    # Step 4: Generate the selected pattern
    if choice == 1:  # Right-angled Triangle
        for i in range(1, rows + 1):
            stars = '*' * i
            print(stars)

    elif choice == 2:  # Square with Hollow Center
        for i in range(size):
            if i == 0 or i == size - 1:
                print('*' * size, end='')
            else:
                print('*' + ' ' * (size - 2) + '*', end='')
            print()

    elif choice == 3:  # Diamond
        for i in range(rows - 1):
            spaces = ' ' * (rows - i - 1)
            stars = '*' * (2 * i + 1)
            print(spaces + stars)
        for i in range(rows, 0, - 1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

    elif choice == 4:  # Left-angled Triangle
        for i in range(rows, 0, -1):
            stars = '*' * i
            print(stars)

    elif choice == 5:  # Hollow Square
        for i in range(size):
            if i == 0 or i == size - 1:
                print('*' * size, end='')
            else:
                print('*' + ' ' * (size - 2) + '*', end='')
            print()

    elif choice == 6:  # Pyramid
        for i in range(rows):
            spaces = ' ' * (rows - i - 1)
            stars = '*' * (2 * i + 1)
            print(spaces + stars)

    elif choice == 7:  # Reverse Pyramid
        for i in range(rows, 0, - 1):
            spaces = ' ' * (rows - i)
            stars = '*' * (2 * i - 1)
            print(spaces + stars)

    elif choice == 8:  # Rectangle with Hollow Center
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for i in range(1, height + 1):
            if i == 1 or i == height:
                print('*' * width)
            else:
                print('*' + ' ' * (width - 2) + '*')

    else:
        print("❌ Invalid choice! Please restart the program.")

    # Step 5: Allow the user to restart
    while True:
        restart = input("Do you want to draw another pattern? (yes to restart, no to exit): ").lower()
        if restart == "yes":
            break  # Breaks the inner loop to restart the program
        elif restart == "no":
            print("Thank you for using the Python Pattern Drawing Program. Goodbye!")
            exit()  # Exits the entire program
        else:
            print("❌ Invalid input. Please enter 'yes' to restart or 'no' to exit.")
