from config.arguments import Arguments
from config.config import Config
from domain.versioniser.versioniser import Versioniser


__version__ = '0.0.1'


def config() -> Config:
    arguments = Arguments.get_arguments()
    return Config(
        target_repository_path=arguments.target_directory,
        versioned_files=arguments.versioned_files,
        routines=arguments.routines,
    )


def main():
    versioniser = Versioniser(config=config())
    versioniser.run()


if __name__ == "__main__":
    main()
