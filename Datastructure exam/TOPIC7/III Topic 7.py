class Ticket:
    def __init__(self, ticket_id, customer_name, issue_description, status, priority):
        self.ticket_id = ticket_id  # Unique ticket ID
        self.customer_name = customer_name  # Customer's name
        self.issue_description = issue_description  # Description of the issue
        self.status = status  # Status of the ticket (Open, Closed, etc.)
        self.priority = priority  # Priority of the ticket (lower number = higher priority)

    def __repr__(self):
        return f"Ticket ID: {self.ticket_id}, Customer: {self.customer_name}, Issue: {self.issue_description}, Status: {self.status}, Priority: {self.priority}"


class HeapSort:
    def __init__(self, tickets):
        self.tickets = tickets

    # Helper function to perform the heapify operation
    def heapify(self, n, i):
        smallest = i  # Assume the current node is the smallest
        left = 2 * i + 1  # Left child
        right = 2 * i + 2  # Right child

        # Check if left child exists and is smaller than root
        if left < n and self.tickets[left].priority < self.tickets[smallest].priority:
            smallest = left

        # Check if right child exists and is smaller than the smallest so far
        if right < n and self.tickets[right].priority < self.tickets[smallest].priority:
            smallest = right

        # If smallest is not the root, swap and continue heapifying
        if smallest != i:
            self.tickets[i], self.tickets[smallest] = self.tickets[smallest], self.tickets[i]
            self.heapify(n, smallest)

    # Function to perform heap sort
    def heap_sort(self):
        n = len(self.tickets)

        # Build a min-heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            self.tickets[i], self.tickets[0] = self.tickets[0], self.tickets[i]  # Swap
            self.heapify(i, 0)  # Heapify the root element

    def display_sorted_tickets(self):
        print("\nSorted Tickets Based on Priority:")
        for ticket in self.tickets:
            print(ticket)


# Example Usage:

# Create a list of tickets with varying priorities
tickets = [
    Ticket(1, "Nziza", "Login issue", "Open", 3),
    Ticket(2, "Ben", "Payment issue", "Open", 1),
    Ticket(3, "Celine", "Account suspension", "Closed", 2),
    Ticket(4, "Didie", "Profile update", "Open", 4),
    Ticket(5, "Alexia", "Password reset", "Open", 5)
]

# Create a HeapSort instance
heap_sort = HeapSort(tickets)

# Display unsorted tickets
print("Unsorted Tickets:")
for ticket in tickets:
    print(ticket)

# Sort the tickets based on priority
heap_sort.heap_sort()

# Display the sorted tickets
heap_sort.display_sorted_tickets()
