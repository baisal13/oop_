from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart

def menu():
    while True:
        print("\n1. Show Devices\n2. Show Cart\n3. Apply Discount\n4. Interact with Device\n5. Checkout\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for i, device in enumerate(devices):
                print(f"{i+1}. {device}")
            item_choice = int(input("Select device to add to cart (0 to cancel): "))
            if item_choice > 0 and item_choice <= len(devices):
                quantity = int(input("Enter quantity: "))
                print(cart.add_device(devices[item_choice-1], quantity))

        elif choice == "2":
            print(cart.print_items())
            print(cart.get_total_price())

        elif choice == "3":
            for i, device in enumerate(devices):
                print(f"{i+1}. {device}")
            item_choice = int(input("Select device to apply discount (0 to cancel): "))
            if item_choice > 0 and item_choice <= len(devices):
                discount = float(input("Enter discount percentage: "))
                print(devices[item_choice-1].apply_discount(discount))

        elif choice == "4":
            for i, device in enumerate(devices):
                print(f"{i+1}. {device}")
            item_choice = int(input("Select device to interact with (0 to cancel): "))
            if item_choice > 0 and item_choice <= len(devices):
                device = devices[item_choice-1]
                if isinstance(device, Smartphone):
                    print("1. Make Call\n2. Install App")
                    action = input("Choose an action: ")
                    if action == "1":
                        print(device.make_call())
                    elif action == "2":
                        print(device.install_app())
                elif isinstance(device, Laptop):
                    print("1. Run Program\n2. Use Keyboard")
                    action = input("Choose an action: ")
                    if action == "1":
                        print(device.run_program())
                    elif action == "2":
                        print(device.use_keyboard())
                elif isinstance(device, Tablet):
                    print("1. Browse Internet\n2. Use Touchscreen")
                    action = input("Choose an action: ")
                    if action == "1":
                        print(device.browse_internet())
                    elif action == "2":
                        print(device.use_touchscreen())

        elif choice == "5":
            print(cart.checkout())

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option, try again.")

devices = [
    Smartphone("Samsung Galaxy S23", 1099, 15, 24, 6.5, 25),
    Laptop("Dell XPS 15", 1899, 7, 36, 32, 4.2),
    Tablet("Samsung Galaxy Tab S8", 699, 10, 18, "2560x1600", 500),
]

cart = Cart()

if __name__ == "__main__":
    menu()


