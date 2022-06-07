import threading

class Singleton(type):
    __instance = {}
    __lock = threading.Lock()

    def __call__(cls, *args, **kwds):
        if cls not in cls.__instance:
            with cls.__lock:
                if cls not in cls.__instance:
                    cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls.__instance[cls]