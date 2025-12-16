##task2

#Write a function:
#`get_random_subset_of_naturals_up_to_20()`
#that:
#outputs a random subset of the set of integers between $1$ and $20$ in the format of a `numpy` array.
#The draw of the subset should be uniform, i.e., any subset should in principle have the same chance to be outputted by your function. This problem will be graded manually.
#For $2$ out of the $5$ points allotted to this problem, you can write your function however you wish. To get $5$ points, your function is allowed to make a single call to the `numpy.random.randint()` method
#but it cannot make use of any other random methods.

#Ich habe einen Array, also verschiedene Zahlen und für jede Zahl wird zufällig separat entschieden,
#ob Zahl behalten wird oder weggfällt und so entsteht dann neuer Array/ zufällige Teilmenge
#Aber dass 0 Elemente drin sind, nur 1 Möglichkeit, dass 1 Element drin ist 20 Möglichkeiten, ..., dass alle Elemente drin sind auch nur 1 Möglichkeit (20 über k)
#Also mache ich, es wählt x Zahlen in Teilmenge aus und danach wählt es spezielle Teilmenge aus
#%%
#Nur Teilmengen

import numpy as np 

def get_random_subset_of_naturals_up_to_20():
    subset = []
    for i in range(1, 21):
        if np.random.randint(0, 2) == 1:
            subset.append(i)
    
    return np.array(subset)
    
    pass

print(get_random_subset_of_naturals_up_to_20())

#%%
#Anzahl der Teilmengen gleich wahrscheinlich

import numpy as np 

def get_random_subset_of_naturals_up_to_20():
    n = list(range(1, 21))
    size = np.random.randint(0, 21)
    
    subset = []
    while len(subset) < size:
        a = np.random.randint(1, 21)
        if a not in subset:
            subset.append(a)
    
    return np.array(subset)

print(get_random_subset_of_naturals_up_to_20())