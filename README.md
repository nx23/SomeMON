# SomeMON - Pokémon Battle Simulator

SomeMON é um simulador de batalhas inspirado em Pokémon, permitindo que você crie e interaja com ataques baseados em tipos, resistência, fraqueza e imunidade, com uma lógica realista de combate.

## Funcionalidades

- **Tipos e Interações:** Cada tipo de ataque e Pokémon tem suas resistências, fraquezas e imunidades, que afetam o dano durante as batalhas.
- **Ataques Personalizados:** Crie ataques com diferentes tipos, potências e precisões.
- **Cálculo de Dano Realista:** O dano varia dependendo das resistências e fraquezas do tipo alvo.
- **Simulação de Combate:** A mecânica de combate é simulada com base nas interações de tipos, efeitos de ataque e muito mais.

## Estrutura do Projeto

Este projeto é estruturado da seguinte forma:
```
someMON/
└─ src/
   ├─ Mon
   │  ├─ Attack 
   │  │  └── attack.py # Definição da classe Attack, com a mecânica de combate
   │  ├─ Type 
   │  │  ├── type.py # Definição da classe Type, contendo os tipos de ataques e Pokémon
   │  │  └── type_chart.json # Arquivo JSON contendo o gráfico de resistências, fraquezas e imunidades
   │  └── mon.py # Definição da classe de MON que terá as mecânicas de interação
   └── README.md # Documentação do projeto
```

## Como Rodar

### Pré-requisitos

Este projeto requer Python 3.7+.

1. Clone este repositório:

   ```bash
   git clone https://github.com/usuario/someMON.git
   cd someMON
   ```

3. Para rodar o código, execute o seguinte comando:
    ```bash
    python -m src.attack
    ```