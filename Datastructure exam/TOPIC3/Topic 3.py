class TicketNode:
    def __init__(self, ticket_id, description, priority, status):
        self.ticket_id = ticket_id  # Unique ID for the ticket
        self.description = description  # Issue description
        self.priority = priority  # Priority level (High, Medium, Low)
        self.status = status  # Status (Open, In Progress, Resolved)
        self.next = None  # Pointer to next ticket
        self.prev = None  # Pointer to previous ticket
class TicketList:
    def __init__(self):
        self.head = None  # The first ticket in the list
        self.tail = None  # The last ticket in the list

    # Add a ticket to the list (inserting at the end)
    def add_ticket(self, ticket_id, description, priority, status):
        new_ticket = TicketNode(ticket_id, description, priority, status)
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_ticket
        else:
            self.tail.next = new_ticket  # Append to the end
            new_ticket.prev = self.tail  # Set previous pointer of new ticket
            self.tail = new_ticket  # Update the tail to the new ticket

    # Remove a ticket from the list
    def remove_ticket(self, ticket_id):
        current = self.head
        while current:
            if current.ticket_id == ticket_id:
                if current.prev:
                    current.prev.next = current.next  # Bypass the current node
                if current.next:
                    current.next.prev = current.prev  # Bypass the current node
                if current == self.head:  # If it's the head node
                    self.head = current.next
                if current == self.tail:  # If it's the tail node
                    self.tail = current.prev
                return f"Ticket {ticket_id} has been removed."
            current = current.next
        return f"Ticket {ticket_id} not found."

    # Update the status of a ticket
    def update_ticket_status(self, ticket_id, new_status):
        current = self.head
        while current:
            if current.ticket_id == ticket_id:
                current.status = new_status
                return f"Ticket {ticket_id} status updated to {new_status}."
            current = current.next
        return f"Ticket {ticket_id} not found."

    # Display all tickets in the list
    def display_tickets(self):
        tickets = []
        current = self.head
        while current:
            tickets.append(f"Ticket ID: {current.ticket_id} | Description: {current.description} | Priority: {current.priority} | Status: {current.status}")
            current = current.next
        return "\n".join(tickets) if tickets else "No tickets to display."

    # Display tickets from the last (in reverse order)
    def display_tickets_reverse(self):
        tickets = []
        current = self.tail
        while current:
            tickets.append(f"Ticket ID: {current.ticket_id} | Description: {current.description} | Priority: {current.priority} | Status: {current.status}")
            current = current.prev
        return "\n".join(tickets) if tickets else "No tickets to display."
class CustomerSupportSystem:
    def __init__(self):
        self.ticket_list = TicketList()  # Doubly Linked List to manage tickets

    # Add a new support ticket
    def create_ticket(self, ticket_id, description, priority, status="Open"):
        self.ticket_list.add_ticket(ticket_id, description, priority, status)

    # Remove a ticket by ticket ID
    def delete_ticket(self, ticket_id):
        return self.ticket_list.remove_ticket(ticket_id)

    # Update the status of an existing ticket
    def update_ticket(self, ticket_id, new_status):
        return self.ticket_list.update_ticket_status(ticket_id, new_status)

    # Display all tickets in the list (in order)
    def show_tickets(self):
        return self.ticket_list.display_tickets()

    # Display all tickets in reverse order (for last-to-first viewing)
    def show_tickets_reverse(self):
        return self.ticket_list.display_tickets_reverse()
# Initialize the support system
support_system = CustomerSupportSystem()

# Create tickets
support_system.create_ticket(101, "Unable to access the account", "High")
support_system.create_ticket(102, "Page load time is too slow", "Medium")
support_system.create_ticket(103, "Error when submitting form", "Low")

# Display all tickets
print("All Tickets:")
print(support_system.show_tickets())

# Update a ticket status
support_system.update_ticket(102, "In Progress")

# Display tickets after status update
print("\nUpdated Tickets:")
print(support_system.show_tickets())

# Delete a ticket
support_system.delete_ticket(101)

# Display tickets after deletion
print("\nTickets after deletion:")
print(support_system.show_tickets())

# Display tickets in reverse order
print("\nTickets in reverse order:")
print(support_system.show_tickets_reverse())
