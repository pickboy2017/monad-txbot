import os
from colorama import init, Fore, Style

def display_banner():
    init(autoreset=True)

    full_banner = [
        "███████╗██╗     ██╗  ██╗     ██████╗██╗   ██╗██████╗ ███████╗██████╗.",
        "╚══███╔╝██║     ██║ ██╔╝    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗",
        "  ███╔╝ ██║     █████╔╝     ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝",
        " ███╔╝  ██║     ██╔═██╗     ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗",
        "███████╗███████╗██║  ██╗    ╚██████╗   ██║   ██████╔╝███████╗██║  ██║",
        "╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝",
        "Auto Transaction Soneuim Network / Auto Daily Check-in",
        " ",
    ]

    simple_banner = [
        "**------------------------------------**",
        "| Soneuim Auto tx & Daily Check-in Script |",
        "|                                         |",
        "|                                         |",
        "**------------------------------------**",
    ]

    terminal_width = os.get_terminal_size().columns

    banner_to_display = simple_banner if terminal_width < 70 else full_banner

    for line in banner_to_display:
        print(Fore.CYAN + Style.BRIGHT + line.center(terminal_width) + Style.RESET_ALL)

