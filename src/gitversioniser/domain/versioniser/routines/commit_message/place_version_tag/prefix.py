from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.abstract import PlaceVersionTag


class Prefix(PlaceVersionTag):
    @staticmethod
    def run(new_version: str, message: str) -> str:
        return f"[`{new_version}`] {message}"
