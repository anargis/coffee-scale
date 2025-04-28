from machine import Pin, I2C
import time
import ssd1306
from hx711 import HX711

# I2C pins for OLED (SDA = GP4, SCL = GP5)
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Load Cell pins (DT = GP16, SCK = GP17)
dt_pin = Pin(16, Pin.IN)
sck_pin = Pin(17, Pin.OUT)

# Initialize HX711
hx = HX711(dout=dt_pin, pd_sck=sck_pin)

# Setup HX711 (set scale and offset)
hx.set_scale(192)  # Adjust this value based on calibration
hx.tare()  # Reset scale to 0

# Function to display weight on OLED
def display_weight(weight):
    oled.fill(0)  # Clear the display
    oled.text("Coffee Scale:", 0, 10)
    oled.text(f"{weight:.2f} kg", 0, 30)
    oled.show()

# Main loop
while True:
    weight = hx.get_weight(5)  # Read weight in grams
    weight_kg = weight / 1000  # Convert grams to kilograms

    print(f"Weight: {weight_kg:.2f} kg")  # Print weight in terminal
    display_weight(weight_kg)  # Display weight on OLED

    time.sleep(1)  # Update every second
