import math


def calculate_gift_value():
    """
    Calculates the total value of gifts needed based on a required number of points.
    """
    try:
        points_required = int(input("Enter the number of points required: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

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

# Run the function
calculate_gift_value()
'''

How the script works

1.  **Request user input:** The `input()` function prompts the user to enter the number of points required.
2.  **Validate input:** A `try-except` block handles potential `ValueError` exceptions if the user enters non-integer text, ensuring the program doesn't crash.
3.  **Define constants:** The script sets the conversion rates for coins per point, beans per coin, and the percentage of gift value converted to beans.
4.  **Perform calculations:**
    *   `coins_needed`: Calculates the number of coins required based on the input points.
    *   `beans_needed`: Calculates the number of beans required to get the necessary coins.
    *   `total_gift_value`: Calculates the total value of gifts needed by dividing the required beans by the bean earning rate.
5.  **Display the result:** The script prints a user-friendly message with the final calculated gift value, formatted to two decimal places.
'''