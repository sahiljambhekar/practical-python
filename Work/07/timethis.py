import time
from functools import wraps
def timethis(func):
    print("Timing {func.__name__}".format(func=func))
    
    @wraps
    def wrapper():
        start = time.time()
        func(*args,**kwargs)
        stop  = time.time()
        print("Took {} secs to execute {}".format(
            (stop - start), func.__name__
        ))

    return wrapper       
