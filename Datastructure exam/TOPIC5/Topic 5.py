class TicketNode:
    def __init__(self, ticket_id, description, priority, status):
        self.ticket_id = ticket_id  # Unique ID for the ticket
        self.description = description  # Description of the issue
        self.priority = priority  # Priority of the ticket (e.g., High, Medium, Low)
        self.status = status  # Status of the ticket (e.g., Open, In Progress, Resolved)
        
class CircularQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size  # Initialize the queue with None
        self.front = 0  # Front pointer
        self.rear = -1  # Rear pointer
        self.size = 0  # Current size of the queue
        self.max_size = max_size  # Maximum size of the queue

    def enqueue(self, ticket_id, description, priority, status="Open"):
        if self.size == self.max_size:
            self.dequeue()  # Remove the oldest ticket if the queue is full
        self.rear = (self.rear + 1) % self.max_size  # Move rear to the next index (circular)
        self.queue[self.rear] = TicketNode(ticket_id, description, priority, status)
        self.size += 1
        return f"Ticket {ticket_id} added to the queue."

    def dequeue(self):
        if self.size == 0:
            return "Error: Queue is empty. No tickets to resolve."
        resolved_ticket = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size  # Move front pointer (circular)
        self.size -= 1
        return f"Ticket {resolved_ticket.ticket_id} resolved and removed from the queue."

    def display(self):
        if self.size == 0:
            return "No tickets in the queue."
        tickets = []
        i = self.front
        for _ in range(self.size):
            ticket = self.queue[i]
            tickets.append(f"Ticket ID: {ticket.ticket_id}, Description: {ticket.description}, Priority: {ticket.priority}, Status: {ticket.status}")
            i = (i + 1) % self.max_size  # Move to the next ticket (circular)
        return "\n".join(tickets)

class CustomerSupportSystem:
    def __init__(self, max_tickets):
        self.queue = CircularQueue(max_tickets)  # Initialize the circular queue

    def create_ticket(self, ticket_id, description, priority, status="Open"):
        return self.queue.enqueue(ticket_id, description, priority, status)

    def resolve_ticket(self):
        return self.queue.dequeue()

    def show_tickets(self):
        return self.queue.display()

# Example Usage
support_system = CustomerSupportSystem(max_tickets=3)

# Create tickets
print(support_system.create_ticket(101, "Unable to access the account", "High"))
print(support_system.create_ticket(102, "Page load time is slow", "Medium"))
print(support_system.create_ticket(103, "Error when submitting form", "Low"))

# Display all tickets in the queue
print("\nCurrent Tickets in Queue:")
print(support_system.show_tickets())

# Adding more tickets (this will overwrite the oldest ticket because the queue size is 3)
print(support_system.create_ticket(104, "Password reset issue", "High"))

# Display tickets after adding a new ticket (overwriting the oldest ticket)
print("\nTickets after adding Ticket 104 (Overwriting the oldest ticket):")
print(support_system.show_tickets())

# Resolve a ticket (dequeue)
print(support_system.resolve_ticket())

# Display tickets after resolving a ticket
print("\nTickets after resolving a ticket:")
print(support_system.show_tickets())

# Adding another ticket after resolving one
print(support_system.create_ticket(105, "User login error", "Medium"))

# Display tickets after adding another ticket
print("\nTickets after adding Ticket 105:")
print(support_system.show_tickets())
