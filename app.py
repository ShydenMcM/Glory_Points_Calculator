import math
# Import the Flask object from the flask package
from flask import Flask, render_template, request
from werkzeug.middleware.proxy_fix import ProxyFix

# Create an instance of the Flask class
app = Flask(__name__)
# app = ProxyFix(app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Define a route for the home page ("/")
@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize variables for the result and any errors
    coins_needed = None
    beans_needed = None
    total_gift_value = None
    error = None

    # Check if the user submitted a form (POST request)
    if request.method == "POST":
        user_input = request.form.get("user_input")

        # Validate that the input is a number
        if user_input:
            try:
                # Cast the input to a float to do a calculation
                coins_needed = int(user_input)

                # Perform your script's core logic here
                beans_needed, total_gift_value = calculate_gift_value(coins_needed)

            except ValueError:
                # Handle cases where the input is not a valid number
                error = "Please enter a valid number."
        else:
            error = "Input cannot be empty."

    return render_template("index.html", coins_needed=coins_needed, beans_needed=beans_needed,
                           total_gift_value=total_gift_value, error=error)


def calculate_gift_value(points_required: int = 0):
    """
    Calculates the total value of gifts needed based on a required number of points.
    """
    # try:
    #     points_required = int(input("Enter the number of points required: "))
    # except ValueError:
    #     print("Invalid input. Please enter a whole number.")
    #     return

    # Constants from the problem
    COINS_PER_POINT = 1
    BEANS_PER_COIN = 0.9
    BEANS_FROM_GIFT_RATE = 0.40  # 40%

    # Calculate coins needed
    coins_needed = math.ceil(points_required * COINS_PER_POINT)

    # Calculate beans needed
    beans_needed = math.ceil(coins_needed / BEANS_PER_COIN)

    # Calculate total gift value needed
    total_gift_value = math.ceil(beans_needed / BEANS_FROM_GIFT_RATE)

    print(f"To get {points_required:,.0f} glory points, you need {coins_needed:,.0f} coins")
    print(f"To get {coins_needed:,.0f} coins, you need: {beans_needed:,.0f} beans")
    print(f"To get {beans_needed:,.0f} beans, you need: {total_gift_value:,.0f} in total gift value")

    return beans_needed, total_gift_value


# Run the function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
    # while True:
    # calculate_gift_value()
    # will_end = input("Do you want to continue? [Y/N]: ")
    # while will_end.lower() != "y" and will_end.lower() != "n":
    #     print("Invalid input. Please enter Y or N.")
    #     will_end = input("Do you want to continue? [Y/N]: ")
    # if will_end.lower() == "n":
    #     print("Thank you for using Glory Points Calculator")
    # break
