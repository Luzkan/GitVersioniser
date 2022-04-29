from gitversioniser.config.arguments import Arguments
from gitversioniser.config.config import Config
from gitversioniser.domain.versioniser.versioniser import Versioniser


__version__ = '0.2.0+build.1'


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
