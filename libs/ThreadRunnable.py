import time
from threading import Thread
import signal
from abc import ABC, abstractmethod

'''
Runnable thread abstract class: unify thread executing.
Execution process: on_start() -> main_body() loop -> on_end(). 
This class also needs to handle interrupt signals(SIGTERM and SIGINT) so that the thread can exit nicely. 
Functions to implement:
    on_start()
    main_body()
    on_end()
    exit_nicely()
'''


class ThreadRunnable(ABC):
    def __init__(self):
        self.DEBUG = 1
        signal.signal(signal.SIGINT, self._exit_nicely)
        signal.signal(signal.SIGTERM, self._exit_nicely)
        self.loop_run = True
        self.thread = Thread(target=self.thread_function, args=())

    def set_daemon(self):
        self.thread.daemon = True

    def get_thread(self):
        return self.thread

    def thread_start(self):
        self.loop_run = True
        self.thread.start()

    def thread_run(self):
        self.loop_run = True
        self.thread.run()

    def thread_stop(self):
        self.loop_run = False

    def thread_join(self):
        self.thread.join()

    def _exit_nicely(self, *args):
        self.loop_run = False
        self.exit_nicely(*args)

    @abstractmethod
    def exit_nicely(self, *args): pass

    @abstractmethod
    def on_start(self): pass

    @abstractmethod
    def main_body(self): pass

    @abstractmethod
    def on_end(self): pass

    def thread_function(self):
        self.on_start()
        while self.loop_run:
            self.main_body()
        self.on_end()


if __name__ == '__main__':
    class TestRunnable(ThreadRunnable):
        cnt = 0

        def exit_nicely(self, *args):
            print("Exit nicely")

        def on_start(self):
            print("On start")

        def main_body(self):
            print(f"Main body {self.cnt}")
            self.cnt += 1
            time.sleep(0.5)

        def on_end(self):
            print("On end")


    t = TestRunnable()
    t.thread_start()
    time.sleep(5)
    t.thread_stop()