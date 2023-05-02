import time
from machine import Pin, SPI
import gc9a01
import romand

def main():
    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=0)

    tft.init()
    tft.fill(gc9a01.BLACK)
    
    def show_text(text):
        tft.draw(romand, text, 15, 115, gc9a01.WHITE)
    
    def show_jpg(jpg):
        tft.jpg(jpg, 30,0, gc9a01.FAST)

    while True:
        show_text("Hello World")
        show_jpg("11d.jpg")
        '''
        tft.jpg("11d.jpg", 30, 20, gc9a01.FAST)
        tft.draw(romand, "75 F", 130, 70, gc9a01.WHITE) # x, y coords
    
        tft.jpg("home.jpg", 55, 130, gc9a01.FAST)
        tft.draw(romand, "Demir", 130, 155, gc9a01.WHITE)

        time.sleep(1)
        '''

main()