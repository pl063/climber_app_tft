from convert_time import conv_time

from PIL import Image, ImageDraw, ImageFont

def timer_screen(fontsize, text, flags):
    image = Image.new("RGB", (320,  240))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 320, 240), fill=(123, 125, 192))

    draw.rectangle( (10, 10, 310, 230 ), fill=(255, 255, 255))

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fontsize)

    draw.ellipse((70, 30, 250, 210), fill =(255, 255, 255), outline ="black") 
   
  #  text = "0:0"
    result = conv_time(text, flags)
    
    draw.text(
        (145, 105, 250, 200),
        ":".join(result),
        font=font,
        fill=(0, 0, 0),
    )

    return image