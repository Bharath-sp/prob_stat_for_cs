# This starter code was written by Alex Tsun for CSE 312 Summer 2020.


import numpy as np
np.set_printoptions(precision=4, suppress=True)

"""
Col 1: pokemon_id: A unique identifier for the Pokemon.
Col 2: is_legendary: A 1 if the Pokemon is legendary, and 0 otherwise.
Col 3: height: The height of the Pokemon in meters.
Col 4: weight: The weight of the Pokemon in kilograms.
Col 5: encounter_prob: The probability of encountering this Pokemon 
in the wild grass. Note the sum of this entire column is 1, since when
you make an encounter, exactly one of these Pokemon appears.
Col 6: catch_prob: Once you have encountered a Pokemon, the probability 
you catch it
"""

def part_a(filename:str='data/pokemon.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob. """
    data = np.genfromtxt(filename)
    return np.mean(data[:,1:], axis=0)


def part_b(filename:str='data/pokemon.txt'):
    """
    Compute the proportion of Pokemon that are legendary, the average
    height, the average weight, the average encounter_prob, and average 
    catch_prob OF ONLY those Pokemon STRICTLY heavier than the median weight.
    """
    data = np.genfromtxt(filename)
    mask = np.where(data[:,3] >np.median(data[:,3]))
    high_weigh_pokemon = data[mask]
    return np.mean(high_weigh_pokemon[:,1:], axis=0)
 

def part_c(filename:str='data/pokemon.txt', ntrials:int=500):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you ENCOUNTER each Pokemon 
    (at least) once? """
    data = np.genfromtxt(filename)
    def sim_one():
        rng = np.random.default_rng()
        encountered = []
        num_of_encounters=0
        while len(set(encountered)) != 25:
            num_of_encounters += 1
            encountered.append(rng.choice(a=data[:,0],p=data[:,4])) 
            #the vector of probabilities should sum to 1
        return num_of_encounters
    
    total_encounters = 0
    for i in range(ntrials):
        total_encounters += sim_one()
    return total_encounters/ntrials

def part_d(filename:str='data/pokemon.txt', ntrials:int=500):
    """
    Suppose you are walking around the wild grass, and you wonder: how
    many encounters do you expect to make until you CATCH each Pokemon 
    (at least) once? """
    data = np.genfromtxt(filename)[:, -2:]

    def sim_one():
        rng = np.random.default_rng()
        pk_remaining = np.arange(data.shape[0])
        num_of_encounters = 0
        while len(pk_remaining) != 0:
            num_of_encounters += 1
            encountered = rng.choice(a=np.arange(data.shape[0]),p=data[:,0])
            if encountered in pk_remaining and  np.random.rand() < data[encountered,1]:
                pk_remaining = pk_remaining[pk_remaining != encountered]
        return num_of_encounters
    
    total_encounters = 0
    for i in range(ntrials):
        total_encounters += sim_one()
    return total_encounters/ntrials


if __name__ == '__main__':
    print(part_a())
    print(part_b())
    print(part_c())
    print(part_d())