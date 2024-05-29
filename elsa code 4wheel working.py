import machine
import utime
import _thread
#import signal
import sys

PWM1 = 2 #for all motor speed controller
PWM2 = 7
PWM3 = 21
PWM4 = 16
IN1 = 3
IN2 = 4
IN3 = 5
IN4 = 6
IN1_2 = 20
IN2_2 = 19
IN3_2 = 18
IN4_2 = 17

#LEFT WHEELS
#ENC1A =13  # YELLOW
#ENC1B =12  # WHITE
enc1A = machine.Pin(13, machine.Pin.IN)
enc1B = machine.Pin(12, machine.Pin.IN)
posi1 = 0  # Global variable to store the position
pwm_pin1 = machine.Pin(PWM1, machine.Pin.OUT)
in1_pin = machine.Pin(IN1, machine.Pin.OUT)
in2_pin = machine.Pin(IN2, machine.Pin.OUT)
pwm1 = machine.PWM(pwm_pin1)
pwm1.freq(1000)  # Set PWM frequency to 1kHz


#ENC2A =9
#ENC2B =8
enc2A = machine.Pin(9, machine.Pin.IN)
enc2B = machine.Pin(8, machine.Pin.IN)
posi2 = 0  # Global variable to store the position
pwm_pin2 = machine.Pin(PWM2, machine.Pin.OUT)
in3_pin = machine.Pin(IN3, machine.Pin.OUT)
in4_pin = machine.Pin(IN4, machine.Pin.OUT)
pwm2 = machine.PWM(pwm_pin2)
pwm2.freq(1000)  # Set PWM frequency to 1kHz


#RIGHT WHEELS
#ENC3A =11
#ENC3B =10
enc3A = machine.Pin(11, machine.Pin.IN)
enc3B = machine.Pin(10, machine.Pin.IN)
posi3 = 0  # Global variable to store the position
pwm_pin3 = machine.Pin(PWM3, machine.Pin.OUT)
in1_2_pin = machine.Pin(IN1_2, machine.Pin.OUT)
in2_2_pin = machine.Pin(IN2_2, machine.Pin.OUT)
pwm3 = machine.PWM(pwm_pin3)
pwm3.freq(1000)  # Set PWM frequency to 1kHz

#ENC4A =15
#ENC4B =14
enc4A = machine.Pin(15, machine.Pin.IN)
enc4B = machine.Pin(14, machine.Pin.IN)
posi4 = 0  # Global variable to store the position
pwm_pin4 = machine.Pin(PWM4, machine.Pin.OUT)
in3_2_pin = machine.Pin(IN3_2, machine.Pin.OUT)
in4_2_pin = machine.Pin(IN4_2, machine.Pin.OUT)
pwm4 = machine.PWM(pwm_pin4)
pwm4.freq(1000)  # Set PWM frequency to 1kHz


def set_motor(direc, pwm, pwm_val, mdp1, mdp2):
    pwm.duty_u16(int(pwm_val * 65535 / 100))  # Convert 0-100% to 0-65535
    if direc == 1:
        mdp1.value(1)
        mdp2.value(0)
    elif direc == -1:
        mdp1.value(0)
        mdp2.value(1)
    else:
        mdp1.value(0)
        mdp2.value(0)

'''
def read_encoder(pin, posi, enc):
    global posi
    if enc.value() > 0:
        posi += 1
    else:
        posi -= 1

set_motor(direc, pwm, pwm_val, mdp1,mdp2):
read_encoder(pin, posi, enc):

def set_motor1(dir1, pwm_val_1):
    pwm1.duty_u16(int(pwm_val_1 * 65535 / 100))  # Convert 0-100% to 0-65535
    if dir1 == 1:
        in1_pin.value(1)
        in2_pin.value(0)
    elif dir1 == -1:
        in1_pin.value(0)
        in2_pin.value(1)
    else:
        in1_pin.value(0)
        in2_pin.value(0)



def set_motor2(dir2, pwm_val_2):
    pwm2.duty_u16(int(pwm_val_2 * 65535 / 100))  # Convert 0-100% to 0-65535
    if dir2 == 1:
        in3_pin.value(1)
        in4_pin.value(0)
    elif dir2 == -1:
        in3_pin.value(0)
        in4_pin.value(1)
    else:
        in3_pin.value(0)
        in4_pin.value(0)
        

def set_motor3(dir3, pwm_val_3):
    pwm3.duty_u16(int(pwm_val_3 * 65535 / 100))  # Convert 0-100% to 0-65535
    if dir3 == 1:
        in1_2_pin.value(1)
        in2_2_pin.value(0)
    elif dir3 == -1:
        in1_2_pin.value(0)
        in2_2_pin.value(1)
    else:
        in1_2_pin.value(0)
        in2_2_pin.value(0)

def set_motor4(dir4, pwm_val_4):
    pwm4.duty_u16(int(pwm_val_4 * 65535 / 100))  # Convert 0-100% to 0-65535
    if dir4 == 1:
        in3_2_pin.value(1)
        in4_2_pin.value(0)
    elif dir4 == -1:
        in3_2_pin.value(0)
        in4_2_pin.value(1)
    else:
        in3_2_pin.value(0)
        in4_2_pin.value(0)
'''        
        
