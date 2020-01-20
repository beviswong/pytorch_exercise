import numpy as np
import torch

a = np.array([2, 3.3])
b = torch.tensor(a)
print("b = {}".format(b))

c = np.ones([3, 3])
d = torch.from_numpy(c)

e = np.zeros([4, 4])
print("d = {}".format(d))