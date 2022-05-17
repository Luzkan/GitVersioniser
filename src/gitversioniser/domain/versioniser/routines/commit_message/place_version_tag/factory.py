from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.abstract import PlaceVersionTag
from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.null import Null
from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.prefix import Prefix
from gitversioniser.domain.versioniser.routines.commit_message.place_version_tag.suffix import Suffix
from gitversioniser.domain.versioniser.routines.factory import RoutineFactory
from gitversioniser.helpers.types import ROUTINE_COMMIT_MESSAGE_PLACE_VERSION_TAG


class PlaceVersionTagFactory(RoutineFactory):
    @staticmethod
    def create(routine_name: ROUTINE_COMMIT_MESSAGE_PLACE_VERSION_TAG) -> type[PlaceVersionTag]:
        return {
            RoutineFactory.skip_init(Null).factory_name(): Null,
            RoutineFactory.skip_init(Prefix).factory_name(): Prefix,
            RoutineFactory.skip_init(Suffix).factory_name(): Suffix,
        }[routine_name]
