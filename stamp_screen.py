
from PIL import Image, ImageDraw, ImageFont


def stamp_screen(fontsize, stamp_arr, time_str):
    image = Image.new("RGB", (320,  240))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 320, 240), fill=(123, 125, 192))

    draw.rectangle( (10, 10, 310, 230 ), fill=(255, 255, 255))

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fontsize)
    #stamps:
    draw.text(
        (115, 25, 250, 200),
        "Stamps:",
        font=font,
        fill=(0, 0, 0),
    )

    stamp_position_y = 50
    trace_index = 1

    for stamp in stamp_arr:
        text = "Checkpoint "
        text += str(trace_index) + " -" + " "
     
        text += str(stamp) + "s"
        draw.text(
            (70, stamp_position_y, 250, 200),
            text,
            font=font,
            fill=(0, 0, 0),
        )

        trace_index += 1

        stamp_position_y += 25

   #timer:
    draw.ellipse((130, 150, 195, 210), fill =(255, 255, 255), outline ="black") 
   
    
    draw.text(
        (137, 165, 250, 200),
        time_str,
        font=font,
        fill=(0, 0, 0),
    )
    return image
   