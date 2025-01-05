from collections import deque
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

class OrderQueue:
    """A Queue to dynamically track orders."""
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        """Add a new order to the queue."""
        self.queue.append(order)

    def dequeue(self):
        """Remove and return the oldest order from the queue."""
        if self.queue:
            return self.queue.popleft()
        else:
            print("Queue is empty.")
            return None

    def display_queue(self):
        """Display all orders in the queue."""
        print("Current Orders in Queue:", list(self.queue))

class GiftCategoryTree:
    """A Tree to represent hierarchical gift categories."""
    class TreeNode:
        """A node in the GiftCategoryTree."""
        def __init__(self, category):
            self.category = category
            self.subcategories = []

        def add_subcategory(self, subcategory):
            """Add a subcategory to this node."""
            self.subcategories.append(subcategory)

    def __init__(self):
        self.root = self.TreeNode("Gifts")

    def add_category(self, parent_category, category):
        """Add a new category under the specified parent category."""
        parent_node = self.find_category(self.root, parent_category)
        if parent_node:
            parent_node.add_subcategory(self.TreeNode(category))
        else:
            print(f"Parent category '{parent_category}' not found.")

    def find_category(self, node, category):
        """Find a category in the tree starting from the given node."""
        if node.category == category:
            return node
        for subcategory in node.subcategories:
            result = self.find_category(subcategory, category)
            if result:
                return result
        return None

    def display_tree(self, node=None, level=0):
        """Display the hierarchical structure of the tree."""
        if node is None:
            node = self.root
        print("  " * level + node.category)
        for subcategory in node.subcategories:
            self.display_tree(subcategory, level + 1)

class InsertionSorter:
    """A class to sort data using Insertion Sort."""
    @staticmethod
    def insertion_sort(data):
        """Sort the data based on priority using insertion sort."""
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j][0] < key[0]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

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

    # Using the OrderQueue
    print("\nUsing the Order Queue:")
    order_queue = OrderQueue()
    order_queue.enqueue("Order1: Custom Mug")
    order_queue.enqueue("Order2: Smartwatch")
    order_queue.enqueue("Order3: Photo Book")

    # Display the queue
    order_queue.display_queue()

    # Dequeue an order
    print("\nDequeued Order:", order_queue.dequeue())
    order_queue.display_queue()

    # Using the GiftCategoryTree
    print("\nUsing the Gift Category Tree:")
    category_tree = GiftCategoryTree()
    category_tree.add_category("Gifts", "Electronics")
    category_tree.add_category("Gifts", "Personalized Items")
    category_tree.add_category("Electronics", "Smartwatches")
    category_tree.add_category("Personalized Items", "Photo Books")
    category_tree.display_tree()

    # Sorting orders using InsertionSort
    print("\nSorting orders using Insertion Sort:")
    orders = [
        (50, "Order1: Custom Mug"),
        (30, "Order2: Smartwatch"),
        (20, "Order3: Photo Book"),
        (40, "Order4: Wireless Earbuds"),
        (60, "Order5: Personalized Keychain")
    ]
    sorted_orders = InsertionSorter.insertion_sort(orders)
    for priority, order in sorted_orders:
        print(f"Priority {priority}: {order}")