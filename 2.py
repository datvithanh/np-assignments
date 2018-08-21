import numpy as np

def point_on_plane(p1 = [], p2 = [], p3 = [], p0 = []):
    v1 = p3 - p1
    v2 = p2 - p1
    cp = np.cross(v1, v2)
    a, b, c = cp
    
    d = -np.dot(cp, p3)

    u = np.array([a, b, c])

    t = -(np.sum(np.multiply(np.ndarray.tolist(p0), [a, b, c])) + d)/np.sum(np.multiply(u,u)) 

    res = u * t + p0

    return res
    

print(point_on_plane(np.array([2, 4, 5]), np.array([4, 7, 9]),
                     np.array([7, 9, 2]), np.array([30, 25, 56])))



