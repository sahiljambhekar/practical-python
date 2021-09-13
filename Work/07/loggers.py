from functools import wraps

def logged(func):
    print("Adding logging to {} ".format(func.__name__))
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Calling function {}".format(func.__name__))
        return func(*args,**kwargs)
    return wrapper   

def log_format(fmt):
  def logged(func):
      print("Adding log format '{}' to {} ".format(fmt,func.__name__))

      @wraps(func)
      def wrapper(*args,**kwargs):
          print(fmt.format(func=func))
          return func(*args,**kwargs)
      
      return wrapper 
  return logged 