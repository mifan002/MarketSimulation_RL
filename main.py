import matplotlib.pyplot as plt
from stable_baselines3 import PPO

from src.EvaluateModel import evaluate_model
from src.MarketEnvironment import MarketEnvironment


def main():
    env = MarketEnvironment()

    # Initialize reinforcement learning agents
    model1 = PPO("MlpPolicy", env, verbose=1)

    # Train agents
    model1.learn(total_timesteps=20000)

    # Evaluate the first agent
    mean_reward1, actions1 = evaluate_model(model1, env)
    print(f"Mean reward for the first agent: {mean_reward1}")

    # Plot prices for the first agent
    for i, actions in enumerate(actions1):
        plt.plot(actions, label=f"Episode {i+1}")
    plt.title("Prices for model 1")
    plt.xlabel("Time step")
    plt.ylabel("Price")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
