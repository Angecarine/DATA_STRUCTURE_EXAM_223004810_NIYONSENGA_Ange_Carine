class TreeNode:
    def __init__(self, ticket_id, customer_name, issue_description, status):
        self.ticket_id = ticket_id  # Unique identifier for the ticket
        self.customer_name = customer_name  # Customer's name
        self.issue_description = issue_description  # Description of the issue
        self.status = status  # Current status of the ticket
        self.children = []  # Children nodes (sub-tickets/issues)

    def add_child(self, child_node):
        self.children.append(child_node)  # Add a sub-ticket


class TicketingTree:
    def __init__(self, root_ticket):
        self.root = root_ticket  # Root of the tree (the main ticket)

    def add_ticket(self, parent_ticket_id, ticket):
        parent_ticket = self.find_ticket(self.root, parent_ticket_id)
        if parent_ticket:
            parent_ticket.add_child(ticket)  # Add new ticket as a child of the parent
            print(f"Ticket {ticket.ticket_id} added under parent {parent_ticket_id}.")
        else:
            print(f"Parent ticket {parent_ticket_id} not found.")

    def find_ticket(self, current_node, ticket_id):
        # Recursive search to find a ticket by its ticket_id
        if current_node.ticket_id == ticket_id:
            return current_node
        for child in current_node.children:
            found_ticket = self.find_ticket(child, ticket_id)
            if found_ticket:
                return found_ticket
        return None  # Return None if the ticket is not found

    def update_ticket_status(self, ticket_id, new_status):
        ticket = self.find_ticket(self.root, ticket_id)
        if ticket:
            ticket.status = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print(f"Ticket {ticket_id} not found.")

    def display_ticket_hierarchy(self, current_node=None, level=0):
        # Recursively print the ticket hierarchy
        if current_node is None:
            current_node = self.root  # Start with the root ticket
        print(" " * level * 4 + f"Ticket ID: {current_node.ticket_id}, Customer: {current_node.customer_name}, Issue: {current_node.issue_description}, Status: {current_node.status}")
        for child in current_node.children:
            self.display_ticket_hierarchy(child, level + 1)


# Example Usage:

# Root ticket representing a general issue (e.g., "Login issue")
root_ticket = TreeNode(1, "Aliane", "Login issue", "Open")
ticket_tree = TicketingTree(root_ticket)

# Adding sub-tickets (e.g., issues related to "Login issue")
ticket_tree.add_ticket(1, TreeNode(2, "Alliance", "Forgot password", "Open"))
ticket_tree.add_ticket(1, TreeNode(3, "Cloude", "Two-factor authentication error", "Closed"))

# Adding more tickets under existing sub-tickets
ticket_tree.add_ticket(2, TreeNode(4, "Dave", "Password reset not working", "Open"))
ticket_tree.add_ticket(3, TreeNode(5, "Emma", "Authentication app error", "Closed"))

# Display the ticket hierarchy
print("\nDisplaying ticket hierarchy:")
ticket_tree.display_ticket_hierarchy()

# Update a ticket status
ticket_tree.update_ticket_status(2, "Closed")

# Display the updated ticket hierarchy
print("\nDisplaying updated ticket hierarchy:")
ticket_tree.display_ticket_hierarchy()
