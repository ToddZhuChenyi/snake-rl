
import yaml
import torch
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import SubprocVecEnv
from snake_envs.snake_env import SnakeEnv
policy_kwargs = dict(net_arch=[256, 128])
if __name__ == "__main__":
    
        device = "cpu"
        print(f"✅ 使用设备: {device}")

    
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)


        num_envs = config.get("num_envs", 16)

        def make_env():
            def _init():
                return SnakeEnv(grid_size=20, render_mode=False)
            return _init

        env = SubprocVecEnv([make_env() for _ in range(num_envs)])

   
        model = PPO(
         "MlpPolicy",
        env,
        learning_rate=config["learning_rate"],
        n_steps=config["n_steps"],
        batch_size=config["batch_size"],
        gamma=config["gamma"],
        gae_lambda=config["gae_lambda"],
        clip_range=config["clip_range"],
        ent_coef=config["ent_coef"],
        verbose=config["verbose"],
        device=device,tensorboard_log="./tensorboard_logs",
        policy_kwargs=policy_kwargs
    )

   
        model.learn(total_timesteps=config["total_timesteps"], progress_bar=True)

    
        model.save("models/ppo_snake")
        print("✅ 模型训练完成并保存为 models/ppo_snake.zip")