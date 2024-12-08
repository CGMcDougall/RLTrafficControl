import TheRLPart
from Traffic_env.envs.MonoIntersection import IntersectionControl

if __name__=="__main__":
    #QLearning
    monoInt = IntersectionControl(mat_size=14, Lanes=2, render_mode="None")
    q, d = TheRLPart.runQLearning(monoInt,1000000,15)

    #Sarsa
    #monoInt = IntersectionControl(mat_size=14, Lanes=2, render_mode="None")
    #q, d = TheRLPart.sarsa(monoInt, gamma=0.9, step_size=0.9, epsilon=0.05)

    d.plot()
