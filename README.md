# MarketSimulation_RL

[![Python 3.9](https://img.shields.io/badge/Python-3.9-3776AB?style=plastic&logo=python&logoColor=white)](https://docs.python.org/3.9/)
[![Latest Commit](https://img.shields.io/github/last-commit/sypsyp97/MarketSimulation_RL?style=plastic&logo=github&logoColor=white&color=blueviolet&label=Latest%20Commit)](https://github.com/sypsyp97/MarketSimulation_RL/commits/main)
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg?style=plastic&logo=apache)](https://opensource.org/licenses/Apache-2.0)
[![Documentation](https://img.shields.io/badge/Documentation-Online-orange?style=plastic&logo=read-the-docs&logoColor=white)](https://sypsyp97.github.io/MarketSimulation_RL/)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-yellow?style=plastic&logo=github&logoColor=white)](https://github.com/sypsyp97/MarketSimulation_RL/issues)


Welcome to the MarketSimulation_RL repository! This project is focused on conducting market simulations using Reinforcement Learning (RL) methods. The primary question we aim to answer is whether collusion can emerge in a market environment even without explicit communication between the agents.

---

## Table of Contents

- [Dependencies and Installation](#dependencies-and-installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [To-Do List](#to-do-list)
- [License](#license)
- [Contact](#contact)

---

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
---

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

---

## Documentation

The detailed documentation is available [online](https://sypsyp97.github.io/MarketSimulation_RL/).

Alternatively, you can clone the `gh-pages` branch of this repository to view the documentation offline:

- Clone the `gh-pages` branch to your local machine：
 ```bash
git clone -b gh-pages https://github.com/sypsyp97/MarketSimulation_RL.git ./MarketSimulation_RL_Doc
cd MarketSimulation_RL_Doc
 ```
- Open the `index.html` file in a web browser to view the documentation.
```bash
xdg-open index.html
```
---

## To-Do List

Here are some of the enhancements planned for future development:

- [ ] Adding more realistic elements to the market simulation environment.
- [ ] Use custom data sets for more tailored simulations.

Contributions towards these enhancements are welcome!

---

## License

This project is licensed under the [Apache-2.0 license](./LICENSE).

---

## Contact

For further assistance or any questions, feel free to open an issue on this GitHub repository or reach out to the maintainer.

**Yipeng Sun**
- Github: [@sypsyp97](https://github.com/sypsyp97)
- Email: [yipeng.sun@fau.de](mailto:yipeng.sun@fau.de)

Please adhere to the code of conduct when interacting with the community and keep discussions relevant to the project. Happy coding!
