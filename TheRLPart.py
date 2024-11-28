import Profhelpers as ph
from Traffic_env.envs import MonoIntersection as MI
import numpy as np


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




