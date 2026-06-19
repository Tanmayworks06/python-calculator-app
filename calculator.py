while True:
    print("=== Call functions to perform ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter no. b/w(1-5): "))

        if choice == 5:
            print("Goodbye, have a nice day")
            break

        numbers = list(map(float, input("Enter numbers: ").split()))

        if choice == 1:
            print("Result:", sum(numbers))


        elif choice == 2:
            result = numbers[0]

            for num in numbers[1:]:
                result -= num

            print("Result:", result)


        elif choice == 3:
            result = 1

            for num in numbers:
                result *= num

            print("Result:", result)


        elif choice == 4:
            result = numbers[0]

            for num in numbers[1:]:

                if num == 0:
                    print("Cannot divide by zero")
                    break

                result /= num

            else:
                print("Result:", result)


        else:
            print("Invalid option")

    except ValueError:
        print("Enter numbers only")

        