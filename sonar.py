import RPi.GPIO as GPIO
import time

# NOTE: don't use GPIO02 or GPIO03, they have
# internal pullup resistors that prevents results.
def sonar():
    try:
      # Setup
      #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(12, GPIO.OUT)
        # Set to low
        GPIO.output(12, False)

        # Sleep 2 micro-seconds
        time.sleep(0.000002)

        # Set high
        GPIO.output(12, True)

        # Sleep 5 micro-seconds
        time.sleep(0.000005)

        # Set low
        GPIO.output(12, False)

        # Set to input
        GPIO.setup(12, GPIO.IN)

        # Count microseconds that SIG was high
        while GPIO.input(12) == 0:
          starttime = time.time()

        while GPIO.input(12) == 1:
          endtime = time.time()

        duration = endtime - starttime
        # The speed of sound is 340 m/s or 29 microseconds per centimeter.
        # The ping travels out and back, so to find the distance of the
        # object we take half of the distance travelled.
        # distance = duration / 29 / 2
        distance = duration * 34000 / 2
        #print var = distance, "cm"
        return distance

    finally:
      GPIO.cleanup()