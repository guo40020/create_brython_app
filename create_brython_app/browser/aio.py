def ajax(method: str, url: str, format='text', headers=None, data=None, cache=False):
    """
    req = await ajax("GET", url) inside an asynchronous function gives back control to the main program, and resumes the function when the Ajax request of the type method ("GET", "POST", "PUT", etc.) to the specified URL is completed. The return value is an instance of the class Request (see below).
    format is the expected response format. It can be one of:
    "text" : the response is a string
    "binary" : an instance of class bytes
    "dataURL" : a string formatted as dataURL
    headers is a dictionary with the HTTP headers to send with the request.
    data is a string or a dictionary that will be sent with the request to form the query string for a "GET" request, or the request body for "POST".
    cache is a boolean indicating if the browser cache should be used
    """
    pass


def get(url: str, format='text', headers=None, data=None, cache=False):
    """
    shortcut for ajax("GET", url...)
    """
    pass


def post(url: str, format='text', headers=None, data=None, cache=False):
    """
    shortcut for ajax("POST", url...)
    """
    pass


def event(element, name):
    """
    evt = await aio.event(element, "click") suspends execution of an asynchronous function until the user clicks on the specified element. The return value is an instance of the DOMEvent class (cf. section events)
    """
    pass


def sleep(seconds):
    """
    In an asynchronous function, await sleep(n) gives back control to the main program and resumes function execution after n seconds.
    """
    pass


def run(coroutine):
    """
    Runs a coroutine, ie the result of a call to an asynchronous function defined by async def. This is a non blocking function: it doesn't wait until the asynchronous function is completed to execute the instructions in the following lines. The time when the next instructions are run is not (easily) predictable.
    """
    pass


class Request:
    def __init__(self):
        self.data = None
        self.response_headers = None
        self.staus = None
        self.statusText = None

