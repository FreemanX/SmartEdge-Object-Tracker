from sensor.Sensor import Sensor
import time
from random import uniform

# class GPS
class GPS(Sensor):
    def __init__(self):
        super().__init__()
        self.set_daemon()

    def get_reading_from_hardware(self):
        self.reading_dict['latitude'] = str(round(uniform(-18.456, -14.750), 6))
        self.reading_dict['longitude'] = str(round(uniform(146.629, 151.033), 6))

    def on_start(self):
        """
        Before the thread start, if the censor need any preperation 
        """

    def main_body(self):
        """
        What to run in thread while loop
        """
        self.update_reading()  # call function from super class
        time.sleep(5)

    def on_end(self):
        """
        What to do when thread ends. Clean up hardware cache, release hardware resources...?
        """

    def exit_nicely(self, *args):
        """
        In case of program crashed, what to do?
        """

