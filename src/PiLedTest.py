import time
from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def main():
    switch.init()
    time = 0
    while 1:
        if switch.read_slide_switch():
            blink_led(0.2)
        else:
            for _ in range(12):
                blink_led(0.1)
            
            break
    

if __name__ == "__main__":
    main()