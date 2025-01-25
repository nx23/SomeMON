from src.Mon.Type import Type
from src.Mon import Mon


class Attack:
    def __init__(self, name: str, type: Type, accuracy: int, power: int, effect=None):
        self.name = name
        self.type = type
        self.accuracy = accuracy
        self.power = power
        self.effect = effect

    def __repr__(self) -> str:
        return f"Attack(name='{self.__name}', type='{self.__type}', accuracy={self.__accuracy}, power={self.__power})"

    def __str__(self) -> str:
        return f"{self.__name} ({self.__type.name})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Attack):
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
    def name(self, name):
        Attack._check_for_valid_name(name)
        self.__name = name

    @property
    def type(self) -> Type:
        return self.__type
    
    @type.setter
    def type(self, type: Type):
        self._check_for_valid_type(type)
        self.__type = type

    @property
    def accuracy(self) -> int:
        return self.__accuracy
    
    @accuracy.setter
    def accuracy(self, accuracy):
        Attack._check_for_valid_accuracy(accuracy)
        self.__accuracy = accuracy

    @property
    def power(self) -> int:
        return self.__power
    
    @power.setter
    def power(self, power):
        Attack._check_for_valid_power(power)
        self.__power = power

    def calculate_damage(self, user: Mon, target: Mon, attack: "Attack") -> int:
        # Calcula o dano base considerando ataque e defesa
        if attack.type.name in [user.main_type, user.sub_type]:
            modifiers = [1.25]  # STAB (Same-Type Attack Bonus)
        else:
            modifiers = []

        # Verifica fraquezas, resistências e imunidades
        for target_type in [target.main_type, target.sub_type]:
            if attack.type.name in target_type.immunities:
                print(f"{attack.name} não teve efeito em {target.main_type}")
                return 0
            elif attack.type.name in target_type.resistances:
                modifiers.append(0.5)
            elif attack.type.name in target_type.weaknesses:
                modifiers.append(2.0)

        base_damage = (user.atk / target.df) * attack.power
        return int(base_damage * sum(modifiers))

    @classmethod
    def _check_for_valid_name(cls, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")

    @classmethod
    def _check_for_valid_type(cls, type):
        if not isinstance(type, Type):
            raise TypeError(f"{type} must be a string")

    @classmethod
    def _check_for_valid_accuracy(cls, accuracy):
        if not isinstance(accuracy, int):
            raise TypeError("accuracy must be an integer")

    @classmethod
    def _check_for_valid_power(cls, power):
        if not isinstance(power, int):
            raise TypeError("power must be an integer")

if __name__ == "__main__":
    # Carregar o type_chart
    Type.load_type_chart("type_chart.json")

    # Criar instâncias de tipos
    dragon = Type("Dragon")

    # Criar um ataque com tipo 'Dragon' (Dragão)
    dragon_blast = Attack(name="Dragon Blast", type=dragon, accuracy=95, power=95)

    # Exemplo de impressão
    print(dragon_blast)
    print(f"Attack Type: {dragon_blast.type.name}")  # 'Dragon'

    # Verificar resistências, fraquezas, imunidades do ataque
    print(f"Resistances of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.resistances}")
    print(f"Weaknesses of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.weaknesses}")
    print(f"Immunities of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.immunities}")
