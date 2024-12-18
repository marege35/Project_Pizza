# Pizza Ordering System

This is a web application that allows customers to easily build their perfect pizza from a variety of options. 

Customers can order multiple pizza in a single session. 
It dynamically calculates prices, and shows a summary of the customer’s order.

## Features

- **OOP-Driven Design**:  
  Each pizza type (Cheese, Pepperoni, Ham, Meaty) inherits from a common `Pizza` abstract class, ensuring a consistent interface and easy extensibility.
  
  - **Abstract Base Class (`Pizza`)**: Defines the template for all pizzas with attributes like dough, sauce, cheese, veggies, and meats, as well as an abstract `prepare()` method that subclasses must implement.
  - **Ingredient Factory (`IngredientFactory`)**: The creation of all ingredients. This makes it easy to extend or modify.

  Customers can add multiple pizza lines, selecting the type and quantity. The OOP structure ensures each pizza instance is created, prepared, and priced through a standardized process.

- **Price Calculation**:  
  JavaScript updates pizza totals and the overall total price as the customer's change pizza types or change quantities.

- **Flexible and Extensible**:  
  Thanks to the OOP design, adding a new pizza or changing ingredient is straightforward. Just add a new subclass of `Pizza` or modify the `IngredientFactory` without altering the rest of the system.


## Technologies Used

Python 3 for app.py.. Then Flask For the web server and routing because of the use of python.
HTML/CSS for making the app, as well as JavaScript for dynamic price updates, adding new order lines, and improving the user experience.


## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-pizza-repo.git
   cd your-pizza-repo
   ```

2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   If you don’t have a `requirements.txt`, run:
   ```bash
   pip install flask
   ```
   
   and any other packages you need.

4. **Run the Application**:
   ```bash
   python app.py
   ```
   
   By default, the Flask development server runs at `http://127.0.0.1:5000`.

5. **Open in Browser**:
   Go to `http://127.0.0.1:5000` in your web browser to see the Pizza Ordering System.

## Usage

- **Home Page**:  
  The home page lets you input your name, contact number, and select pizzas. By default, one pizza line is shown.

- **Add More Pizzas**:  
  Click the `+ Add Another Pizza` button to add a new line for selecting another pizza type and quantity. The total price updates instantly.

- **Ordering**:  
  When you are done selecting the pizza you want, click **Order Now**. The system will display your order summary right beside the order form.

- **Order Summary**:  
  The summary shows each selected pizza, its quantity, price details, and the grand total.

## For modertation:

- **Add More Pizza Types**:  
  In `app.py`, update the `pizza_classes` dictionary and `IngredientFactory` methods to add new pizza types or ingredients.
  
- **Change Prices**:  
  Adjust the `pizza_classes` dictionary to set new prices for each pizza type.

- **Styling and Layout**:  
  Modify `style.css` or the templates to customize the look and feel of the website.

## Troubleshooting

- **Server Errors**:  
  Check the Flask console output for detailed error messages. Ensure all required fields are included before submitting the form.

## License

This project is available under the [MIT License](./License.txt). You may modify and distribute this project as long as you comply with the license terms.