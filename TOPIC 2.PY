from dataclasses import dataclass
from typing import Optional, List, Set
from datetime import datetime

@dataclass
class Gift:
    id: int
    name: str
    category: str
    price: float
    rating: float
    tags: Set[str]
    stock: int

class CircularNode:
    def __init__(self, gift: Gift):
        self.gift = gift
        self.next: Optional[CircularNode] = None
        self.prev: Optional[CircularNode] = None

class BSTNode:
    def __init__(self, gift: Gift):
        self.gift = gift
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None
        self.height = 1

class CircularGiftList:
    def __init__(self):
        self.head: Optional[CircularNode] = None
        self.size = 0

    def add_gift(self, gift: Gift) -> None:
        """Add a new gift to the circular linked list."""
        new_node = CircularNode(gift)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
        
        self.size += 1

    def remove_gift(self, gift_id: int) -> Optional[Gift]:
        """Remove a gift from the circular linked list."""
        if not self.head:
            return None

        current = self.head
        for _ in range(self.size):
            if current.gift.id == gift_id:
                # Update links
                current.prev.next = current.next
                current.next.prev = current.prev
                
                # If removing head, update head
                if current == self.head:
                    self.head = current.next if self.size > 1 else None
                
                self.size -= 1
                return current.gift
            current = current.next
            
        return None

    def get_recommendations(self, count: int, category: Optional[str] = None) -> List[Gift]:
        """Get gift recommendations, optionally filtered by category."""
        if not self.head or count <= 0:
            return []

        recommendations = []
        current = self.head
        seen_ids = set()

        while len(recommendations) < count and len(seen_ids) < self.size:
            if current.gift.id not in seen_ids and \
               (category is None or current.gift.category == category):
                recommendations.append(current.gift)
            seen_ids.add(current.gift.id)
            current = current.next

        return recommendations

class GiftBST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def get_height(self, node: Optional[BSTNode]) -> int:
        """Get height of a node."""
        return node.height if node else 0

    def get_balance(self, node: Optional[BSTNode]) -> int:
        """Get balance factor of a node."""
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y: BSTNode) -> BSTNode:
        """Perform right rotation."""
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def rotate_left(self, x: BSTNode) -> BSTNode:
        """Perform left rotation."""
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    def insert(self, gift: Gift) -> None:
        """Insert a new gift into the BST."""
        def _insert(root: Optional[BSTNode], gift: Gift) -> BSTNode:
            if not root:
                return BSTNode(gift)

            if gift.price < root.gift.price:
                root.left = _insert(root.left, gift)
            else:
                root.right = _insert(root.right, gift)

            root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

            balance = self.get_balance(root)

            # Left Left
            if balance > 1 and gift.price < root.left.gift.price:
                return self.rotate_right(root)

            # Right Right
            if balance < -1 and gift.price > root.right.gift.price:
                return self.rotate_left(root)

            # Left Right
            if balance > 1 and gift.price > root.left.gift.price:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

            # Right Left
            if balance < -1 and gift.price < root.right.gift.price:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

            return root

        self.root = _insert(self.root, gift)

    def find_in_price_range(self, min_price: float, max_price: float) -> List[Gift]:
        """Find gifts within a specific price range."""
        results = []
        
        def _search(node: Optional[BSTNode]) -> None:
            if not node:
                return
                
            if min_price <= node.gift.price <= max_price:
                results.append(node.gift)
                
            if node.gift.price > min_price:
                _search(node.left)
            if node.gift.price < max_price:
                _search(node.right)

        _search(self.root)
        return results

class GiftRecommendationSystem:
    def __init__(self):
        self.circular_list = CircularGiftList()
        self.price_bst = GiftBST()
        self.gift_count = 0

    def add_gift(self, name: str, category: str, price: float, rating: float, 
                 tags: Set[str], stock: int) -> Gift:
        """Add a new gift to both data structures."""
        self.gift_count += 1
        gift = Gift(
            id=self.gift_count,
            name=name,
            category=category,
            price=price,
            rating=rating,
            tags=tags,
            stock=stock
        )
        
        self.circular_list.add_gift(gift)
        self.price_bst.insert(gift)
        return gift

    def get_recommendations(self, count: int, category: Optional[str] = None,
                          min_price: Optional[float] = None,
                          max_price: Optional[float] = None) -> List[Gift]:
        """Get gift recommendations based on various criteria."""
        recommendations = []
        
        if min_price is not None and max_price is not None:
            # Use BST for price-based search
            recommendations = self.price_bst.find_in_price_range(min_price, max_price)
            if category:
                recommendations = [g for g in recommendations if g.category == category]
        else:
            # Use circular list for general recommendations
            recommendations = self.circular_list.get_recommendations(count, category)
            
        # Sort by rating and return top results
        recommendations.sort(key=lambda x: x.rating, reverse=True)
        return recommendations[:count]

# Example usage and testing
def main():
    # Initialize system
    system = GiftRecommendationSystem()
    
    # Add sample gifts
    gifts_data = [
        ("Smart Watch", "Electronics", 199.99, 4.5, {"tech", "wearable"}, 10),
        ("Coffee Maker", "Kitchen", 49.99, 4.2, {"appliance", "coffee"}, 15),
        ("Book Set", "Books", 29.99, 4.8, {"reading", "collection"}, 20),
        ("Gaming Console", "Electronics", 299.99, 4.7, {"tech", "gaming"}, 5),
        ("Jewelry Box", "Accessories", 79.99, 4.0, {"storage", "decoration"}, 12)
    ]
    
    for name, category, price, rating, tags, stock in gifts_data:
        system.add_gift(name, category, price, rating, tags, stock)
    
    # Get recommendations
    print("\nGeneral Recommendations (top 3):")
    for gift in system.get_recommendations(3):
        print(f"{gift.name} - ${gift.price:.2f} - Rating: {gift.rating}")
    
    print("\nElectronics under $250:")
    for gift in system.get_recommendations(5, "Electronics", 0, 250):
        print(f"{gift.name} - ${gift.price:.2f} - Rating: {gift.rating}")

if __name__ == "__main__":
    main()