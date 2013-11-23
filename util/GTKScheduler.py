import gtk
from collection import deque

class GTKScheduler:
    
    def __init__(self):
        self.actions = 0*[None]
        self.args = 0*[None]


    def schedule(self, time, action, args):
        gtk.timeout_add(int(time*1000), action, *args)

    def prepare(self):
        pass

    def start(self):
        pass

    def run_next(action, args):
        action(*args)
        return False
