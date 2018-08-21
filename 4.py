import numpy as np 

"""

df/dx0 = (df/dy0) * (dy0/dx0) + (df/dy1) * (dy1/dx0)
tuong tu df/dx1
"""

dfy = np.array([5, 12])

y = np.array([[5, 3, 1], [7, 2, 9]])

print(y[:, range(2)])

dfx = np.dot(y[:, range(2)].T, dfy)

print(dfx)

