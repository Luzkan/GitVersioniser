from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.abstract import PlaceVersionTag


class Null(PlaceVersionTag):
    @staticmethod
    def run(new_version: str, message: str) -> str:
        return message
