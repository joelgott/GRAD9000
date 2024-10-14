import board
import displayio
import busio
import terminalio
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.line import Line

displayio.release_displays()

spi = busio.SPI(MOSI = board.D3, clock=board.D4)
tft_cs = board.D0
tft_dc = board.D2

display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=board.D1)

display = ST7735R(display_bus, width=160, height=128, rotation=90, bgr=True)


# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(160, 128, 1)
color_palette = displayio.Palette(1)
# write some text in each font color, rgb, cmyk
color_palette[0] = 0x000000  # light grey
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

eye3 = Circle(80, 64, 5, outline=0xAA4400, fill=0xAAAA00)
eye2 = Circle(80, 64, 30, outline=0xAA0000, fill=0xAA4400)
eye1 = Circle(80, 64, 60, outline=0xAA0000, fill=0xAA0000)
splash.append(eye1)
splash.append(eye2)
splash.append(eye3)

# for i in range(16):
#     color = 0xFFFF00 - i*0x001100
#     c1 = Circle(80, 64, (i)*2, outline=color)
#     c2 = Circle(80, 64, (i+1)*2, outline=color)
#     splash.append(c1)
#     splash.append(c2)

# text_group = displayio.Group(scale=1, x=20, y=10)
# text_area_green = label.Label(terminalio.FONT, text="GRADIENTE 2024", color=0xFFFFFF)
# text_group.append(text_area_green)
# splash.append(text_group)


#triangle = Triangle(30, 40, 120, 40, 80, 120, fill=0x00FF00, outline=0xFFFFFF)
#splash.append(triangle)
while True:
    pass

