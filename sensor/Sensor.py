from libs.utils import *
from libs.ThreadRunnable import *
from threading import Lock

class Sensor(ThreadRunnable, ABC):
    """
    An abstract class for sensors. Force thread-safety.
    reading_dict format: <reading name:str>: value
    """
    def __init__(self):
        ThreadRunnable.__init__(self)
        self.access_lock = Lock()
        self.reading_dict = {}

    def get_readings(self):
        with self.access_lock:
            return self.reading_dict
    
    def update_reading(self):
        with self.access_lock:
            self.get_reading_from_hardware()
    
    @abstractmethod
    def get_reading_from_hardware(self): pass
