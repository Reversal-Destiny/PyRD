class ErrorHandlerDecorator:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("{0}: {1}".format(self.message, e))
        return wrapped_func