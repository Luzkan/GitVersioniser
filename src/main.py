from gitversioniser.config.arguments import Arguments
from gitversioniser.config.config import Config
from gitversioniser.domain.versioniser.versioniser import Versioniser
from gitversioniser.helpers.logger import CONSOLE


__version__ = '0.6.0-rc.1+build.7'


def config() -> Config:
    arguments = Arguments.get_arguments()
    return Config(
        target_repository_path=arguments.target_directory,
        versioned_files=arguments.versioned_files,
        routines=arguments.routines,
        commit_patterns=arguments.patterns,
    )


def greetings():
    CONSOLE.rule('[b]GitVersioniser[/b]')
    CONSOLE.print('Automatic Semantic Versioniser & Change Tracker', style="b green", justify="center")
    CONSOLE.print('https://github.com/Luzkan/GitVersioniser', style="magenta", justify="center")
    CONSOLE.print(f'v{__version__}', style="b green", justify="center")


def main():
    greetings()
    versioniser = Versioniser(config=config())
    versioniser.run()


if __name__ == "__main__":
    main()
