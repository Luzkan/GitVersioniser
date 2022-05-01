import logging
from typing import Literal

from rich import pretty
from rich.console import Console
from rich.logging import RichHandler

pretty.install()

CONSOLE_LOG_LEVEL: Literal['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'] = 'INFO'
CONSOLE = Console(width=140, force_terminal=True)


logging.basicConfig(
    level=CONSOLE_LOG_LEVEL,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, console=CONSOLE)]
)

log = logging.getLogger("rich")
