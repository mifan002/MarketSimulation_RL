# MarketSimulation_RL

![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-Apache--2.0-green)

This repository contains work on market simulations using Reinforcement Learning (RL) to find if collusion will happen without communication.

## Table of Contents

1. [Dependencies and Installation](#dependencies-and-installation)
2. [Usage](#usage)
3. [License](#license)

## Dependencies and Installation

The project uses the following libraries:

- `gym`: for reinforcement learning environments
- `numpy`: for numerical computations
- `stable_baselines3`: for reinforcement learning algorithms (PPO, A2C, DQN)
- `sb3_contrib`: for additional reinforcement learning algorithms (TRPO)

To install these libraries, you can use `pip`:

```shell
pip install gym numpy stable_baselines3 sb3_contrib
```

## Usage

At the moment, the repository only contains a single Jupyter notebook `test.ipynb`. You can run this notebook to interact with the code and see the results of the implemented reinforcement learning algorithms.

Please note that as the notebook content is not visible directly in the repository, you may need to clone the repository to see the content of the notebook:

```shell
git clone https://github.com/sypsyp97/MarketSimulation_RL.git
```

## License

This project is licensed under the [Apache-2.0 license](./LICENSE).
