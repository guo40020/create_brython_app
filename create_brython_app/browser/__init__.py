def alert(message: str):
    """
    a function that prints the message in a pop-up window. Returns None
    :param message: message
    :return: None
    """
    pass


def bind(target: str, event: str):
    """
    a function used as a decorator for event binding.
    :param target: selector
    :param event: event name
    :return:None
    """
    pass


def confirm(message: str) -> bool:
    """
    a function that prints the message in a window, and two buttons (ok/cancel). Returns True if ok, False if cancel
    :param message: message
    :return: bool, True if ok, False if cancel
    """
    pass


class console:
    @staticmethod
    def log(msg):
        pass


class document:
    def __getitem__(self, item):
        pass


def load(script_url: str):
    """
    Load the Javascript library at address script_url.
    This function uses a blocking Ajax call. It must be used when one can't load the Javascript library in the html page by <script src="prog.js"></script>.
    The names inserted by the library inside the global Javascript namespace are available in the Brython script as attributes of the window object.
    :param script_url: script url
    :return: None
    """
    pass


def prompt(message: str, default=''):
    """
    Load the Javascript library at address script_url.
    This function uses a blocking Ajax call. It must be used when one can't load the Javascript library in the html page by <script src="prog.js"></script>.
    The names inserted by the library inside the global Javascript namespace are available in the Brython script as attributes of the window object.
    :param message: message
    :param default: default
    :return: Returns the entered value ; if no value was entered, return default if defined, else the empty string
    """
    pass


def run_script(src: str, name=''):
    """
    this function executes the Python source code in src with an optional name. It can be used as an alternative to exec(), with the benefit that the indexedDB cache is used for importing modules from the standard library.
    :param src: source
    :param name: name
    :return: None
    """
    pass


window = dict()
