from restaurant import Restaurant
from customer import Customer
from review import Review

# Create instances
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)

# Test methods
print(restaurant1.average_star_rating())
print(customer1.num_reviews())
print(Customer.find_by_name("John Doe"))
print(Customer.find_all_by_given_name("Jane"))

# ... more test cases
