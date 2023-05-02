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
        tft.draw(romand, text, 120, 115, gc9a01.WHITE)
        
    def show_m(text):
        tft.draw(romand, text, 65,115,gc9a01.WHITE)
    
    def show_jpg(jpg):
        tft.jpg(jpg, 30,0, gc9a01.FAST)
        
    def seconds():
        pass
    min = 10

    while True:
        # Dynamicall display i to the screen
        for i in range(0, 61):
            if i == 60:
                min += 1
            if min != 0:
                show_m(str(min))
                
            show_text(str(i))
            time.sleep(.1)
            tft.fill(gc9a01.BLACK)
            
                
        
        '''
        tft.jpg("11d.jpg", 30, 20, gc9a01.FAST)
        tft.draw(romand, "75 F", 130, 70, gc9a01.WHITE) # x, y coords
    
        tft.jpg("home.jpg", 55, 130, gc9a01.FAST)
        tft.draw(romand, "Demir", 130, 155, gc9a01.WHITE)

        time.sleep(1)
        '''

main()


