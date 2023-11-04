# Define arrays to store item information
item_codes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3"]
item_descriptions = ["Compact Case", "Tower Case", "8 GB RAM", "16 GB RAM", "32 GB RAM",
                    "1 TB HDD", "2 TB HDD", "4 TB HDD"]
item_prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99]

# Initialize total cost with the cost of basic components
total_cost = 200.0

print("Welcome to the Computer Customization Tool!")

# Display available items
print("Available Items:")
print("Item Code\tDescription\tPrice ($)")
for i in range(len(item_codes)):
    print(f"{item_codes[i]}\t{item_descriptions[i]}\t{item_prices[i]:.2f}")

# Choose a case
chosen_case = input("Choose a case (Enter the item code): ")

# Choose RAM
chosen_ram = input("Choose RAM (Enter the item code): ")

# Choose HDD
chosen_hdd = input("Choose a Main Hard Disk Drive (Enter the item code): ")

# Calculate the total cost
chosen_items = [chosen_case, chosen_ram, chosen_hdd]
for i in range(len(item_codes)):
    if item_codes[i] in chosen_items:
        total_cost += item_prices[i]

# Display chosen items and total cost
print("Chosen items:")
print(f"Case: {item_descriptions[item_codes.index(chosen_case)]}")
print(f"RAM: {item_descriptions[item_codes.index(chosen_ram)]}")
print(f"Main Hard Disk Drive: {item_descriptions[item_codes.index(chosen_hdd)]}")
print(f"Total cost: ${total_cost:.2f}")

print("Thank you for using our Computer Customization Tool!")
