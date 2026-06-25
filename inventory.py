# Holly Paulk
# M03T07 – OOP – Synthesis
# Practical task


# ========The beginning of the class==========
class Shoe:
    """Initialize shoe attributes."""
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe."""
        return self.quantity

    def __str__(self):
        """Return a readable string representation of the shoe."""
        return (f"Country: {self.country}, Code: {self.code}, "
                f"Product: {self.product}, Cost: {self.cost}, "
                f"Quantity: {self.quantity}")


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt and read the data from this
    file, then create a shoes object with this data and append this object
    into the shoes list. One line in this file represents data to create one
    object of shoes. You must use the try-except in this function for error
    handling. Remember to skip the first line using your code.
    '''
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # skip header line

            for line in file:
                try:
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoe = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe)
                except ValueError:
                    print(f"Skip invalid line: {line.strip()}")

        print("Inventory data successfully processed.")

    except FileNotFoundError:
        print("Error: inventory.txt file not found.")


def capture_shoes():
    '''
    This function will allow a user to capture data about a shoe and use this
    data to create a shoe object and append this object inside the shoe list.
    '''
    try:
        country = input("Enter country: ")
        code = input("Enter shoe code: ")
        product = input("Enter product name: ")
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        print("Shoe added successfully.")

    except ValueError:
        print("Invalid input. Cost must be a number and quantity must be an integer.")


def view_all():
    '''
    This function will iterate over the shoes list and print the details of the
    shoes returned from the __str__ function. Optional: you can organise your
    data in a table format by using Python’s tabulate module.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    print("\n----- Shoe Inventory -----")
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity, which is
    the shoes that need to be re-stocked. Ask the user if they want to add
    this quantity of shoes and then update it. This quantity should be updated
    on the file for this shoe.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    lowest = min(shoe_list, key=lambda x: x.quantity)

    print(f"\nLowest stock item:\n{lowest}")

    try:
        choice = input("Do you want to restock this item? (yes/no): ").lower()

        if choice == "yes":
            add_qty = int(input("Enter quantity to add: "))
            lowest.quantity += add_qty

            update_inventory_file()
            print("Stock updated successfully.")

    except ValueError:
        print("Invalid quantity entered.")


def search_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    code = input("Enter shoe code to search: ")

    for shoe in shoe_list:
        if shoe.code == code:
            print("Shoe found:")
            print(shoe)
            return shoe

    print("Shoe not found.")
    return None


def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    print("\n--- Inventory Value ---")
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product} ({shoe.code}) - Total Value: {value}")


def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    if not shoe_list:
        print("No shoes available.")
        return

    highest = max(shoe_list, key=lambda x: x.quantity)

    print("\nProduct with Highest Quantity (FOR SALE):")
    print(highest)


def update_inventory_file():
    """Writes updated shoe list back to inventory.txt."""
    try:
        with open("inventory.txt", "w") as file:
            file.write("country,code,product,cost,quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    except Exception as e:
        print(f"Error updating file: {e}")


# ==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


def main_menu():
    read_shoes_data()

    while True:
        print("\n----- SHOE INVENTORY MENU -----")
        print("1. View all shoes")
        print("2. Add new shoe")
        print("3. Search shoe by code")
        print("4. Restock lowest quantity shoe")
        print("5. View value per shoe")
        print("6. View highest quantity (FOR SALE)")
        print("7. Exit")

        option = input("Select an option: ")

        if option == "1":
            view_all()
        elif option == "2":
            capture_shoes()
            update_inventory_file()
        elif option == "3":
            search_shoe()
        elif option == "4":
            re_stock()
        elif option == "5":
            value_per_item()
        elif option == "6":
            highest_qty()
        elif option == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")


# ==========Run Program=============
if __name__ == "__main__":
    main_menu()
