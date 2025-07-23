from gym import spaces
import gym
import numpy as np
from snake_envs.game_logic import SnakeGame, ACTION_MAP  

class SnakeEnv(gym.Env):
    def __init__(self, grid_size=20, render_mode=False):  
        super(SnakeEnv, self).__init__()
        self.grid_size = grid_size
        self.render_mode = render_mode

        self.game = SnakeGame(grid_size=self.grid_size, render_mode=self.render_mode)

        
        self.observation_space = spaces.Box(
        low=-1.0,
        high=1.0,
        shape=(11,),
        dtype=np.float32
        )

        
        self.action_space = spaces.Discrete(4)

    def reset(self):
        obs = self.game.reset()
        return obs

    def step(self, action):
        reward, done = self.game.step(action)
        obs = self.game.get_observation()
        return obs, reward, done, {}

    def render(self, mode="human"):
        self.game.render()

    def close(self):
        self.game.close()  