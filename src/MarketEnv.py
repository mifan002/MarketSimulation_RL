# Define the environment
import gym
import numpy as np
from gym import spaces


# Define the market environment
class MarketEnvironment(gym.Env):
    """A custom environment that simulates a market with two sellers and four buyers.

    Each seller sets a price (the action), and each buyer has a certain willingness to
    pay. The state of the environment consists of the two prices set by the sellers and
    the current willingness to pay of each buyer.

    The episode ends when all buyers have bought the products.
    """

    def __init__(self):
        """Initialize the MarketEnvironment.

        Define action and observation spaces. Initialize state and prices history.
        """
        super(MarketEnvironment, self).__init__()

        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions, Box(2,) for two sellers
        self.action_space = spaces.MultiDiscrete([101, 101])

        # Prices could range from 0 to 100, there are four buyers
        self.observation_space = spaces.Box(low=0, high=100, shape=(6,))
        self.prices_history = []

        # Initialize state
        self.reset()

    def step(self, action):
        """Execute one time step within the environment.

        Parameters
        ----------
        action : array_like
            The prices set by the sellers.

        Returns
        -------
        array_like
            The new state of the environment after taking the action.
        float
            The reward achieved by the action.
        bool
            A flag denoting whether the episode has ended.
        dict
            An empty dictionary for additional info (unused in this environment).
        """

        # Execute one time step within the environment
        assert self.action_space.contains(action)

        # Simple model: buyers buy from the cheapest seller
        sorted_sellers = np.argsort(action)
        self.state[0] = action[sorted_sellers[0]]
        self.state[1] = action[sorted_sellers[1]]

        # Distribute the buyers
        for i in range(2, 6):
            if self.state[i] >= self.state[0]:
                self.state[0] += self.state[i]
                self.state[i] = 0
            elif self.state[i] >= self.state[1]:
                self.state[1] += self.state[i]
                self.state[i] = 0

        # Set reward as the profit of the sellers
        reward = self.state[0] + self.state[1]

        # Set done flag if all buyers have bought the products
        done = np.sum(self.state[2:]) == 0

        # Save the prices to history
        self.prices_history.append(action)

        return self.state, reward, done, {}

    def reset(self):
        """Reset the state of the environment to an initial state.

        Returns
        -------
        array_like
            The initial state of the environment.
        """

        # Reset the state of the environment to an initial state
        self.state = np.zeros(6)
        # Initialize buyers' willingness to pay
        self.state[2:6] = np.random.uniform(low=0, high=100, size=4)
        return self.state
