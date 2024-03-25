#import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

spi = board.SPI()

class Display:
    def __init__(self, pins, baudrate, border, fontsize, ):
        self._pins = pins
        self._baudrate = baudrate
        self._border = border
        self._fontsize = fontsize
        self._disp_setting =  ili9341.ILI9341(
                                                spi,
                                                rotation=90,  # 2.2", 2.4", 2.8", 3.2" ILI9341
                                                cs=pins[0],
                                                dc=pins[1],
                                                rst=pins[2],
                                                baudrate=self._baudrate,
                                                
                                            )
    def create_image(image, width, height):
        image = Image.new("RGB", (width, height))
        draw = ImageDraw.Draw(image)

   