total = 0
count = 0

while True:
    choice = input("Do you want to enter a transaction? (y/n): ")

    if choice == "n":
        break
    elif choice != "y":
        print("Invalid choice. Please enter 'y' or 'n'.")
        continue

    amount = float(input("Enter today's transaction: "))

    if amount <= 0:
        print("Invalid transaction. Skipping...")
        continue

    total += amount
    count += 1

print("\nTransaction Summary")
print("Total:", total)
print("Count:", count)