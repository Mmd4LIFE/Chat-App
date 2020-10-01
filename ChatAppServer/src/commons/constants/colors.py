"""
    created at oct 01/2020 by Mmd4LIFE
    - this package create console color
"""

from colorama import Fore, Back, init as colorama_init

class Colors:
    colorama_init(autoreset=True)

    FORE_GREEN = Fore.GREEN
    FORE_RED = Fore.RED
    FORE_YELLOW = Fore.YELLOW
    FORE_CYAN = Fore.CYAN
    FORE_BLUE = Fore.BLUE
    FORE_WHITE = Fore.WHITE

    BACK_GREEN = Back.GREEN
    BACK_RED = Back.RED
    BACK_YELLOW = Back.YELLOW
    BACK_CYAN = Back.CYAN
    BACK_BLUE = Back.BLUE
    BACK_WHITE = Back.WHITE
