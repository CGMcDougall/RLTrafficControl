import Profhelpers as ph
from Traffic_env.envs import MonoIntersection as MI
import numpy as np


##IDK ABOUT THIS TBH,
def basicGreedPolicy(env, q):
    pi = []
    for i in range(env.n_states):
        max = np.argmax(q[i])
        l = [0, 0, 0, 0]
        l[max] = 1
        pi += [l]

    pi = np.array(pi)

    Pi = ph.diagonalization(pi, env.n_states, env.n_actions)

    return Pi



##3QLearnign maybe idk
def QLearning(env,gamma,step_size,epsilon,discount_rate=0.99,max_episode=1000):

    QTable = np.zeros((env.n_states, env.n_actions))
    state = 0

    for i in range(0,max_episode):

        Discount_Factor = np.power(discount_rate,i)

        explore = (np.random.uniform(0, 1) <= epsilon)

        if explore:
            action = np.random.randint(0, env.n_actions)
        else:
            action = np.argmax(QTable[state])


        ##Observe results from step
        next_state, reward, terminated, trunc = env.step()

        #Qlearning math
        original_val = QTable[state,action]

        new_max = np.argmax(QTable[next_state])

        ##Discount Rate required for continuous tasks
        new_reward = ((reward * Discount_Factor) + gamma * QTable[next_state][new_max])

        QTable[state,action] = original_val + step_size * (new_reward - original_val)

        state = next_state

    return basicGreedPolicy(env,QTable), QTable




def runQLearning(env,max_episode,total_iterations):

    def Learn(env,gamma,step_size,epsilon,iteration,discount_rate=0.99):

        Discount_Factor = np.power(discount_rate, iteration)
        explore = (np.random.uniform(0, 1) <= epsilon)
        if explore:
            action = np.random.randint(0, env.n_actions)
        else:
            action = np.argmax(QTable[state])

        next_state, reward, terminated, trunc = env.step()

        QTable[state,action] = QTable[state,action] + step_size*((discount_rate*reward)+gamma*np.max(QTable[next_state]) - QTable[state,action])

        state = next_state


    QTable = np.zeros((env.n_states, env.n_actions))

    for i in range(0,total_iterations):

        state, _ = env.reset()
        for j in range(0,max_episode):
            #Do a thing idk
            Learn(env,gamma,)


















