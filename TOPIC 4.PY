import heapq

class FixedOrderHeap:
    """A Heap to manage a fixed number of orders."""
    def __init__(self, max_size):
        self.heap = []
        self.max_size = max_size

    def add_order(self, order):
        """Add a new order to the heap."""
        if len(self.heap) < self.max_size:
            heapq.heappush(self.heap, order)
        else:
            # If the heap is full, replace the smallest element if the new order is larger
            heapq.heappushpop(self.heap, order)

    def get_orders(self):
        """Get all orders in sorted order."""
        return sorted(self.heap, reverse=True)

    def display_heap(self):
        """Display the current heap structure."""
        print("Current Orders in Heap:", self.heap)

# Example usage for a personalized gift recommendation system
if __name__ == "__main__":
    max_orders = 5
    order_heap = FixedOrderHeap(max_orders)

    # Adding orders to the heap
    order_heap.add_order((50, "Order1: Custom Mug"))
    order_heap.add_order((30, "Order2: Smartwatch"))
    order_heap.add_order((20, "Order3: Photo Book"))
    order_heap.add_order((40, "Order4: Wireless Earbuds"))
    order_heap.add_order((60, "Order5: Personalized Keychain"))

    # Display the heap
    print("Heap after adding initial orders:")
    order_heap.display_heap()

    # Adding a new order that exceeds the smallest order
    print("\nAdding a higher priority order:")
    order_heap.add_order((70, "Order6: Luxury Pen"))
    order_heap.display_heap()

    # Retrieving all orders in sorted order
    print("\nSorted Orders:")
    for priority, order in order_heap.get_orders():
        print(f"Priority {priority}: {order}")