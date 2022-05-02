import logging
from typing import Literal

from rich import pretty, traceback
from rich.console import Console
from rich.logging import RichHandler


CONSOLE_WIDTH: int = 140
CONSOLE: Console = Console(width=CONSOLE_WIDTH, force_terminal=True)

pretty.install(console=CONSOLE)
traceback.install(console=CONSOLE, width=CONSOLE_WIDTH)

CONSOLE_LOG_LEVEL: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'] = 'INFO'

logging.basicConfig(
    level=CONSOLE_LOG_LEVEL,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, console=CONSOLE)]
)
