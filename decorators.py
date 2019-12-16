##  CLOSURE EXAMPLE  ##
def outer_function(msg):
	def inner_function():
		print(message)
	return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")

hi_func()


######
"""	DECORATORS is a function that takes another function 
	as an argument add some functionality and returns another function.
	So for example, if you wanted to log information when 
	a function is run, you could use a decorator to add this 
	functionality without modifying the source code of your original function.
"""

##  BASIC FUNCTION DECORATOR EXAMPLE

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print("wrapper executed before {}".format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

def display():
	print("display has ran")

decorated_function = decorator_function(display)
decorated_function()

## THE ABOVE IS SAME AS THE FOLLOWING
@decorator_function
def display():
	print("display has ran")
 
## ADDING SECOND FUNCTION 
@decorator_function
def display_info(name, age):
	print("display_info ran with arguments ({}, {})".format(name, age))

display()
display_info("Alex", 35)


## EXAMPLE OF USING CLASSES AS DECORATORS

class decorator_class(object):

	def __init__(self, original_function):
		self.original_function = original_function

	## USING __call__ function to mimic functionality 
	def __call__(self, *args, **kwargs):
		print("wrapper executed before {}".format(self.original_function.__name__))
		return self.original_function(*args, **kwargs)

## THE ABOVE IS SAME AS THE FOLLOWING
@decorator_class
def display():
	print("display has ran")
 
## ADDING SECOND FUNCTION 
@decorator_class
def display_info(name, age):
	print("display_info ran with arguments ({}, {})".format(name, age))

display()
display_info("Alex", 35)


## PRACTICAL EXAMPLE OF USING DECORATORS
## Track how many time specific function has run and what arguments were passed 

from functools import wraps 

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Tom', 22)







