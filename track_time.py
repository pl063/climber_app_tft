from timer import timer_screen
from stamp_screen import stamp_screen

counter_arr= ["0", "0"] 
counter_text = ":".join(counter_arr)

flags = [False]

def track_time():
    while True:
        flags.clear()
        flags.append(False)

        channel_value = channel.value
        image = timer_screen(fontsize, counter_text, flags)
        disp._disp_setting.image(image)
        next_counter = int(counter_arr[1]) + 1
        counter_arr[1] = str(next_counter)
        counter_text = ":".join(counter_arr)
        if(channel_value < treshhold):
            stamp_arr.append(str(next_counter))
