import time
from machine import Pin, SPI
import gc9a01
import romand
import framebuf

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
        rotation=25)

    tft.init()
    tft.fill(gc9a01.BLACK)
        
    def show_date():
        now = time.localtime()
        year = str(now[0])
        month = str(now[1])
        day = str(now[2])
        date_str = f"{month}/{day}/{year}"
        tft.draw(romand, date_str, 35, 140, gc9a01.WHITE)
    
    def show_time():
        now = time.localtime()
        hour = str(now[3])
        minute = str(now[4])
        second = str(now[5])
        time_str = f"{hour}:{minute}:{second}"
        tft.draw(romand, time_str, 50, 95, gc9a01.WHITE)
    
    while True:
        show_time()
        show_date()
        time.sleep(1)
        tft.fill(gc9a01.BLACK)

main()

