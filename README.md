# 🍽 Restaurant Simulation System

A simulation of a restaurant environment using Python. This system imitates real-world interactions between servers, chefs, orders, and menu items. The goal is to simulate a flow of receiving, preparing, and completing food orders with a dynamic menu and randomized staff behavior.

---

## 📌 Features

- Simulates a full restaurant order lifecycle
- Random generation of orders
- Dynamic menu loaded from CSV
- Staff (servers and chefs) loaded from JSON
- Displays detailed processing steps (who takes and who prepares orders)
- Supports ingredient tracking, pricing, and order timing
- Easy-to-extend architecture with classes for MenuItem, Order, Chef, Server, Restaurant

---

## 📁 Project Structure

### `main.py`
- **Entry point** of the application.
- Opens the restaurant.
- Asks user for number of orders to simulate.
- Generates orders randomly from menu.
- Processes them using random chefs and servers.
- Closes the restaurant.
- Creates or overwrites a CSV file (`menu_data.csv`) with predefined sample menu items.

### `chef.py`
- Defines the `Chef` class with name and surname.
- Responsible for preparing orders.
- Simulates time delay using `time.sleep()` to represent real cooking time.
- Outputs who prepared what, with price details.

### `server.py`
- Defines the `Server` class with name and surname.
- Responsible for receiving and logging orders from customers.

### `order.py`
- Defines the `Order` class.
- Contains list of `MenuItem` objects, timestamp, and total price.
- Provides string representation of an order and its total price in AMD.
- Useful for both logging and business logic.

### `menuitem.py`
- Defines the `MenuItem` class.
- Each menu item includes:
  - Name
  - Ingredients
  - Price
  - Priority (for future sorting/logic)
  - Duration (optional: used to simulate prep time)

### `restaurant.py`
- Central controller class `Restaurant`.
- Loads:
  - Menu items from `menu_data.csv`
  - Chefs and servers from `worker_names.txt` (JSON)
- Manages:
  - Opening and closing the restaurant
  - Generating random orders
  - Assigning orders to servers and chefs
- Future plans include comparing chef agility with dish priority (partially implemented).

### `worker_names.txt`
- JSON file defining staff information:
  - Chefs: name, surname, agility level (1–5)
  - Servers: name and surname
- Used by `restaurant.py` to instantiate `Chef` and `Server` objects.

### `menu_data.csv`
- Contains predefined menu items in the following format:
