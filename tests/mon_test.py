import pytest
from src.core.entities.mon import Mon
from src.core.entities.type import Type
from src.core.entities.attack import Attack

@pytest.fixture
def setup_mon():
    Type.load_type_chart("type_chart.json")
    fire_type = Type(name="Fire")
    normal_type = Type(name="Normal")
    water_type = Type(name="Water")
    attack1 = Attack(name="Ember", power=40, type=fire_type, accuracy=100, attack_status='satk')
    attack2 = Attack(name="Water Gun", power=40, type=water_type, accuracy=100, attack_status='satk')
    mon = Mon(species="Charmander", hp=39, atk=52, df=43, satk=60, sdf=50, spd=65, main_type=fire_type, attacks=[attack1])
    return mon, fire_type, water_type, normal_type, attack1, attack2

def test_mon_initialization(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, fire_type, _, _, _, _ = setup_mon
    assert mon.name == "Charmander", "Mon species should be Charmander"
    assert mon.species == "Charmander", "Mon species should be Charmander"
    assert mon.hp == 39, "Mon HP should be 39"
    assert mon.atk == 52, "Mon attack should be 52"
    assert mon.df == 43, "Mon defense should be 43"
    assert mon.satk == 60, "Mon special attack should be 60"
    assert mon.sdf == 50, "Mon special defense should be 50"
    assert mon.spd == 65, "Mon speed should be 65"
    assert mon.main_type == fire_type, "Mon main type should be Fire"
    assert mon.sub_type is None, "Mon sub type should be None"
    assert len(mon.attacks) == 1, "Mon should have 1 attack"
    assert mon.attacks[0].name == "Ember", "Mon's first attack should be Ember"

def test_add_attack(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, attack2 = setup_mon
    mon.add_attack(attack2)
    assert len(mon.attacks) == 2, "Mon should have 2 attacks after adding one"
    assert attack2 in mon.attacks, "Water Gun attack should be in Mon's attacks"

def test_add_attack_limit(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, fire_type, _, normal_type, _, attack2 = setup_mon
    mon.add_attack(attack2)
    mon.add_attack(Attack(name="Scratch", power=40, type=normal_type, accuracy=100, attack_status='atk'))
    mon.add_attack(Attack(name="Growl", power=0, type=normal_type, accuracy=100, attack_status='atk'))
    with pytest.raises(ValueError, match="A Mon can have at most 4 attacks"):
        mon.add_attack(Attack(name="Overheat", power=130, type=fire_type, accuracy=100, attack_status='atk'))

def test_attack(setup_mon: tuple[Mon, Type, Type, Attack, Attack]):
    mon, _, water_type, _, attack1, _ = setup_mon
    target_mon = Mon(species="Squirtle", hp=44, atk=48, df=65, satk=50, sdf=64, spd=43, main_type=water_type)
    mon.attack(target_mon, attack1)
    assert target_mon.current_hp < target_mon.max_hp, "Target Mon's current HP should be less than max HP after attack"

def test_invalid_stat(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    setup_mon
    with pytest.raises(ValueError, match="hp must be between 1 and 255"):
        Mon(species="Bulbasaur", hp=300, atk=49, df=49, satk=65, sdf=65, spd=45, main_type=Type(name="Fire"))

def test_invalid_type(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    setup_mon
    with pytest.raises(ValueError, match="InvalidType is misspelled or is not a valid type."):
        Mon(species="Bulbasaur", hp=45, atk=49, df=49, satk=65, sdf=65, spd=45, main_type=Type(name="InvalidType"))

def test_set_current_hp(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.current_hp = 20
    assert mon.current_hp == 20, "Mon's current HP should be 20"
    with pytest.raises(ValueError, match="HP value cannot be less than 0"):
        mon.current_hp = -10
    with pytest.raises(ValueError, match="Current HP cannot exceed the maximum*"):
        mon.current_hp = 1000

def test_set_name(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.name = "Char"
    assert mon.name == "Char", "Mon's name should be Char"

def test_set_species(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.species = "Charmeleon"
    assert mon.species == "Charmeleon", "Mon's species should be Charmeleon"

def test_set_hp(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.hp = 45
    assert mon.hp == 45, "Mon's HP should be 45"

def test_set_atk(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.atk = 55
    assert mon.atk == 55, "Mon's attack should be 55"

def test_set_df(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.df = 50
    assert mon.df == 50, "Mon's defense should be 50"

def test_set_satk(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.satk = 65
    assert mon.satk == 65, "Mon's special attack should be 65"

def test_set_sdf(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.sdf = 55
    assert mon.sdf == 55, "Mon's special defense should be 55"

def test_set_spd(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    mon.spd = 70
    assert mon.spd == 70, "Mon's speed should be 70"

def test_add_duplicate_attack(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, attack1, _ = setup_mon
    with pytest.raises(ValueError, match=f"Attack '{attack1.name}' is already added to {mon.name}"):
        mon.add_attack(attack1)

def test_add_invalid_attack(setup_mon: tuple[Mon, Type, Type, Type, Attack, Attack]):
    mon, _, _, _, _, _ = setup_mon
    with pytest.raises(TypeError, match="Attack must be an instance of the Attack class"):
        mon.add_attack("InvalidAttack")
