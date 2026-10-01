

print("Welcome to the Bill Splitter App!\n")

while True:
    try:
        bill = float(input("Enter total bill amount: "))
        if bill < 0:
            print("Error: Bill amount cannot be negative. Please try again.\n")
            continue

        people = int(input("Enter number of people: "))
        while people <= 0:
            print("Error: Number of people must be greater than 0.")
            people = int(input("Enter number of people: "))

        tip_percentage = int(input("Enter tip percentage (0/5/10/15/20): "))
        if tip_percentage < 0:
            print("Error: Tip percentage cannot be negative. Please try again.\n")
            continue

        # Calculations
        tip_amount = (tip_percentage / 100) * bill
        final_bill = bill + tip_amount
        per_person = final_bill / people

        # Display formatted output
        print(f"\nTip Amount: ₹{tip_amount:.2f}")
        print(f"Total Bill (with Tip): ₹{final_bill:.2f}")
        print(f"Each person should pay: ₹{per_person:.2f}\n")

        # Repeat option
        repeat = input("Would you like to calculate another bill? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Thank you for using the Bill Splitter App!")
            break
        print()

    except ValueError:
        print("Invalid input! Please enter numeric values where required.\n")