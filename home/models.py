from home import db


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', backref='pizza', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
        }


class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
