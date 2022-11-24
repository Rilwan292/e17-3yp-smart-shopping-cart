import RPi.GPIO as GPIO
#import the RPi.GPIO library

from RPLCD.gpio import CharLCD
#import the CharLCD library from RPLCD.gpio

GPIO.setwarnings(False)
#to ignore the warnings

lcd = CharLCD(pin_rs = 22, pin_rw=24, pin_e=23, pins_data= [9,25,11,8],
numbering_mode = GPIO.BCM, cols=16, rows=2, dotsize=8)
#declare the LCD pins with GPIO pins of Raspberry Pi 4


#display the text on 16x2 LCD

def LCDDisplay(message):
    lcd.clear()
    lcd.write_string(message)

def LCDClear():
    lcd.clear()

if __name__=="__main__":
    LCDDisplay("Hello PJ")