from gymnasium.envs.registration import register

register(
    id="Traffic_env/GridWorld-v0",
    entry_point="Traffic_env.envs:GridWorldEnv",
)
