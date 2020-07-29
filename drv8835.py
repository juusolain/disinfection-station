import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class DRV8835():
    def __init__(self):
        self.RIGHT = 6
        
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)

        GPIO.setup(self.RIGHT, GPIO.OUT)

        self.RIGHT_PWM = GPIO.PWM(13, 50)
        self.RIGHT_PWM.start(1)

    def forward(self,right_speed):
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, right_speed)

    def backward(self, right_speed):
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, -right_speed)

    def set_motor_speed(self, motor, dir_pin, speed):
        if speed < 0:
            GPIO.output(dir_pin, GPIO.HIGH)
            speed = -speed
        else:
            GPIO.output(dir_pin, GPIO.LOW)
        motor.ChangeDutyCycle(speed)

    def stop(self):
        self.set_motor_speed(self.RIGHT_PWM, self.RIGHT, 0)