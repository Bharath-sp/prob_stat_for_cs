# This starter code was written by Alex Tsun for CSE 312 Summer 2020.

import numpy as np
import matplotlib.pyplot as plt

def part_a(n:int=21, p:float=0.3, ntrials:int=5000):
    
    def sim_one_game(n, p):
        you = 0
        opp = 0
        while (you < n and opp < n) or abs(you-opp)<2:
            if np.random.rand()<p:
                you +=1
            else:
                opp +=1
        return int(max(you, opp) == you)

    you_win = 0
    for i in range(ntrials):
        you_win += sim_one_game(n,p)
    return you_win/ ntrials
    

def part_b():
    x_vals = np.array(np.arange(0,1.02,0.02))
    game_pts =[3,11,21]
    color_list = ["-b", "-r", "-g"]
    y_vals= np.array([[part_a(n,p) for p in x_vals] for n in game_pts])

    for i, n in enumerate(game_pts):
        plt.plot(x_vals, y_vals[i], color_list[i], label="n={}".format(n))
    plt.legend(loc="upper left")
    plt.xlabel('P(win point)')
    plt.ylabel('P(win game)')
    plt.title('Relating P(win point) to P(win game)')
    plt.savefig("ping pong.png")
    

if __name__ == '__main__':
   # print(part_a())
    part_b()
