class GiftNode:
    def __init__(self, item_name, price, category, recipient_age):
        self.item_name = item_name
        self.price = price
        self.category = category
        self.recipient_age = recipient_age
        self.next = None

class GiftRecommendationSystem:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head is None
    
    def add_gift(self, item_name, price, category, recipient_age):
        """Add a new gift recommendation to the system"""
        new_node = GiftNode(item_name, price, category, recipient_age)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        
        self.size += 1
        return f"Added {item_name} to recommendations"
    
    def remove_gift(self, item_name):
        """Remove a gift recommendation from the system"""
        if self.is_empty():
            return "List is empty"
        
        # If head node is to be removed
        if self.head.item_name == item_name:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            return f"Removed {item_name} from recommendations"
        
        # Remove node from middle or end
        current = self.head
        prev = None
        while current.next != self.head:
            if current.item_name == item_name:
                prev.next = current.next
                self.size -= 1
                return f"Removed {item_name} from recommendations"
            prev = current
            current = current.next
            
        # Check last node
        if current.item_name == item_name:
            prev.next = self.head
            self.size -= 1
            return f"Removed {item_name} from recommendations"
            
        return "Gift not found"
    
    def get_recommendations_by_price(self, max_price):
        """Get all gift recommendations within the specified price range"""
        if self.is_empty():
            return []
        
        recommendations = []
        current = self.head
        
        while True:
            if current.price <= max_price:
                recommendations.append({
                    'item_name': current.item_name,
                    'price': current.price,
                    'category': current.category,
                    'recipient_age': current.recipient_age
                })
            current = current.next
            if current == self.head:
                break
                
        return recommendations
    
    def get_recommendations_by_category(self, category):
        """Get all gift recommendations in a specific category"""
        if self.is_empty():
            return []
        
        recommendations = []
        current = self.head
        
        while True:
            if current.category.lower() == category.lower():
                recommendations.append({
                    'item_name': current.item_name,
                    'price': current.price,
                    'category': current.category,
                    'recipient_age': current.recipient_age
                })
            current = current.next
            if current == self.head:
                break
                
        return recommendations
    
    def get_age_appropriate_gifts(self, age):
        """Get gifts appropriate for a specific age"""
        if self.is_empty():
            return []
        
        recommendations = []
        current = self.head
        
        while True:
            # Consider gifts within a 2-year range of the target age
            if abs(current.recipient_age - age) <= 2:
                recommendations.append({
                    'item_name': current.item_name,
                    'price': current.price,
                    'category': current.category,
                    'recipient_age': current.recipient_age
                })
            current = current.next
            if current == self.head:
                break
                
        return recommendations
    
    def display_all_gifts(self):
        """Display all gifts in the system"""
        if self.is_empty():
            return "No gifts in the system"
        
        gifts = []
        current = self.head
        
        while True:
            gifts.append({
                'item_name': current.item_name,
                'price': current.price,
                'category': current.category,
                'recipient_age': current.recipient_age
            })
            current = current.next
            if current == self.head:
                break
                
        return gifts

# Example usage
def demo_gift_system():
    gift_system = GiftRecommendationSystem()
    
    # Adding sample gifts
    gift_system.add_gift("LEGO Set", 29.99, "Toys", 8)
    gift_system.add_gift("Science Kit", 39.99, "Educational", 10)
    gift_system.add_gift("Art Supplies", 24.99, "Crafts", 7)
    gift_system.add_gift("Board Game", 19.99, "Games", 9)
    gift_system.add_gift("Robot Kit", 49.99, "Educational", 11)
    
    # Get recommendations by price
    budget_gifts = gift_system.get_recommendations_by_price(30.00)
    print("\nGifts under $30:")
    for gift in budget_gifts:
        print(f"- {gift['item_name']} (${gift['price']})")
    
    # Get recommendations by category
    educational_gifts = gift_system.get_recommendations_by_category("Educational")
    print("\nEducational gifts:")
    for gift in educational_gifts:
        print(f"- {gift['item_name']} (${gift['price']})")
    
    # Get age-appropriate gifts
    age_appropriate = gift_system.get_age_appropriate_gifts(9)
    print("\nGifts appropriate for age 9:")
    for gift in age_appropriate:
        print(f"- {gift['item_name']} (Age: {gift['recipient_age']})")
    
    return gift_system

if __name__ == "__main__":
    demo_gift_system()