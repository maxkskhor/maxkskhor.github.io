import random
import matplotlib.pyplot as plt

# Objective: Find out the optimal number h of an explore-exploit strategy
# that maximises the chance of finding the *best* candidate

# a list of numbers from 1 to 100
# assume 100 is the best candidate, 1 is the worst
seq = [i for i in range(1, 101)]


def run_experiment(N: int = 1000):
    res = {}
    for stop in range(1, 101):
        res[stop] = 0
        # run the experiment N times
        for _ in range(N):
            # shuffle the list in place
            random.shuffle(seq)
            highest_num_so_far = max(seq[:stop + 1])
            candidate_chosen = seq[-1]
            for current_candidate in seq[stop + 1:]:
                # if the current candidate is better than all the previous candidates, we will take it
                if current_candidate > highest_num_so_far:
                    candidate_chosen = current_candidate
                    break
            # add one to counter if candidate chosen is the best (100)
            if candidate_chosen == 100:
                res[stop] += 1
    
    for i in res:
        res[i] /= N
    return res


if __name__ == '__main__':
    n = 50000
    res = run_experiment(n)
    plt.plot(res.keys(), res.values())
    plt.title(f'Run Experiment {n} times')
    plt.ylabel('Probability of getting best candidate')
    plt.xlabel('Exploration stopping point')
    plt.show()
