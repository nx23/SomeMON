import json
from pathlib import Path


class Type:
    _type_chart = None

    def __init__(self, name: str):
        self.__name = name

        # Check if the type_chart has been loaded before using it
        if Type._type_chart is None:
            raise ValueError("The type chart has not been loaded. Call 'load_type_chart' first.")

        # Use _get_interactions to get the names of the types, not the instances
        self.__resistances = tuple(Type._get_interactions(name=self.__name, interaction_type="resistances"))
        self.__weaknesses = tuple(Type._get_interactions(name=self.__name, interaction_type="weaknesses"))
        self.__immunities = tuple(Type._get_interactions(name=self.__name, interaction_type="immunities"))

    def __repr__(self) -> str:
        return f"Type(name='{self.__name}')"

    def __str__(self) -> str:
        return self.__name

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Type):
            return self.__name == other.name
        elif isinstance(other, str):
            return self.__name == other
        return False

    def __hash__(self) -> int:
        return hash(self.__name)

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str):
        Type._check_for_valid_type(name)
        self.__name = name

    @property
    def resistances(self) -> tuple[str]:
        return self.__resistances

    @property
    def weaknesses(self) -> tuple[str]:
        return self.__weaknesses

    @property
    def immunities(self) -> tuple[str]:
        return self.__immunities

    @classmethod
    def _check_for_valid_type(cls, type_name: str):
        """Check if the type name is present in the type_chart."""
        if not isinstance(type_name, str) or not type_name:
            raise TypeError(f"{type_name} must be a non-empty string")
        
        if type_name not in Type._type_chart:
            raise TypeError(f"{type_name} is misspelled or is not a valid type.")

    @classmethod
    def _get_interactions(cls, name: str, interaction_type: str) -> list[str]:
        """Get the interactions (resistances, weaknesses, immunities) from the type_chart"""
        return cls._type_chart.get(name, {}).get(interaction_type, [])

    @classmethod
    def load_type_chart(cls, file_name: str = "type_chart.json") -> None:
        """Load the type_chart from a JSON file and store it as a class attribute"""
        if cls._type_chart is None:  # Ensure that the type_chart is loaded only once
            project_root = Path(__file__).resolve().parents[3]  # Project root directory
            file_path = project_root / 'src' / 'data' / file_name
            
            try:
                with file_path.open("r") as f:
                    cls._type_chart = json.load(f)
            except FileNotFoundError:
                raise FileNotFoundError(f"The file {file_name} does not exist at {file_path}.")
            except IOError as e:
                raise IOError(f"An error occurred while trying to read the file {file_name}: {e}")


if __name__ == "__main__":
    # Loading the type_chart once (shared by all instances)
    Type.load_type_chart("type_chart.json")

    # Creating instances of types (both Pokémon and Attacks)
    fire = Type("Fire")
    water = Type("Water")

    # Accessing resistances, weaknesses, and immunities
    print(f"Resistances of Fire: {fire.resistances}")
    print(f"Weaknesses of Fire: {fire.weaknesses}")
    print(f"Immunities of Fire: {fire.immunities}")

    print(f"Resistances of Water: {water.resistances}")
    print(f"Weaknesses of Water: {water.weaknesses}")
    print(f"Immunities of Water: {water.immunities}")

    # Example of comparison
    print(f"Fire == Water? {fire == water}")
    print(f"Fire in set? {'Fire' in {fire}}")
