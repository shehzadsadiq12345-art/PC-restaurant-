from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to PC Restaurant Lahore 🍽️"

# Menu route
@app.route("/menu")
def menu():
    return {
        "BBQ": "Chicken Tikka, Seekh Kebab",
        "Fast Food": "Zinger Burger, Fries",
        "Desi": "Chicken Karahi, Biryani"
    }

# Contact route
@app.route("/contact")
def contact():
    return {
        "phone": "03217371673",
        "location": "Lahore, Pakistan"
    }

if __name__ == "__main__":
    app.run(debug=True)