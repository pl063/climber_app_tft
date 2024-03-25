import board
import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
 
# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
 
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)
 
# Define the analog input channel
channel = AnalogIn(ads, ADS.P0)
treshhold = 29600


# Loop to read the analog input continuously
while True:
    channel_value = channel.value
    print(channel_value)
    if(channel_value < treshhold):
        print("DARK")
    else:
        print("LIGHT")
    time.sleep(1)