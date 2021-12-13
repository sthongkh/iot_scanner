import functools


def exception(logger):
    """
    A decorator that wraps the passed in function and logs 
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception
                err = "There was an exception in "
                err += func.__name__
                logger.exception(err)
                print(err)

            # re-raise the exception
            #raise
        return wrapper
    return decorator

def debug(logger): 
    def mydecorator(f):
        @functools.wraps(f)
        def log_f_as_called(*args, **kwargs):
            value = f(*args, **kwargs)
            f_name = f.__name__
            logger.info("[{}] - {}".format(f_name, value))
            return value
        return log_f_as_called
    return mydecorator