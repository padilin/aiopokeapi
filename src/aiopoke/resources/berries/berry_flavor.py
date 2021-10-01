from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility import Name, NamedResource

if TYPE_CHECKING:
    from . import Berry


class BerryFlavor(NamedResource):
    berries: List["FlavorBerryMap"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.berries = [
            FlavorBerryMap(berry_data) for berry_data in data["berries"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<BerryFlavor berries={self.berries} id_={self.id_} name={self.name} names={self.names}>"


class FlavorBerryMap:
    potency: int
    berry: MinimalResource["Berry"]

    def __init__(self, data) -> None:
        self.potency = data["potency"]
        self.berry = MinimalResource(data["berry"])

    def __repr__(self) -> str:
        return f"<FlavorBerryMap potency={self.potency} berry={self.berry}>"
