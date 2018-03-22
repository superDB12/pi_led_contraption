#from gpiozero import LED
#from time import sleep

class PiLedContraption:
    _valid_ports=[]
    _led_order=[]

    def __init__(self, valid_leds):
        self._valid_ports =[18]
        for i in self._valid_ports:
            self._led_order.append(LED(i))


    def led_on(self, user_input_led_number):
        if 1 <= user_input_led_number < 7:
            self._led_order[(user_input_led_number - 1)].on()
            print("LED {} is on".format(user_input_led_number))
        else:
            print("invalid LED")
            print("LED {} is on".format(i))

    def led_off(self):
        pass

    def race_up(self):
        pass

    def race_down(self):
        pass

    def dance_randomly(self):
        pass

'''def blink_led_once(blink_frequency, port):
    """turns the led on for 1/2 the time specified in blink_frequency, then it off for the same amount of time."""
    myLED = LED(port)

    myLED.on()
    sleep(blink_frequency / 2)
    myLED.off()
    sleep(blink_frequency / 2)


def blink_led_forever():
    """blink the led once per second in a never ending loop"""
    while True:
        blink_led_once(1)


def race_led(blink_frequency):
    # led 1
    blink_led_once(blink_frequency, 18)
    # led 2
    blink_led_once(blink_frequency, 23)
    # led 3
    blink_led_once(blink_frequency, 25)
    # led 4
    blink_led_once(blink_frequency, 12)
    # led 5
    blink_led_once(blink_frequency, 16)
    # led 6
    blink_led_once(blink_frequency, 20)
    # led 7
    blink_led_once(blink_frequency, 21)
    # led 8
    blink_led_once(blink_frequency, 26)
    # led 9
    blink_led_once(blink_frequency, 19)
    # led 10
    blink_led_once(blink_frequency, 13)



def test_leds():
    print("This will make the LED blink once")
    blink_led_once(2, 18)

    print ("This will make them race")
    race_led(1)

    print("Come on, we can go faster!")
    race_led(.5)'''

if __name__ == "__main__":
    test_class=PiLedContraption(0)
    type(test_class)

    test_class.led_on()