import numpy as np

aa = np.mat(np.array([[1,2],[2,3],[1,4],[3,2],[2,4],[1,2],[2,6]]))
print(aa[:,0].reshape(1,7).A[0])