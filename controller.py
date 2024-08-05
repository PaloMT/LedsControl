import pyfirmata
import time 


comport='COM10'

board=pyfirmata.Arduino(comport)


led_1=board.get_pin('d:12:o')
led_2=board.get_pin('d:11:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:9:o')
led_5=board.get_pin('d:8:o')

def led(fingerUp):
    led_1.write(fingerUp[0])
    led_2.write(fingerUp[1])
    led_3.write(fingerUp[2])
    led_4.write(fingerUp[3])
    led_5.write(fingerUp[4])

    
    if fingerUp==[0,1,0,0,1]:
        for led in [led_1, led_2, led_3, led_4, led_5]:
            led.write(1)
            time.sleep(0.15)
            led.write(0)
    elif fingerUp==[1,1,0,0,1]: 
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        time.sleep(0.5)  
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        time.sleep(0.5)   
    elif fingerUp==[1,0,0,0,1]: 
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(1)
        time.sleep(0.5)  
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(0)
        time.sleep(0.5)   
        time.sleep(0.5)  
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
        time.sleep(0.5)