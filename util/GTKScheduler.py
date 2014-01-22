import gtk
from collection import deque

class GTKScheduler:
    
    def __init__(self):
        self.actions = 0*[None]

    def schedule(self, time_s, action, args):
        self.actions.append((time*1000, action, args))

    def start(self):
        for t, action, args in self.actions:
            gtk.timeout_add(t, wrap_false, (action, args))

    def wrap_false(action, args):
        action(*args)
        return False
