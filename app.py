from flask import Flask, render_template, request, redirect, url_for
from abc import ABC, abstractmethod

app = Flask(__name__)

#for storing customer and order details
customers = {}
orders = []

#abstract Pizza class and concrete pizzas
class Pizza(ABC):
    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._ham = None
        self._mushrooms = None
        self._meaty = []
        self._price = 0.0

    @abstractmethod
    def prepare(self):
        pass

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def __str__(self):
        result = f"---- {self._name} ----\n"
        if self._dough: result += f"{self._dough}\n"
        if self._sauce: result += f"{self._sauce}\n"
        if self._cheese: result += f"{self._cheese}\n"
        if self._veggies: result += ", ".join(self._veggies) + "\n"
        if self._ham: result += f"{self._ham}\n"
        if self._pepperoni: result += f"{self._pepperoni}\n"
        if self._mushrooms: result += f"{self._mushrooms}\n"
        if self._meaty: result += ", ".join(self._meaty) + "\n"
        if self._price: result += f"Price: kr{self._price:.2f}\n"
        return result

class IngredientFactory:
    def create_dough(self):
        return "Thin Crust Dough"

    def create_sauce(self):
        return "Tomato Sauce"

    def create_cheese(self):
        return "Mozzarella Cheese"

    def create_veggies(self):
        return ["Onions", "Bell Peppers", "Olives"]

    def create_pepperoni(self):
        return "Pepperoni"
    
    def create_mushrooms(self):
        return "Sliced Mushrooms"

    def create_ham(self):
        return "Sliced Ham"
    
    def create_meaty(self):
        return ["Bacon", "Beef", "Chicken"]

class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()

class PepperoniPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._pepperoni = self._ingredient_factory.create_pepperoni()

class HamPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._ham = self._ingredient_factory.create_ham()
        self._mushrooms = self._ingredient_factory.create_mushrooms()

class MeatyPizza(Pizza):
    def __init__(self, ingredient_factory):
        super().__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._ham = self._ingredient_factory.create_ham()
        self._mushrooms = self._ingredient_factory.create_mushrooms()
        self._meaty = self._ingredient_factory.create_meaty()
        self._veggies = self._ingredient_factory.create_veggies()

@app.route("/", methods=["GET", "POST"])
def home():
    ingredient_factory = IngredientFactory()

    if request.method == "POST":
        name = request.form.get("name")
        contact = request.form.get("contact")
        pizza_types = request.form.getlist("pizza_type[]")
        quantities = request.form.getlist("quantity[]")

        if not name or not contact or not pizza_types or not quantities:
            return "Missing data!", 400

        pizza_classes = {
            "Cheese": (CheesePizza, "Cheese Pizza", 198.00),
            "Pepperoni": (PepperoniPizza, "Pepperoni Pizza", 298.99),
            "Ham": (HamPizza, "Ham Pizza", 298.00),
            "Meaty": (MeatyPizza, "Meaty Pizza", 365.00),
        }

        total_order_price = 0
        order_details = []

        for p_type, qty_str in zip(pizza_types, quantities):
            qty = int(qty_str)
            pizza_info = pizza_classes.get(p_type)
            if not pizza_info:
                return "Invalid pizza type!", 400

            pizza_class, pizza_name, pizza_price = pizza_info
            pizza = pizza_class(ingredient_factory)
            pizza.set_name(pizza_name)
            pizza.set_price(pizza_price)
            pizza.prepare()

            line_total = pizza_price * qty
            total_order_price += line_total
            order_details.append(f"{qty} x {pizza_name} (kr{line_total:.2f})\n {pizza}")

        full_description = "\n".join(order_details)

        # Instead of redirecting, we have the order summary on the same page
        order_summary = {
            "name": name,
            "contact": contact,
            "description": full_description,
            "price": f"kr{total_order_price:.2f}",
        }

        return render_template("home.html", order=order_summary)

    return render_template("home.html", order=None)


@app.route("/order_summary/<contact>")
def order_summary(contact):
    order = next((order for order in orders if order["contact"] == contact), None)
    if order:
        return render_template("order_summary.html", order=order)
    else:
        return "Order not found", 404

if __name__ == "__main__":
    app.run(debug=True)
