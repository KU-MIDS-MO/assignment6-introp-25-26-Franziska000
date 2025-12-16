##task1

# Write a function:
# `estimate_pi(num_samples)`
# that:
# returns an estimate of π using num_samples random points generated with np.random.rand().
#Ich habe Quadrat und in Quadrat ist Viertelkreis und jetzt habe ich random Punkte und will schauen,
#wie viel Punkte im Kreis und wie viel außerhalb sind, also das Verhältnis
#Und die Fläche vom Kreis berechne ich ja so: A = π*r**2 // 4; also Punkte im Kreis // alle Punkte = π // 4 -> return π = 4 * Verhältnis
#r = 1, also π // 4
#Wo der Punkt jeweils ist weiß ich durch Pythagoras, x**2 + y**2, also wenn x**2 + y**2 <= 1, dann liegt Punkt im Kreis

import numpy as np

def estimate_pi(num_samples):
    count_inside = 0
    
    for i in range(num_samples):
        x, y = np.random.rand(2)
        
        if x**2 + y**2 <= 1:
            count_inside += 1
    
    ratio = count_inside / num_samples
    
    estimate_pi = 4 * ratio
    
    return estimate_pi

    pass

print(estimate_pi(5000))