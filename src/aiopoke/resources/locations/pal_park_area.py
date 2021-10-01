from typing import List, TYPE_CHECKING
from ...minimal_resources import MinimalResource
from ...utility.common_models import Name, NamedResource

if TYPE_CHECKING:
    from ...resources import PokemonSpecies


class PalParkArea(NamedResource):
    pokemon_encounters: List["PalParkEncounterSpecies"]
    names: List["Name"]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.pokemon_encounters = [
            PalParkEncounterSpecies(pokemon_encounter_data)
            for pokemon_encounter_data in data["pokemon_encounters"]
        ]
        self.names = [Name(name_data) for name_data in data["names"]]

    def __repr__(self) -> str:
        return f"<PalParkArea id_={self.id_} pokemon_encounters={self.pokemon_encounters} name='{self.name}' names={self.names}>"


class PalParkEncounterSpecies:
    base_score: int
    rate: int
    pokemon_species: MinimalResource["PokemonSpecies"]

    def __init__(self, data) -> None:
        self.base_score = data["base_score"]
        self.rate = data["rate"]
        self.pokemon_species = MinimalResource(data["pokemon_species"])

    def __repr__(self) -> str:
        return f"<PalParkEncounterSpecies base_score={self.base_score} rate={self.rate} pokemon_species={self.pokemon_species}"
