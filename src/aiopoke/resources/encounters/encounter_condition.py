from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from . import EncounterConditionValue


class EncounterCondition(NamedResource):
    values: List[MinimalResource["EncounterConditionValue"]]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.values = [
            MinimalResource(encounter_condition_value)
            for encounter_condition_value in data["values"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<EncounterCondition id_={self.id_} name='{self.name}' names={self.names} values={self.values}>"
