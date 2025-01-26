import pytest
from src.core.entities.type import Type
from src.core.entities.mon import Mon
from src.core.entities.attack import Attack
from typing import Tuple

@pytest.fixture
def setup_attack_test() -> Tuple[Type, Type, Attack, Mon, Mon]:
    # Load the type_chart
    Type.load_type_chart("type_chart.json")
    fire_type = Type(name="Fire")
    water_type = Type(name="Water")
    attack = Attack(name="Flamethrower", type=fire_type, accuracy=100, power=95, attack_status='atk')
    charizard = Mon(species="Charizard", main_type=fire_type, atk=84, df=78, satk=109, sdf=85, spd=100, hp=100)
    blastoise = Mon(species="Blastoise", main_type=water_type, atk=83, df=100, satk=85, sdf=105, spd=100, hp=100)
    return fire_type, water_type, attack, charizard, blastoise

def test_attack_initialization(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    fire_type, _, attack, _, _ = setup_attack_test
    assert attack.name == "Flamethrower", "Attack name should be 'Flamethrower'"
    assert attack.type == fire_type, "Attack type should be 'Fire'"
    assert attack.accuracy == 100, "Attack accuracy should be 100"
    assert attack.power == 95, "Attack power should be 95"
    assert attack.attack_status == 'atk', "Attack status should be 'atk'"

def test_attack_name_setter(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    attack.name = "Fire Blast"
    assert attack.name == "Fire Blast", "Attack name should be 'Fire Blast'"

def test_attack_type_setter(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, water_type, attack, _, _ = setup_attack_test
    attack.type = water_type
    assert attack.type == water_type, "Attack type should be 'Water'"

def test_attack_accuracy_setter(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    attack.accuracy = 85
    assert attack.accuracy == 85, "Attack accuracy should be 85"
    with pytest.raises(ValueError):
        attack.accuracy = -10

def test_attack_power_setter(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    attack.power = 100
    assert attack.power == 100, "Attack power should be 100"
    with pytest.raises(ValueError):
        attack.power = -10

def test_attack_status_setter(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    attack.attack_status = 'satk'
    assert attack.attack_status == 'satk', "Attack status should be 'satk'"

def test_calculate_damage(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, charizard, blastoise = setup_attack_test
    damage = attack.calculate_damage(charizard, blastoise)
    assert damage > 0, "Damage should be greater than 0"
    assert blastoise.current_hp < blastoise.max_hp, "Target's current HP should be less than 100"

def test_attack_miss(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, charizard, blastoise = setup_attack_test
    attack.accuracy = 0  # Ensures the attack will miss
    damage = attack.calculate_damage(charizard, blastoise)
    assert damage == 0, "Damage should be 0 when attack misses"
    assert blastoise.current_hp == blastoise.max_hp, "Target's current HP should remain 100 when attack misses"

def test_attack_str_method(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    assert str(attack) == "Flamethrower (Fire)", "String representation of attack should be 'Flamethrower (Fire)'"

def test_attack_repr_method(setup_attack_test: tuple[Type, Type, Attack, Mon, Mon]):
    _, _, attack, _, _ = setup_attack_test
    assert repr(attack) == "Attack(name='Flamethrower', type=Type(name='Fire'), accuracy=100, power=95, attack_status='atk')", "Repr representation of attack should match"
