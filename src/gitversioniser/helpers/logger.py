import logging
from typing import Literal

from rich import pretty, traceback
from rich.console import Console
from rich.logging import RichHandler


CONSOLE = Console(width=140, force_terminal=True)

pretty.install(console=CONSOLE)
traceback.install(console=CONSOLE)

CONSOLE_LOG_LEVEL: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'] = 'INFO'

logging.basicConfig(
    level=CONSOLE_LOG_LEVEL,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, console=CONSOLE)]
)

log = logging.getLogger("rich")
