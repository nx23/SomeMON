import pytest
from src.core.entities.type import Type

@pytest.fixture(scope="module", autouse=True)
def setup_type_test():
    Type.load_type_chart("type_chart.json")
    type_chart = Type.get_type_chart()
    fire_type = Type(name="Fire")
    water_type = Type(name="Water")
    grass_type = Type(name="Grass")
    electric_type = Type(name="Electric")
    ice_type = Type(name="Ice")
    return type_chart, fire_type, water_type, grass_type, electric_type, ice_type

def test_fire_type(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, fire_type, *_ = setup_type_test

    assert fire_type.name == "Fire", "Fire type name should be 'Fire'"
    assert type_chart is not None, "Type chart data should be loaded"
    assert "Grass" in type_chart["Fire"]["resistances"], "Fire type should be resistant to Grass"
    assert fire_type.immunities == tuple(type_chart["Fire"]["immunities"]), "Fire type immunities should match the type chart"
    
def test_water_type(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, _, water_type, _, _, _ = setup_type_test

    assert water_type.name == "Water", "Water type name should be 'Water'"
    assert type_chart is not None, "Type chart data should be loaded"
    assert "Fire" in type_chart["Water"]["resistances"], "Water type should be resistant to Fire"
    assert water_type.immunities == tuple(type_chart["Water"]["immunities"]), "Water type immunities should match the type chart"

def test_grass_type(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, _, _, grass_type, _, _ = setup_type_test

    assert grass_type.name == "Grass", "Grass type name should be 'Grass'"
    assert type_chart is not None, "Type chart data should be loaded"
    assert "Water" in type_chart["Grass"]["resistances"], "Grass type should be resistant to Water"
    assert grass_type.immunities == tuple(type_chart["Grass"]["immunities"]), "Grass type immunities should match the type chart"

def test_electric_type(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, _, _, _, electric_type, _ = setup_type_test

    assert electric_type.name == "Electric", "Electric type name should be 'Electric'"
    assert type_chart is not None, "Type chart data should be loaded"
    assert "Electric" in type_chart["Electric"]["resistances"], "Electric type should be resistant to Electric"
    assert electric_type.immunities == tuple(type_chart["Electric"]["immunities"]), "Electric type immunities should match the type chart"

def test_ice_type(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, _, _, _, _, ice_type = setup_type_test

    assert ice_type.name == "Ice", "Ice type name should be 'Ice'"
    assert type_chart is not None, "Type chart data should be loaded"
    assert "Ice" in type_chart["Ice"]["resistances"], "Ice type should be resistant to Ice"
    assert ice_type.immunities == tuple(type_chart["Ice"]["immunities"]), "Ice type immunities should match the type chart"

def test_type_effectiveness(setup_type_test: tuple[dict[str, dict[str, list[str]]], Type, Type, Type, Type, Type]):
    type_chart, fire_type, water_type, _, _, _ = setup_type_test

    assert fire_type.is_weak_to("Water") == ("Water" in type_chart["Fire"]["weaknesses"]), "Fire type should be weak to Water"
    assert fire_type.is_resistant_to("Grass") == ("Grass" in type_chart["Fire"]["resistances"]), "Fire type should be resistant to Grass"
    assert fire_type.is_immune_to("Electric") == ("Electric" in type_chart["Fire"]["immunities"]), "Fire type should be immune to Electric"
    assert water_type.is_weak_to("Electric") == ("Electric" in type_chart["Water"]["weaknesses"]), "Water type should be weak to Electric"
    assert water_type.is_resistant_to("Ice") == ("Ice" in type_chart["Water"]["resistances"]), "Water type should be resistant to Ice"
    assert water_type.is_immune_to("Grass") == ("Grass" in type_chart["Water"]["immunities"]), "Water type should be immune to Grass"
