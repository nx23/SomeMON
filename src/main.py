from src.core.entities.attack import Attack
from src.core.entities.mon import Mon
from src.core.entities.type import Type

# Load the type_chart
Type.load_type_chart("type_chart.json")

# Creating some types
fire_type = Type("Fire")
water_type = Type("Water")
grass_type = Type("Grass")
poison_type = Type("Poison")

# Creating some attacks
ember = Attack("Ember", power=40, type=fire_type, accuracy=10, attack_status="satk")
water_gun = Attack("Water Gun", power=40, type=water_type, accuracy=100, attack_status="satk")
vine_whip = Attack("Vine Whip", power=45, type=grass_type, accuracy=100, attack_status="satk")

# Creating some Mons
charmander = Mon(
    species="Charmander",
    hp=39,
    atk=52,
    df=43,
    satk=60,
    sdf=50,
    spd=65,
    main_type=fire_type,
    attacks=[ember]
)

squirtle = Mon(
    species="Squirtle",
    hp=44,
    atk=48,
    df=65,
    satk=50,
    sdf=64,
    spd=43,
    main_type=water_type,
    attacks=[water_gun]
)

bulbasaur = Mon(
    species="Bulbasaur",
    hp=45,
    atk=49,
    df=49,
    satk=65,
    sdf=65,
    spd=45,
    main_type=grass_type,
    sub_type=poison_type,
    attacks=[vine_whip]
)

# Simulating a battle
print("=== BATTLE START ===")
print(charmander)
print(squirtle)
print(bulbasaur)

print("\n--- Turn 1 ---")
charmander.attack(squirtle, ember)
print(squirtle)

print("\n--- Turn 2 ---")
squirtle.attack(charmander, water_gun)
print(charmander)

print("\n--- Turn 3 ---")
bulbasaur.attack(charmander, vine_whip)
print(charmander)

print("=== BATTLE END ===")
