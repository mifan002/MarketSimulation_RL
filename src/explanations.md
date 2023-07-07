# Market Simulation with Reinforcement Learning

This project defines a custom environment using OpenAI's Gym framework to simulate a market with two sellers and four buyers. 

In this simulated marketplace, each seller sets a price, which is their action within the environment. Each buyer, on the other hand, has a certain willingness to pay. The state of the environment consists of the two prices set by the sellers and the current willingness to pay of each buyer.

The `step` method implemented in the environment dictates how buyers are distributed to the sellers based on the prices set by the sellers, and how the state of the environment is subsequently updated. Specifically, if a buyer's willingness to pay is larger or equal to a seller's price, the buyer buys from that seller. The amount of money exchanged is then added to the seller's score, which is the price they had set.

The reward within this environment is defined as the sum of the profits of the sellers. The simulation concludes when all buyers have purchased products. This is indicated by a `done` flag set to `True` when the sum of the remaining willingness to pay of all buyers is zero.

This implementation provides a simplified version of market dynamics and serves as a starting point for exploring more complex scenarios. Real-world factors such as product quality, brand loyalty, imperfect price adjustment, and more can be considered when refining this model.

The next step for this project is the implementation of reinforcement learning agents, such as Q-learning agents, to dictate the actions of the sellers. The agents are expected to learn to set prices (actions) based on the current state of the environment in order to maximize the reward they receive.
