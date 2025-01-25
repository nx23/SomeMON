from .Type import Type

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

    def attack(self, target: list[Type]):
        damage = self.power

        for type in target:
            if self.type in type.immunities:
                return 0
            if self.type in type.resistances:
                damage = self._weaken_power(damage)
            if self.type in type.weaknesses:
                damage = self._enhance_power(damage)

        return damage

    def _enhance_power(self, damage) -> int:
        return damage * 2

    def _weaken_power(self, damage) -> int:
        return damage // 2

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
    fairy = Type("Fairy")
    steel = Type("Steel")
    dragon = Type("Dragon")
    normal = Type("Normal")

    # Criar um ataque com tipo 'Dragon' (Dragão)
    dragon_blast = Attack(name="Dragon Blast", type=dragon, accuracy=95, power=95)

    # Exemplo de impressão
    print(dragon_blast)
    print(f"Attack Type: {dragon_blast.type.name}")  # 'Dragon'

    # Verificar resistências, fraquezas, imunidades do ataque
    print(f"Resistances of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.resistances}")
    print(f"Weaknesses of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.weaknesses}")
    print(f"Immunities of Attack Type ({dragon_blast.type.name}): {dragon_blast.type.immunities}")

    # Teste de ataque com interações de tipos
    # Se não houver resistências ou fraquezas, o dano deve ser o poder do ataque
    damage = dragon_blast.attack([normal])
    print(f"Damage must be 95 {damage}")  # O dano deve ser 95, sem alterações

    # Teste de ataque contra tipos que resistem ao ataque
    damage = dragon_blast.attack([steel])
    print(f"Damage must be 47 {damage}")  # O dano deve ser 47

    # Teste de ataque contra tipos super resistentes ao ataque
    damage = dragon_blast.attack([steel, steel])
    print(f"Damage must be 23 {damage}")  # O dano deve ser 23

    # Teste de ataque contra tipos com fraqueza ao ataque
    damage = dragon_blast.attack([dragon])
    print(f"Damage must be 190 {damage}")  # O dano deve ser 190

    # Teste de ataque contra tipos com super fraqueza ao ataque
    damage = dragon_blast.attack([dragon, dragon])
    print(f"Damage must be 380 {damage}")  # O dano deve ser 380

    # Teste de ataque contra tipos com imunidade ao ataque
    damage = dragon_blast.attack([fairy])
    print(f"Damage must be 0 {damage}")  # O dano deve ser 0

    # O poder do golpe deve permanecer o mesmo no fim, ou seja, 95
    print(f"Dragon Blast power must be 95 {dragon_blast.power}")
