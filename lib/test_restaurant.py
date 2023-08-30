from restaurant import Restaurant
from customer import Customer
from review import Review

# Test Restaurant class
def test_restaurant_name():
    restaurant = Restaurant("Test Restaurant")
    assert restaurant.name() == "Test Restaurant"

def test_restaurant_average_star_rating_empty():
    restaurant = Restaurant("Empty Restaurant")
    assert restaurant.average_star_rating() == 0

# Test Customer class
def test_customer_given_name():
    customer = Customer("John", "Doe")
    assert customer.given_name() == "John"

def test_customer_full_name():
    customer = Customer("Jane", "Smith")
    assert customer.full_name() == "Jane Smith"

def test_customer_num_reviews():
    customer = Customer("Alice", "Johnson")
    restaurant = Restaurant("Test Restaurant")
    customer.add_review(restaurant, 4)
    assert customer.num_reviews() == 1

# Test Review class
def test_review_rating():
    customer = Customer("Bob", "Brown")
    restaurant = Restaurant("Test Restaurant")
    review = Review(customer, restaurant, 3)
    assert review.rating() == 3



if __name__ == "__main__":
    pytest.main()
