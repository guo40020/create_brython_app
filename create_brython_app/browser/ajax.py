class Ajax:
    pass


def bind(evt, function):
    """
    attaches the function to the event evt. evt is a string that matches the different request states :
    "uninitialized" : not initialized
    "loading" : established connection
    "loaded": received request
    "interactive": response in progress
    "complete" : finished
    The function takes a single argument, the Ajax instance.
    """
    pass


def open(method, url, async_):
    """
    method is the HTTP method used for the request (usually GET or POST),
    url is the url to call,
    async is a boolean that indicates whether the call is asynchronous (the script that started the request goes on running without waiting for the response) or not (the script hangs until the response is received).
    """
    pass


readyState = 0
