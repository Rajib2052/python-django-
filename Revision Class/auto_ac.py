# Simulated temperature sensor function
def get_temperature():
    # For this example, we'll return a constant value
    # Replace this with actual code to get temperature from a sensor
    return 30

# Function to turn on the AC
def turn_on_ac():
    print("AC is now ON")

# Main loop to check temperature and control AC
while True:
    # Get the current temperature
    current_temperature = get_temperature()

    # Check if the temperature is 30 or higher
    if current_temperature >= 30:
        turn_on_ac()
        break  # Exit the loop after turning on the AC

# After the loop ends
print("Temperature has reached 30 or more. AC is turned on.")
