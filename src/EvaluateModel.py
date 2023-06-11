import numpy as np


def evaluate_model(model, env, num_episodes=1):
    """Evaluate a trained model on a specified environment.

    Parameters
    ----------
    model : stable_baselines3.common.base_class.BaseAlgorithm
        The trained model to be evaluated.
    env : gym.Env
        The Gym environment on which the model is evaluated.
    num_episodes : int, optional
        The number of episodes for which the model is evaluated, by default 1.

    Returns
    -------
    float
        The mean reward achieved by the model over all episodes.
    list of list
        The list of actions taken by the model in each episode.
    """

    episode_rewards = []
    episode_actions = []
    for i in range(num_episodes):
        obs = env.reset()
        done = False
        episode_reward = 0
        actions = []
        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, info = env.step(action)
            episode_reward += reward
            actions.append(action)
        episode_rewards.append(episode_reward)
        episode_actions.append(actions)
    return np.mean(episode_rewards), episode_actions
