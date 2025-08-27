```

### How the script works

1.  **Request user input:** The `input()` function prompts the user to enter the number of points required.
2.  **Validate input:** A `try-except` block handles potential `ValueError` exceptions if the user enters non-integer text, ensuring the program doesn't crash.
3.  **Define constants:** The script sets the conversion rates for coins per point, beans per coin, and the percentage of gift value converted to beans.
4.  **Perform calculations:**
    *   `coins_needed`: Calculates the number of coins required based on the input points.
    *   `beans_needed`: Calculates the number of beans required to get the necessary coins.
    *   `total_gift_value`: Calculates the total value of gifts needed by dividing the required beans by the bean earning rate.
5.  **Display the result:** The script prints a user-friendly message with the final calculated gift value, formatted to two decimal places.