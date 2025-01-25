import json
import os


class Type:
    _type_chart = None

    def __init__(self, name: str):
        self.__name = name

        # Verificando se o type_chart foi carregado antes de usar
        if Type._type_chart is None:
            raise ValueError("The type chart has not been loaded. Call 'load_type_chart' first.")

        # Usando o _get_interactions para pegar os nomes dos tipos, não as instâncias
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
        """Verifica se o nome do tipo está presente no type_chart."""
        if not isinstance(type_name, str) or not type_name:
            raise TypeError(f"{type_name} must be a non-empty string")
        
        if type_name not in Type._type_chart:
            raise TypeError(f"{type_name} is misspelled or is not a valid type.")

    @classmethod
    def _get_interactions(cls, name: str, interaction_type: str) -> list[str]:
        """Obtém as interações (resistências, fraquezas, imunidades) do type_chart"""
        return cls._type_chart.get(name, {}).get(interaction_type, [])

    @classmethod
    def load_type_chart(cls, file_name: str) -> None:
        """Carrega o type_chart a partir de um arquivo JSON e o armazena como um atributo de classe"""
        if cls._type_chart is None:  # Garantir que vai carregar o type_chart apenas uma vez
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, file_name)
            
            with open(file_path, "r") as f:
                cls._type_chart = json.load(f)


if __name__ == "__main__":
    # Carregando o type_chart uma vez (compartilhado por todas as instâncias)
    Type.load_type_chart("type_chart.json")

    # Criando instâncias de tipos (tanto de Pokémon quanto de Ataques)
    fire = Type("Fire")
    water = Type("Water")

    # Acessando resistências, fraquezas e imunidades
    print(f"Resistances of Fire: {fire.resistances}")
    print(f"Weaknesses of Fire: {fire.weaknesses}")
    print(f"Immunities of Fire: {fire.immunities}")

    print(f"Resistances of Water: {water.resistances}")
    print(f"Weaknesses of Water: {water.weaknesses}")
    print(f"Immunities of Water: {water.immunities}")

    # Exemplo de comparação
    print(f"Fire == Water? {fire == water}")
    print(f"Fire in set? {'Fire' in {fire}}")
