from flask import request
from flask_restful import Resource
from home import api, db
from home.models import Restaurant, Pizza, RestaurantPizza
from flasgger import swag_from


class RestaurantResource(Resource):
    @swag_from('swagger/restaurant_get.yml')
    def get(self, restaurant_id=None):
        if restaurant_id:
            restaurant = Restaurant.query.get(restaurant_id)
            if restaurant:
                pizzas = [rp.pizza.serialize() for rp in restaurant.restaurant_pizzas]
                return {'restaurant': restaurant.serialize(), 'pizzas': pizzas}
            return {'error': 'Restaurant not found'}, 404
        else:
            restaurants = [r.serialize() for r in Restaurant.query.all()]
            return {'restaurants': restaurants}

    @swag_from('swagger/restaurant_delete.yml')
    def delete(self, restaurant_id):
        restaurant = Restaurant.query.get(restaurant_id)
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        return {'error': 'Restaurant not found'}, 404


class PizzaResource(Resource):
    @swag_from('swagger/pizzas_get.yml')
    def get(self):
        pizzas = [p.serialize() for p in Pizza.query.all()]
        return {'pizzas': pizzas}


class RestaurantPizzaResource(Resource):
    @swag_from('swagger/restaurant_pizzas_post.yml')
    def post(self):
        data = request.get_json()
        price = data.get('price')
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        if not (price and pizza_id and restaurant_id):
            return {'errors': ['Missing data']}, 400

        if not 1 <= price <= 30:
            return {'errors': ['Price must be between 1 and 30']}, 400

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        if not (pizza and restaurant):
            return {'errors': ['Pizza or restaurant not found']}, 404

        restaurant_pizza = RestaurantPizza(price=price, restaurant=restaurant, pizza=pizza)
        db.session.add(restaurant_pizza)
        db.session.commit()

        return pizza.serialize(), 201


api.add_resource(RestaurantResource, '/restaurants', '/restaurants/<int:restaurant_id>')
api.add_resource(PizzaResource, '/pizzas')
api.add_resource(RestaurantPizzaResource, '/restaurant_pizzas')
