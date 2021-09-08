from functools import wraps
def logged(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
      print("Calling {}".format(f.__name__))
      fun = f(*args,**kwargs)
      #first_arg = fun[1]
      #print("First arg {}".format(first_arg)) 
      return fun 
    return wrapper    

@logged
def add(a,b):
    return a+b
#logged_add = logged(add)  
#add(3,5)