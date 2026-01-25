from scipy import io
import numpy as np
import matplotlib.pyplot as plt

classi = io.loadmat('classi.mat')

# Loading .mat file of neurone data as 2 matrices
cat1 = classi['cat1']
cat2 = classi['cat2']

print(np.size(cat1, 0))

# Number of neurones
numN = np.arange(0, np.size(cat1, 0))

print(numN)


plt.plot(cat1[:, 0],numN, 'o')

plt.xticks(np.arange(0,1, step=0.01))
plt.yticks(np.arange(0, np.size(numN), step=5))


plt.show()

