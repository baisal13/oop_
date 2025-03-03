1)Base Class - Device
Methods:
display_info(): Prints device details.
__str__(): Returns a string representation of the device.
apply_discount(): Reduces the price based on a discount percentage.
is_available(): Checks if the required quantity is in stock.
reduce_stock(): Reduces stock if the purchase is valid.

2)Smartphone Class - Derived from Device
Additional Attributes:
screen_size: Screen size in inches.
battery_life: Battery life in hours.

Methods:
make_call(): Simulates making a phone call.
install_app(): Simulates installing an application.

3)Laptop Class - Derived from Device
Additional Attributes:
ram_size: RAM capacity in GB.
processor_speed: Processor speed in GHz.

Methods:
run_program(): Simulates running a program.
use_keyboard(): Simulates typing on the keyboard.

4)Tablet Class - Derived from Device
Additional Attributes:
screen_resolution: Screen resolution (e.g., "2048x1536").
weight: Weight of the tablet in grams.

Methods:
browse_internet(): Simulates browsing the internet.
use_touchscreen(): Simulates using a touchscreen.

5)Cart System
Attributes:
items: A list of tuples storing devices and their quantities.
total_price: The total cost of items in the cart.

Methods:
add_device(): Adds a device to the cart if stock is available.
remove_device(): Removes a device from the cart.
get_total_price(): Returns the total price of the cart.
print_items(): Prints all items in the cart.
checkout(): Finalizes the purchase and clears the cart.
