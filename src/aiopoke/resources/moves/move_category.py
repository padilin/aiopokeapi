from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Description, NamedResource

if TYPE_CHECKING:
    from . import Move


class MoveCategory(NamedResource):
    description: str
    descriptions: List["Description"]
    moves: List[MinimalResource["Move"]]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = [
            name_data["description"]
            for name_data in data["descriptions"]
            if name_data["language"]["name"] == "en"
        ][0]
        self.descriptions = [Description(description_data) for description_data in data["descriptions"]]
        self.moves = [MinimalResource(move_data) for move_data in data["moves"]]

    def __repr__(self) -> str:
        return f"<MoveCategory description='{self.description}' descriptions={self.descriptions} id_={self.id_} moves={self.moves} name='{self.name}'>"
