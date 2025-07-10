from app import app, db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    restaurant1 = Restaurant(name="Karen's Pizza Shack", address="address1")
    restaurant2 = Restaurant(name="Sanjay's Pizza", address="address2")
    restaurant3 = Restaurant(name="Kiki's Pizza", address="address3")

    db.session.add_all([restaurant1, restaurant2, restaurant3])

    # Seed Pizzas
    pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

    db.session.add_all([pizza1, pizza2, pizza3])

    # Seed RestaurantPizzas
    restaurant_pizza1 = RestaurantPizza(price=10, restaurant=restaurant1, pizza=pizza1)
    restaurant_pizza2 = RestaurantPizza(price=15, restaurant=restaurant2, pizza=pizza2)
    restaurant_pizza3 = RestaurantPizza(price=20, restaurant=restaurant3, pizza=pizza3)

    db.session.add_all([restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])

    db.session.commit()
