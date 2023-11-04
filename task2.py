# Define arrays to store item information
item_codes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
item_descriptions = ["Compact Case", "Tower Case", "8 GB RAM", "16 GB RAM", "32 GB RAM",
                    "1 TB HDD", "2 TB HDD", "4 TB HDD", "240 GB SSD", "480 GB SSD",
                    "1 TB HDD", "2 TB HDD", "4 TB HDD", "DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer",
                    "Standard Version OS", "Professional Version OS"]
item_prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99,
               49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Initialize total cost with the cost of basic components
total_cost = 200.0

print("Welcome to the Computer Customization Tool!")

while True:
    # Display available items
    print("Available Items:")
    print("Item Code\tDescription\tPrice ($)")
    for i in range(len(item_codes)):
        print(f"{item_codes[i]}\t{item_descriptions[i]}\t{item_prices[i]:.2f}")

    # Choose a category or finish customizing
    print("\nChoose a category to add items or type 'done' to finish customization.")
    category_choice = input("Enter category code (A, B, C, D, E, F, G) or 'done': ").upper()

    if category_choice == "DONE":
        break

    # Display items in the chosen category
    print(f"\n{category_choice} Category Items:")
    print("Item Code\tDescription\tPrice ($)")
    for i in range(len(item_codes)):
        if item_codes[i].startswith(category_choice):
            print(f"{item_codes[i]}\t{item_descriptions[i]}\t{item_prices[i]:.2f}")

    # Choose an item
    chosen_item = input(f"Choose an item from category {category_choice} (Enter the item code): ")

    if chosen_item not in item_codes:
        print("Invalid item code. Please try again.")
    else:
        total_cost += item_prices[item_codes.index(chosen_item)]
        print(f"Added {item_descriptions[item_codes.index(chosen_item)]} to your computer.")

# Display chosen items and total cost
print("\nChosen items:")
print(f"Case: {item_descriptions[item_codes.index(chosen_case)]}")
print(f"RAM: {item_descriptions[item_codes.index(chosen_ram)]}")
print(f"Main Hard Disk Drive: {item_descriptions[item_codes.index(chosen_hdd)]}")
print(f"Additional items:")
for item in chosen_items:
    print(f"{item_descriptions[item_codes.index(item)]}")
print(f"Total cost: ${total_cost:.2f}")

print("Thank you for using our Computer Customization Tool!")
