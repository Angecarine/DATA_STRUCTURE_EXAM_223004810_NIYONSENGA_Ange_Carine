class Node:
    def __init__(self, ticket_id, description, priority):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, ticket_id, description, priority):
        new_node = Node(ticket_id, description, priority)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, node, new_node):
        if new_node.ticket_id < node.ticket_id:
            if node.left is None:
                node.left = new_node
            else:
                self._insert_recursive(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert_recursive(node.right, new_node)

    def search(self, ticket_id):
        return self._search_recursive(self.root, ticket_id)

    def _search_recursive(self, node, ticket_id):
        if node is None or node.ticket_id == ticket_id:
            return node
        if ticket_id < node.ticket_id:
            return self._search_recursive(node.left, ticket_id)
        return self._search_recursive(node.right, ticket_id)

    def in_order_traversal(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        tickets = []
        if node:
            tickets += self._in_order(node.left)
            tickets.append((node.ticket_id, node.description, node.priority))
            tickets += self._in_order(node.right)
        return tickets

    def sort_by_priority(self):
        # Sort the tickets by priority (High > Medium > Low)
        priority_map = {"Critical": 3, "High": 2, "Medium": 1, "Low": 0}
        tickets = self.in_order_traversal()
        return sorted(tickets, key=lambda ticket: priority_map[ticket[2]], reverse=True)


class TicketNode:
    def __init__(self, ticket_id, description, priority):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_ticket(self, ticket_id, description, priority):
        new_node = TicketNode(ticket_id, description, priority)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def search_ticket(self, ticket_id):
        current = self.head
        while current:
            if current.ticket_id == ticket_id:
                return current
            current = current.next
        return None

    def display_tickets(self):
        current = self.head
        tickets = []
        while current:
            tickets.append((current.ticket_id, current.description, current.priority))
            current = current.next
        return tickets

    def remove_ticket(self, ticket_id):
        # Removing ticket from linked list (mark resolved)
        current = self.head
        previous = None
        while current:
            if current.ticket_id == ticket_id:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # Ticket removed
            previous = current
            current = current.next
        return False  # Ticket not found
class TicketingSystem:
    def __init__(self):
        self.bst = BST()  # BST to manage ticket IDs
        self.pending_tickets = SinglyLinkedList()  # Linked list for unresolved tickets

    def add_ticket(self, ticket_id, description, priority):
        # Add to BST for fast search and sorting
        self.bst.insert(ticket_id, description, priority)
        # Also add to linked list for pending ticket tracking
        self.pending_tickets.add_ticket(ticket_id, description, priority)

    def search_ticket(self, ticket_id):
        # First, check the BST
        ticket_node = self.bst.search(ticket_id)
        if ticket_node:
            return (ticket_node.ticket_id, ticket_node.description, ticket_node.priority)
        # If not found, check the linked list
        ticket_node = self.pending_tickets.search_ticket(ticket_id)
        if ticket_node:
            return (ticket_node.ticket_id, ticket_node.description, ticket_node.priority)
        return None

    def display_sorted_tickets(self):
        tickets = self.bst.in_order_traversal()
        if not tickets:
            return "No tickets in the system."
        return "\n".join([f"Ticket ID: {ticket[0]} | Description: {ticket[1]} | Priority: {ticket[2]}" for ticket in tickets])

    def display_sorted_by_priority(self):
        tickets = self.bst.sort_by_priority()
        if not tickets:
            return "No tickets in the system."
        return "\n".join([f"Ticket ID: {ticket[0]} | Description: {ticket[1]} | Priority: {ticket[2]}" for ticket in tickets])

    def display_pending_tickets(self):
        tickets = self.pending_tickets.display_tickets()
        if not tickets:
            return "No pending tickets."
        return "\n".join([f"Ticket ID: {ticket[0]} | Description: {ticket[1]} | Priority: {ticket[2]}" for ticket in tickets])

    def resolve_ticket(self, ticket_id):
        if self.pending_tickets.remove_ticket(ticket_id):
            return f"Ticket {ticket_id} has been resolved and removed from the pending list."
        return f"Ticket {ticket_id} not found in pending tickets."

ticket_system = TicketingSystem()

# Add tickets to the system
ticket_system.add_ticket(101, "Unable to log in", "High")
ticket_system.add_ticket(102, "Page not loading", "Medium")
ticket_system.add_ticket(104, "Payment failed", "High")
ticket_system.add_ticket(105, "Payment failed", "Medium")
ticket_system.add_ticket(106, "Payment failed", "Low")
ticket_system.add_ticket(107, "Critical system failure", "Critical")

# Display all tickets sorted by ticket_id
print("Tickets sorted by Ticket ID:")
print(ticket_system.display_sorted_tickets())

# Display all tickets sorted by priority
print("\nTickets sorted by Priority:")
print(ticket_system.display_sorted_by_priority())

# Search for a specific ticket by ticket_id
print("\nSearch Result for Ticket 102:")
print(ticket_system.search_ticket(102)) 

# Display all pending tickets
print("\nPending Tickets:")
print(ticket_system.display_pending_tickets())

# Resolve a ticket
print("\nResolving Ticket 102:")
print(ticket_system.resolve_ticket(102))

# Display all pending tickets after resolving one
print("\nPending Tickets after resolving:")
print(ticket_system.display_pending_tickets())
