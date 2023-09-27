# Pizza Restaurant API

This project is a Flask-based API for managing pizza restaurants. It allows you to create, read, update, and delete restaurant and pizza data. It also provides Swagger documentation for easy API testing.
# Prerequisites

Before you begin, ensure you have met the following requirements:

1. Python 3.x installed
2. pip package manager installed
3. Git (optional)

# Getting started

To get this project up and running,follow these steps:

# Installation

1. Clone this repository:

         git clone <repository_url>
2. Change into the project directory:

         cd pizza_restaurants
3. Create a virtual environment:

         python -m venv venv
4. Activate the virtual environment:

    . On macOS and Linux:

         source venv/bin/activate
   .  On Windows:

         venv\Scripts\activate
5. Install project dependencies:

         pip install -r requirements.txt

# Database setup

1. Initialize the database

        flask db init 
2. Create an initial migration:

         flask db migrate <initial migration>
3. Apply the initial migration:

         flask db upgrade

# API Endpoints

1. GET /restaurants: Get a list of all restaurants.
2. GET /restaurants/:id: Get details of a specific restaurant.
3. DELETE /restaurants/:id: Delete a specific restaurant.
4. GET /pizzas: Get a list of all pizzas.
5. POST /restaurant_pizzas: Create a new RestaurantPizza relationship.

# Swagger Documentation

The Swagger UI can be accessed by navigating to `/apidocs` in your web browser. Use Swagger for interactive API testing and documentation.

# Contributing

Contributions are what make the open-source community such an amazing place to be. Any contributions you make are greatly appreciated. Please follow the Contributor Covenant Code of Conduct.

# License

Distributed under the MIT License. See `LICENSE` for more information.