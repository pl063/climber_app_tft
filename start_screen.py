
from PIL import Image, ImageDraw, ImageFont

def start_screen(fontsize):        
    image = Image.new("RGB", (320,  240))
    draw = ImageDraw.Draw(image)
    # Draw a green filled box as the background
    #coordinates for full background are 0, 0, 320, 240
    draw.rectangle((0, 0, 320, 240), fill=(123, 125, 192))
    # Draw a smaller inner rectangle
    draw.rectangle(
    (10, 10, 310, 230 ), fill=(255, 255, 255)
    )
    # Load a TTF Font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", fontsize)
    # Draw Some Text
    text = "Climber v1.0.0"
    draw.text(
        (90, 70, 250, 200),
        text,
        font=font,
        fill=(0, 0, 0),
    )
    draw.rectangle(
        (80, 110, 250, 150), fill=(75, 213, 231)
    )
    text2 = "Start"
    draw.text(
        (140, 120, 200, 200),
        text2,
        font=font,
        fill=(0, 0, 0),
    )

    return image