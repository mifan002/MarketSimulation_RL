# MarketSimulation_RL

![Python 3.9](https://img.shields.io/badge/python-3.9-blueviolet.svg?style=plastic)
[![Latest Commit](https://img.shields.io/github/last-commit/sypsyp97/MarketSimulation_RL?style=plastic&logo=github&logoColor=white&color=blueviolet&label=Latest%20Commit)](https://github.com/sypsyp97/MarketSimulation_RL/commits/main)
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg?style=plastic&logo=apache)](https://opensource.org/licenses/Apache-2.0)
[![Documentation](https://img.shields.io/badge/documentation-view-orange?style=plastic)](https://sypsyp97.github.io/MarketSimulation_RL/)
[![Contributions](https://img.shields.io/badge/Contributions-Contact%20Maintainer-yellow?style=plastic&logo=github&logoColor=white)](https://github.com/sypsyp97/MarketSimulation_RL/issues)

Welcome to the MarketSimulation_RL repository! This project is focused on conducting market simulations using Reinforcement Learning (RL) methods. The primary question we aim to answer is whether collusion can emerge in a market environment even without explicit communication between the agents.


## Table of Contents

1. [Dependencies and Installation](#dependencies-and-installation)
2. [Usage](#usage)
3. [To-Do List](#to-do-list)
4. [License](#license)


## Dependencies and Installation

The project uses the following libraries:

- `gym`: for creating and managing reinforcement learning environments.
- `numpy`: for numerical computations.
- `stable_baselines3`: a set of high-quality implementations of reinforcement learning algorithms.
- `sb3_contrib`: for additional reinforcement learning algorithms such as TRPO.

To install these libraries, you can use `pip`:

```shell
pip install gym numpy stable_baselines3 sb3_contrib
```

## Usage

You can interact with the project's code and see the results of the implemented reinforcement learning algorithms either through the provided Jupyter notebook `test.ipynb` or by running the `main.py` script.

To use the Jupyter notebook, please note that the notebook content is not visible directly in the repository. You will need to clone the repository to see the content of the notebook:

```shell
git clone https://github.com/sypsyp97/MarketSimulation_RL.git
```
After cloning the repository, navigate to the project's root directory and launch Jupyter Notebook:
```shell
cd MarketSimulation_RL
jupyter notebook
```
This will open a new page in your web browser where you can open and run the `test.ipynb` notebook.

To run the `main.py` script, navigate to the project's root directory in your terminal and execute the following command:
```shell
python main.py
```
This will run the main simulation and display the results in the terminal.

## To-Do List

Here are some of the enhancements planned for future development:

- [ ] Adding more realistic elements to the market simulation environment.
- [ ] Use custom data sets for more tailored simulations.

Contributions towards these enhancements are welcome!


## License

This project is licensed under the [Apache-2.0 license](./LICENSE).
