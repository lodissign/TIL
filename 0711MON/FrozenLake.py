import tensorflow as tf
import gym
from gym.envs.registration import register
import msvcrt
import readchar
import colorama as cr
 
cr.init(autoreset=True)
 
#MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3
 
arrow_keys = {
    '\x1b[A' : UP,
    '\x1b[B' : DOWN,
    '\x1b[C' : RIGHT,
    '\x1b[D' : LEFT
}
 
env_dict = gym.envs.registry.env_specs.copy()
 
for env in env_dict:
    if'FrozenLake-v3' in env:
        del gym.envs.registry.env_specs[env]
        
register(
    id='FrozenLake-v3',
    entry_point="gym.envs.toy_text:FrozenLakeEnv",
    kwargs={'map_name':'4x4','is_slippery':False}
)
 
env = gym.make("FrozenLake-v3")
env.render() # 환경을 화면으로 출력
 
while True:
    key = readchar.readkey()  # 키보드 입력 받기
 
    if key not in arrow_keys.keys():
        print("Game aborted!")
        break
 
    action = arrow_keys[key] # 에이전트의 움직임
    state, reward, done, info = env.step(action) # 움직임에 따른 return값
    env.render() # 화면 출력
    print("State:", state, "Action", action, "Reward:", reward, "Info:", info)
 
    if done: #도착 시 게임 종료
        print("Finished with reward", reward)
        break