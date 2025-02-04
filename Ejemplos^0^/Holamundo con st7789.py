import machine
import st7789
import vga2_8x16 as font  

spi = machine.SPI(1, baudrate=8000000, sck=machine.Pin(40), mosi=machine.Pin(41))

DC = machine.Pin(11, machine.Pin.OUT)
CS = machine.Pin(12, machine.Pin.OUT)
BL = machine.Pin(42, machine.Pin.OUT)

tft = st7789.ST7789(spi, 240, 320, dc=DC, cs=CS, backlight=BL, rotation=1)
tft.init()

tft.text(font, "Hola mundo", 130, 100, st7789.WHITE, st7789.BLACK)


