from stable_baselines3 import PPO
from snake_envs.snake_env import SnakeEnv
import time


env = SnakeEnv(grid_size=20, render_mode=True)


model = PPO.load("models/ppo_snake")


obs = env.reset()
done = False
n_episodes = 100
for episode in range(n_episodes):
    obs = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, _ = model.predict(obs)
        obs, reward, done, _ = env.step(action)
        env.render()
        time.sleep(0.1)
        total_reward += reward
    print(f"Episode {episode + 1}: Total Reward = {total_reward}")
env.close()