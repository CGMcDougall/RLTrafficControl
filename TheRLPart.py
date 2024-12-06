import Profhelpers as ph
from Traffic_env.envs import MonoIntersection as MI
import numpy as np


from Traffic_env.envs.MonoIntersection import IntersectionControl


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


    def Learn(env, iteration,state,gamma, step_size, epsilon, discount_rate=0.99):

        Discount_Factor = np.power(discount_rate, iteration)
        explore = (np.random.uniform(0, 1) <= epsilon)


        forced, a = env.forcedAction()
        #print(forced)


        if forced:
            action = int(a)
        elif explore:
            action = np.random.randint(0, env.n_actions)
        else:
            action = np.argmax(QTable[state])
            #print(action)
        #print(QTable[state])
        # if action == 0:
        #     print(action)

        next_state, reward, terminated, trunc = env.step(action)

        QTable[state,action] = QTable[state,action] + step_size*((Discount_Factor*reward)+gamma*np.max(QTable[next_state]) - QTable[state,action])
        #print(QTable)
        #if(action == 1):
            #print(reward)

        return next_state


    QTable = np.zeros((env.n_states, env.n_actions))


    for i in range(0,total_iterations):
        print(i)
        state, _ = env.reset()
        for j in range(0,max_episode):

            state = Learn(env,j,state,gamma=0.9,step_size=0.5,epsilon=0.01,discount_rate=0.99)

            env.action()

    return QTable, env.mat.Data.plot()

if __name__=="__main__":
    monoInt = IntersectionControl(mat_size=14, Lanes=2, render_mode="None")
    q = runQLearning(monoInt,10000,20)

    print(q)


















