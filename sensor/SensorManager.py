from sensor.DHT import DHT
from sensor.GPS import GPS
from libs.ThreadRunnable import ThreadRunnable
import time

class SensorManager(ThreadRunnable):
    def __init__(self):
        super().__init__()
        self.sensor_list = [DHT(), GPS()]
        self.sensors_data = {}

    def get_sensor_reading(self, what: str):
        return self.sensors_data[what]

    def on_start(self):
        for s in self.sensor_list:
            s.thread_start()

    def main_body(self):
        for s in self.sensor_list:
            for k, v in s.get_readings().items():
                self.sensors_data[k] = v
        time.sleep(2)

    def on_end(self):
        for s in self.sensor_list:
            s.thread_stop()
        for s in self.sensor_list:
            s.thread_join()

    def exit_nicely(self, *args):
        pass
