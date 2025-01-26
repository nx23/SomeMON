# SomeMON - Pokémon Battle Simulator

SomeMON is a battle simulator inspired by Pokémon, allowing you to create and interact with attacks based on types, resistance, weakness, and immunity, with realistic combat logic.

## Features

- **Types and Interactions:** Each type of attack and Pokémon has its resistances, weaknesses, and immunities, which affect the damage during battles.
- **Custom Attacks:** Create attacks with different types, powers, and accuracies.
- **Realistic Damage Calculation:** Damage varies depending on the resistances and weaknesses of the target type.
- **Battle Simulation:** The combat mechanics are simulated based on type interactions, attack effects, and much more.

## Project Structure

This project is structured as follows:
```
SomeMON - Pokémon Battle Simulator/
├── src/
│   ├── core/
│   │   └── entities/
│   │       ├── attack.py # Definition of the Attack class, with combat mechanics
│   │       ├── mon.py # Definition of the MON class that will have the interaction mechanics
│   │       └── type.py # Definition of the Type class, containing the types of attacks and Pokémon 
│   ├── data/
│   │   └── type_chart.json # JSON file containing the chart of resistances, weaknesses, and immunities
│   ├── main.py # Edit and run this file to start the battles
│   └── README.md # Project documentation
└── tests/
    ├── test_attack.py # Unit tests for the Attack class
    ├── test_mon.py # Unit tests for the MON class
    └── test_type.py # Unit tests for the Type class
```

## How to Run

### Prerequisites

This project requires Python 3.7+.

1. Clone this repository:

    ```bash
    git clone https://github.com/user/someMON.git
    cd someMON
    ```

2. To run the code, execute the following command:
    ```bash
    python -m src.main
    ```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [gbotareli@gmail.com](mailto:gbotareli@gmail.com).