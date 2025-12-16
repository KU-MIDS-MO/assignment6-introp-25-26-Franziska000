##task3

#Write a function:
#`random_unit_vectors(num_vectors, dim)`
#that:
#a)creates a matrix M of shape (num_vectors, dim)using;
#Hier Vektor, also Liste von Zahlen

#M = np.random.randn(num_vectors, dim)

#b)normalizes each row so it has Euclidean norm 1,
#Hier jetzt die Länge des Vektors, aber erst geteilt durch 1, weil Einheitsvektor (Richtung bleibt gleich), 
#und dann Wurzel v**2 + v**2 + ...

#and c)returns the resulting matrix as a NumPy array.
#also return M_Euclidean norm

import numpy as np

def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)
    
    M_Euclidean_norm = np.zeros((num_vectors, dim))
    
    for i in range(num_vectors):
        v = M[i]
        length = np.sqrt(sum(x**2 for x in v))
        M_Euclidean_norm[i] = v / length
    
    
    return M_Euclidean_norm
    
    pass

print(random_unit_vectors(3, 2))
    
