def delay_decorator():
    def wrapper_function():
        time.sleep(2)
        
    return wrapper_function

delay_decorator()