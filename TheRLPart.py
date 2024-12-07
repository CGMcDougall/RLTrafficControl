import Profhelpers as ph
from Traffic_env.envs import MonoIntersection as MI
import numpy as np


from Traffic_env.envs.MonoIntersection import IntersectionControl


## SARSA
def sarsa(env, gamma, step_size, epsilon, max_episode=20, ep_iterations=50000):
    def chooseAction(state):
        explore = (np.random.uniform(0, 1) <= epsilon)

        if explore:
            action = np.random.randint(0, env.n_actions)
        else:
            action = np.argmax(q[state])
        return action

    q = np.random.rand(env.n_states, env.n_actions)
    # q[env.goal] = np.zeros((env.n_actions))

    for i in range(max_episode):
        state, _ = env.reset()
        action = chooseAction(state)
        print(i)
        for j in range(ep_iterations):
            # take step

            new_state, reward, terminated, trunc = env.step(action)
            env.action()

            # choose new action based on new_state using epsilon greedy policy
            new_action = chooseAction(new_state)

            # note for report: removing discount factor helped calm variability/spikes

            # calculation
            q[state, action] = q[state, action] + step_size * (reward +
                                                               (gamma * q[new_state, new_action] - q[state, action]))

            state = new_state
            action = new_action

    return q, env.mat.Data

def runQLearning(env,max_episode,total_iterations,basePolicy = []):


    def Learn(env, iteration,state,gamma, step_size, epsilon, discount_rate=0.99):

        Discount_Factor = np.power(discount_rate, iteration)
        explore = (np.random.uniform(0, 1) <= epsilon)

        if explore:
            action = np.random.randint(0, env.n_actions)
        else:
            action = np.argmax(QTable[state])

        next_state, reward, terminated, trunc = env.step(action)

        QTable[state,action] = QTable[state,action] + step_size*((Discount_Factor*reward)+gamma*np.max(QTable[next_state]) - QTable[state,action])

        return next_state

    if len(basePolicy) != 0:
        QTable = basePolicy
    else:
        QTable = np.zeros((env.n_states, env.n_actions))

    #QTable = np.zeros((env.n_states, env.n_actions))


    for i in range(0,total_iterations):
        print(i)
        state, _ = env.reset()
        for j in range(0,max_episode):

            env.action()
            state = Learn(env,j,state,gamma=0.9,step_size=0.9,epsilon=0.01,discount_rate=0.99)



    return QTable, env.mat.Data

if __name__=="__main__":
    monoInt = IntersectionControl(mat_size=14, Lanes=2, render_mode="None")
    q, d = runQLearning(monoInt,1000000,15)
    #print(q)
    # f = open("QTable.txt","w")
    #
    # for x in q:
    #     s = ' '.join(str(xs) for xs in x) + "\n"
    #     f.write(s)
    # #f.writelines(q)
    # f.close()

    # monoInt2 = IntersectionControl(mat_size=14, Lanes=2, render_mode="human")
    # q1, _ = runQLearning(monoInt2, 10000, 1,q)

    d.plot()





















