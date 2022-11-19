from sensor.Sensor import Sensor
import random
import time

# class DHT
class DHT(Sensor):
    def __init__(self):
        super().__init__()
        self.set_daemon()

    def get_reading_from_hardware(self):
        alpha = 0.01
        if 'temperature' not in self.reading_dict:
            self.reading_dict['temperature'] = round(random.randrange(150, 250) / 10, 1)
        else:
            self.reading_dict['temperature'] = round(self.reading_dict['temperature'] * \
                (1-alpha) + random.randrange(100, 300)/10 * alpha, 1)

    def on_start(self):
        """
        Before the thread start, if the censor need any preperation 
        """

    def main_body(self):
        """
        What to run in thread while loop
        """
        self.update_reading()  # call function from super class
        time.sleep(2)

    def on_end(self):
        """
        What to do when thread ends. Clean up hardware cache, release hardware resources...?
        """

    def exit_nicely(self, *args):
        """
        In case of program crashed, what to do?
        """

