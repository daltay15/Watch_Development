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
    
    def show_text(text, x, y):
        # Erase the previously displayed text by drawing a black rectangle over it
        tft.blit(tft, x, y, x + len(text) * 8, y + 16, x, y)

        # Draw the new text at the specified coordinates
        tft.draw(romand, text, x, y, gc9a01.WHITE)


        
    def show_time():
        while True:
            current_time = time.localtime()
            hour = str(current_time[3])
            minute = str(current_time[4])
            second = str(current_time[5])
            if len(hour) == 1:
                hour = '0' + hour
            if len(minute) == 1:
                minute = '0' + minute
            if len(second) == 1:
                second = '0' + second
            time_string = hour + ':' + minute + ':' + second
            show_text(time_string, 45, 120)
            time.sleep(1)
            tft.fill(gc9a01.BLACK)
    
    show_time()

main()

