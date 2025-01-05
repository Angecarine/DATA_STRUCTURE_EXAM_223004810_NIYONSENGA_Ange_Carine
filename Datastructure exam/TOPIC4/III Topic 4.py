class OrderNode:
    def __init__(self, order_id, customer_name, issue_description, status):
        self.order_id = order_id
        self.customer_name = customer_name
        self.issue_description = issue_description
        self.status = status
        self.next = None


class OrderList:
    def __init__(self, max_orders=10):
        self.head = None  
        self.max_orders = max_orders  
        self.current_orders = 0  

    # Add a new order to the list
    def add_order(self, order_id, customer_name, issue_description, status):
        if self.current_orders >= self.max_orders:
            print("Order limit reached. Cannot add more orders.")
            return
        
        new_order = OrderNode(order_id, customer_name, issue_description, status)
        
        if not self.head:
            # If the list is empty, set the new order as the first node
            self.head = new_order
        else:
            # Insert the new order at the end of the list
            current = self.head
            while current.next:
                current = current.next
            current.next = new_order

        self.current_orders += 1
        print(f"Order {order_id} added successfully.")

    # Update the status of an order by order ID
    def update_order_status(self, order_id, new_status):
        current = self.head
        while current:
            if current.order_id == order_id:
                current.status = new_status
                print(f"Order {order_id} status updated to {new_status}.")
                return
            current = current.next
        print(f"Order {order_id} not found.")

    # Remove an order by order ID
    def remove_order(self, order_id):
        current = self.head
        prev = None
        while current:
            if current.order_id == order_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next  
                self.current_orders -= 1
                print(f"Order {order_id} removed successfully.")
                return
            prev = current
            current = current.next
        print(f"Order {order_id} not found.")

    # Display all orders in the list
    def display_orders(self):
        if not self.head:
            print("No orders to display.")
            return
        current = self.head
        while current:
            print(f"Order ID: {current.order_id}, Customer: {current.customer_name}, Issue: {current.issue_description}, Status: {current.status}")
            current = current.next


# Example Usage:

# Initialize the order list with a limit of 5 orders
order_list = OrderList(max_orders=5)

# Add orders
order_list.add_order(1, "Alice", "Login issue", "Open")
order_list.add_order(2, "Bob", "Payment error", "Open")
order_list.add_order(3, "Charlie", "Page not loading", "Closed")
order_list.add_order(4, "David", "Account suspension", "Open")
order_list.add_order(5, "Eve", "Cannot access dashboard", "Open")

# Attempt to add a 6th order (will fail because of the limit)
order_list.add_order(6, "Frank", "Forgot password", "Open")

# Display all orders
print("\nDisplaying all orders:")
order_list.display_orders()

# Update the status of an order
order_list.update_order_status(2, "Closed")

# Remove an order
order_list.remove_order(3)

# Display all orders after removal and update
print("\nDisplaying all orders after update and removal:")
order_list.display_orders()
