Object Relations Code Challenge - Restaurants
Problem Statement
This project aims to create a system for managing restaurant reviews. We have three main models: Restaurant, Customer, and Review. A Restaurant can have multiple Reviews, a Customer can write multiple Reviews, and each Review belongs to both a Restaurant and a Customer. The goal is to implement methods that allow us to manage and analyze these relationships.

Project Structure
The project is organized into three classes: Restaurant, Customer, and Review, each of which resides in its own Python file. These classes are defined as follows:

Restaurant: Represents a restaurant and includes methods to retrieve its name and average star rating.

Customer: Represents a customer and includes methods for managing their information and reviews.

Review: Represents a review, including the customer who wrote it, the restaurant it's about, and the rating.

The project structure looks like this:

project-folder/
├── customer.py
├── restaurant.py
├── review.py
└── main.py (for testing and interaction)
Clone the Project
To clone this project to your local machine, follow these steps:

Open a terminal and navigate to the directory where you want to clone the project.

Run the following command:

git clone https://github.com/your-username/restaurant-reviews.git
Replace your-username with your GitHub username.

Once the cloning is complete, navigate to the project folder:

cd restaurant-reviews
Installing Dependencies
Before you can run the project, you need to install its dependencies. We use Pipenv for managing dependencies. If you don't have Pipenv installed, you can install it with the following command (assuming you have Python 3.10 installed):

pip install pipenv
Once Pipenv is installed, navigate to the project folder and run:

pipenv install
This command will read the Pipfile and install the required packages, including ipdb for debugging (if not already installed).

Getting Started
To start using the project, open a Python shell or a code editor of your choice and create instances of Restaurant, Customer, and Review. You can then use the provided methods to interact with the data and relationships between them.

For example:

python
Copy code
from customer import Customer
from restaurant import Restaurant
from review import Review

# Create instances of Customer and Restaurant

customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Delicious Delights")

# Add a review by the customer for the restaurant

customer1.add_review(restaurant1, 4)

# Retrieve the average star rating for the restaurant

avg_rating = restaurant1.average_star_rating()
print(f"Average Rating for {restaurant1.name()}: {avg_rating}")
Contributing
If you would like to contribute to this project, please fork the repository, make your changes, and create a pull request. We welcome any improvements or additional features that align with the project's goals.

License
This project is licensed under the MIT License. See the LICENSE file for details.