def read_encoder1(pin):
    global posi1
    #value = enc1B.value()
    #LEFT WHEEL
    if  enc1B.value() > 0:
        posi1 += 1
    else:
        posi1 -= 1

def read_encoder2(pin):
    global posi2
    #value = enc2B.value()
    #LEFT WHEEL
    if  enc2B.value() > 0:
        posi2 += 1
    else:
        posi2 -= 1

def read_encoder3(pin):
    global posi3
    #value = enc3B.value()
    #RIGHT WHEEL - so the change is opposite to LEFT WHEEL
    if  enc3B.value() > 0:
        posi3 -= 1
    else:
        posi3 += 1
        # Do nothing

def read_encoder4(pin):
    global posi4
    #value = enc4B.value()
    #RIGHT WHEEL - so the change is opposite to LEFT WHEEL
    if  enc4B.value() > 0:
        posi4 -= 1
    else:
        posi4 += 1

'''
def read_encoder2(pin):
    global posi2
    #LEFT WHEEL
    if enc2B.value() > 0:
        posi2 += 1
    else:
        posi2 -= 1
def read_encoder3(pin):
    global posi3
    #RIGHT WHEEL - so the change is opposite to LEFT WHEEL
    if enc3B.value() > 0:
        posi3 += 1
    else:
        posi3 -= 1
def read_encoder4(pin):
    global posi4
    #RIGHT WHEEL - so the change is opposite to LEFT WHEEL
    if enc4B.value() > 0:
        posi4 += 1
    else:
        posi4 -= 1
'''

#Attach the interrupt to the encoder pin
#// encA.irq(trigger=machine.Pin.IRQ_RISING, handler=read_encoder)

enc1A.irq(trigger=machine.Pin.IRQ_RISING, handler=read_encoder1)
enc2A.irq(trigger=machine.Pin.IRQ_RISING, handler=read_encoder2)
enc3A.irq(trigger=machine.Pin.IRQ_RISING, handler=read_encoder3)
enc4A.irq(trigger=machine.Pin.IRQ_RISING, handler=read_encoder4)


# Define the handler function
#def signal_handler(sig, frame):
#    print('You pressed Ctrl+C! Exiting gracefully...')
#    exit(0)

# Set up the signal handler
#signal.signal(signal.SIGINT, signal_handler)

print('Press Ctrl+C to exit')

def main_loop():  
    global posi1
    global posi2
    global posi3
    global posi4

    set_motor(1, pwm1, 50, in1_pin, in2_pin)
    set_motor(1, pwm2, 50, in3_pin, in4_pin)
    set_motor(1, pwm3, 50, in2_2_pin, in1_2_pin)
    set_motor(1, pwm4, 50, in4_2_pin, in3_2_pin)

    current4 = posi4
    prev4 = posi4

    current1 = posi1
    prev1 = posi1

    while True:
        
        prev4 = current4
        prev1 = current1
        utime.sleep(5)
        #print(posi1,posi2,posi3,posi4)
        current4 = posi4
        current1 = posi1

        difference4 = current4 - prev4
        difference1 = current1 - prev1

        print(difference4, difference1)
        #print(difference1)
        
# _thread.start_new_thread(main_loop, ())h

try:
    main_loop()
except KeyboardInterrupt:
    print('KeyboardInterrupt caught! Exiting gracefully...')
    sys.exit(0)

