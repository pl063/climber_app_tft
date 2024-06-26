import digitalio
import board
import RPi.GPIO as GPIO
import os
import sys
from time import sleep
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from setup import Display
from start_screen import start_screen
from timer import timer_screen
from stamp_screen import stamp_screen

GPIO.setmode(GPIO.BCM)  

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D27) #GPIO 27
reset_pin = digitalio.DigitalInOut(board.D17) #GPIO 17

# Initialize adc
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
# Define the analog input channel
transistor_channels = [AnalogIn(ads, ADS.P0), AnalogIn(ads, ADS.P1), AnalogIn(ads, ADS.P2)]

treshhold = 20000 #treshhold value for phototransistors
button_flags = [False] #switch button function from start to reset 

#display settings
baudrate = 24000000
border = 20
fontsize = 21
pins = [cs_pin, dc_pin, reset_pin] 


button_channel = AnalogIn(ads, ADS.P3)
button_vcc = 19 #use gpio for 3.3v
adc_vdd = 21
GPIO.setup(adc_vdd, GPIO.OUT)
GPIO.setup(button_vcc, GPIO.OUT)
GPIO.output(button_vcc, GPIO.HIGH)
GPIO.output(adc_vdd, GPIO.HIGH)


stamp_arr = []
time_str = "0:0"
index_tran = [0]
is_finished_flags = [False]



disp = Display(pins, baudrate, fontsize, border)

if disp._disp_setting.rotation % 180 == 90:
    height = disp._disp_setting.height  
    width = disp._disp_setting.width



def read_transistors():
    result = 0
    
    try:   
        current_trace_key = transistor_channels[index_tran[0]]
        current_value = current_trace_key.value
        result = current_value


        #print("INDEX " + str(index_tran[0]))
        print(result)
        #print(current_trace_key)
       # print(index_tran[0])
      #  print(current_value)


        if(current_value < treshhold):
             index_tran[0] += 1

        
    except :
        print("Error occured with indeces - probe finished")
        is_finished_flags.append(True)
        pass

    return result
 

def tick():
   
    counter_arr= ["0", "0"] 
    counter_text = ":".join(counter_arr)

    flags = [False]
    flags_transistors = [False]
  
    #tick timer
    while True:
        #clean flags, initiate anew
      
        flags.clear()
        flags.append(False)

       
        tran_value = read_transistors()

        #change display images according to transistors' values
        if (flags_transistors[len(flags_transistors) - 1]): 
              image = stamp_screen(fontsize, stamp_arr,  counter_text)
        else:
           image = timer_screen(fontsize, counter_text, flags)
       
        disp._disp_setting.image(image)
        #time counter``
        next_counter = int(counter_arr[1]) + 1
        if(next_counter >= 60):
            counter_arr[0] = str(int(counter_arr[0]) + 1)
            counter_arr[1] = str(next_counter - 60)
        else:
            counter_arr[1] = str(next_counter)
        counter_text = ":".join(counter_arr)

        if(is_finished_flags[len(is_finished_flags) - 1] == False):
            if(tran_value < treshhold):
                flags_transistors.append(True)
                str_time = ""
                if(next_counter < 10):
                     str_time += "0" + str(next_counter)
                else:
                    str_time += str(next_counter)
                stamp_arr.append(str_time)
            
        #sleep(0.3) #debounce     
        button_state = button_channel.value
       # print(button_state)
        if( button_state >= 26350): #restart the script
            os.execv(sys.executable, ['python'] + [sys.argv[0]]) 

        sleep(1)
        #print(stamp_arr)
    

def main():
    sleep(0.1) #debounce    
    button_state = button_channel.value 
    #print(button_state)
    disp._disp_setting.image(start_screen(fontsize))
    button_flags.append(True)

    while True:
            sleep(0.1) #debounce    
            button_state = button_channel.value
           # print(button_state)
            if( button_state >= 26350 ):
                tick()

main()