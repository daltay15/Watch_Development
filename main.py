import time
from machine import Pin, SPI, PWM
import gc9a01
import utime
import gc
import romand
import math
import framebuf
'''import image'''

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
        
    def draw_border(radius, cala):
        center_x = 120
        center_y = 120
        '''radius = 119'''
        prev_x, prev_y = None, None
        for angle in range(0, 360, 5):
            x = int(center_x + radius * math.cos(math.radians(angle)))
            y = int(center_y + radius * math.sin(math.radians(angle)))
            if prev_x is not None:
                tft.line(prev_x, prev_y, x, y, cala)
            prev_x, prev_y = x, y
        # connect the last point to the first point to complete the circle
        tft.line(prev_x, prev_y, center_x + radius, center_y, cala)

  
    while True:
        show_time()
        show_date()
        tft.draw(romand, "Akash Patel" , 65, 35, gc9a01.GREEN, 0.6)
        if time.localtime()[5] % 2 == 0:
            draw_border(120, gc9a01.RED)
            draw_border(119, gc9a01.RED)
            draw_border(118, gc9a01.RED)
            draw_border(117, gc9a01.RED)
        else:
            draw_border(120, gc9a01.BLUE)
            draw_border(119, gc9a01.BLUE)
            draw_border(118, gc9a01.BLUE)
            draw_border(117, gc9a01.BLUE)
        time.sleep(1)
        tft.fill(gc9a01.BLACK)

main()
