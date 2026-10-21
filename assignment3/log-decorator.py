# Task 1: Writing and Testing a Decorator

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        
        result = func(*args, **kwargs)
        
        pos_params = list(args) if args else "none"
        kw_params = kwargs if kwargs else "none"
        
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {pos_params}\n"
            f"keyword parameters: {kw_params}\n"
            f"return: {result}"
        )
        logger.log(logging.INFO, log_message)
        
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def process_positional(*args):
    return True

@logger_decorator
def process_keywords(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    process_positional(10, 20, "test")
    process_keywords(first="Alice", role="Admin")