UserName = input("Enter your name: ")
Address = input("Enter your address: ")
MobileNumber = input("Enter your mobile number: ")
if len(MobileNumber) != 10 or MobileNumber.isdigit() == False:
    print("Invalid mobile number. Please enter a 10-digit number.")
    MobileNumber = input("Enter your mobile number: ")
total_price = 0
menu = {
    "Pizza": 250,
    "Burger": 30,
    "Pasta": 150,
    "Momos": 100
}
print("\nMenu:")
for item in menu:
    print(f"{item}: Rs.{menu[item]}")
flag = True
while flag:
    current_item = input("Enter the item you want to order (or type 'done' to finish): ")
    current_item = current_item.strip().lower()
    if current_item == 'done':
        total_price += total_price * 0.18
        flag = False
        break
    current_item = current_item.title()
    if current_item in menu:
        item_price = menu[current_item]
        quantity = int(input(f"Enter the quantity of {current_item}: "))
        total_price += item_price * quantity
    else:
        print("Item not found in the menu. Please try again.")

print(total_price)